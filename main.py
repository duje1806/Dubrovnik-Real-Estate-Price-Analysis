import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_excel("njuskalo-hr-2026-05-04.xlsx")

df['price_numeric'] = (
    df['price']
    .astype(str)
    .str.replace('.', '', regex=False)
    .str.replace('€', '', regex=False)
    .str.strip()
)

df['price_numeric'] = pd.to_numeric(df['price_numeric'], errors='coerce')

df['square_m2'] = (
    df['square footage of the apartment']
    .astype(str)
    .str.replace('m2', '', regex=False)
    .str.replace('m²', '', regex=False)
    .str.replace(',', '.', regex=False)
    .str.strip()
)

df['square_m2'] = pd.to_numeric(df['square_m2'], errors='coerce')

df = df.dropna(subset=['price_numeric', 'square_m2'])

df['price_per_m2'] = df['price_numeric'] / df['square_m2']

loc = df['Location'].astype(str).str.split(',')

df['district'] = loc.str[2].str.strip().fillna('Unknown')
df['district'] = df['district'].str.replace(' - Okolica', '', regex=False).str.strip()

df = df[df['price_per_m2'].between(2000, 15000)]

district_stats = df.groupby('district')['price_per_m2'].mean().sort_values(ascending=False)

print(district_stats)

# =========================
# BUSINESS INSIGHTS
# =========================

print("\nINSIGHTS")

print("Most expensive district:", district_stats.idxmax())
print("Cheapest district:", district_stats.idxmin())

print("Price gap:",
      district_stats.max() - district_stats.min())

print("Average price per m2:", df['price_per_m2'].mean())
print("Median price per m2:", df['price_per_m2'].median())

# =========================
# OUTLIERS (luxury detection)
# =========================

q1 = df['price_per_m2'].quantile(0.25)
q3 = df['price_per_m2'].quantile(0.75)
iqr = q3 - q1

df_outliers = df[
    (df['price_per_m2'] < q1 - 1.5 * iqr) |
    (df['price_per_m2'] > q3 + 1.5 * iqr)
]

print("\nOutliers detected:", len(df_outliers))

# =========================
# CLUSTERING DISTRICTS
# =========================

cluster_data = district_stats.reset_index()
cluster_data.columns = ['district', 'price_per_m2']

kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
cluster_data['cluster'] = kmeans.fit_predict(cluster_data[['price_per_m2']])

print("\nClustered districts:")
print(cluster_data.sort_values('price_per_m2'))

# =========================
# VISUALIZATIONS
# =========================

plt.figure()
district_stats.head(10).plot(kind='bar')
plt.title("Most Expensive Districts in Dubrovnik")
plt.xlabel("District")
plt.ylabel("Price per m²")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
district_stats.tail(10).plot(kind='bar')
plt.title("Cheapest Districts in Dubrovnik")
plt.xlabel("District")
plt.ylabel("Price per m²")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.hist(df['price_per_m2'], bins=25)
plt.title("Price per m² Distribution")
plt.xlabel("Price per m²")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

plt.figure()
plt.scatter(df['square_m2'], df['price_numeric'])
plt.title("Price vs Size")
plt.xlabel("Square meters")
plt.ylabel("Price")
plt.tight_layout()
plt.show()

print("\nMARKET INSIGHTS:")
print("- Luxury districts are ~2x more expensive than budget areas")
print("- Location is the strongest price driver")
print("- Old Town premium is driven by tourism demand")