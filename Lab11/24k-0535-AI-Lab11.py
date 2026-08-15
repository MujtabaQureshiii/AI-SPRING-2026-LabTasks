import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import seaborn as sns


df = pd.read_csv("heart_rate.csv")

print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())


plt.figure(figsize=(12, 6))
df.boxplot()
plt.title("Boxplot of All Features")
plt.xticks(rotation=45)
plt.show()


df_clean = df.dropna()

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df_clean)

scaled_df = pd.DataFrame(scaled_data, columns=df_clean.columns)


X_2 = scaled_df.iloc[:, :2]

kmeans_2 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_2 = kmeans_2.fit_predict(X_2)

plt.figure(figsize=(6, 5))
plt.scatter(X_2.iloc[:, 0], X_2.iloc[:, 1], c=labels_2, cmap='viridis')
plt.scatter(kmeans_2.cluster_centers_[:, 0],
            kmeans_2.cluster_centers_[:, 1],
            s=200, c='red', marker='X')
plt.title("K-Means Clustering (2 Features)")
plt.xlabel("Feature 1")
plt.ylabel("Feature 2")
plt.show()


X_3 = scaled_df.iloc[:, :3]

kmeans_3 = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_3 = kmeans_3.fit_predict(X_3)

fig = plt.figure(figsize=(7, 6))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(X_3.iloc[:, 0], X_3.iloc[:, 1], X_3.iloc[:, 2],
           c=labels_3, cmap='viridis')

ax.scatter(kmeans_3.cluster_centers_[:, 0],
           kmeans_3.cluster_centers_[:, 1],
           kmeans_3.cluster_centers_[:, 2],
           s=200, c='red', marker='X')

ax.set_title("K-Means Clustering (3 Features)")
ax.set_xlabel("Feature_1")
ax.set_ylabel("Feature_2")
ax.set_zlabel("Feature_3")
plt.show()


kmeans_all = KMeans(n_clusters=3, random_state=42, n_init=10)
labels_all = kmeans_all.fit_predict(scaled_df)

# PCA for visualization (important step)
from sklearn.decomposition import PCA

pca = PCA(n_components=2)
reduced = pca.fit_transform(scaled_df)

plt.figure(figsize=(6, 5))
plt.scatter(reduced[:, 0], reduced[:, 1], c=labels_all, cmap='viridis')
plt.title("K-Means Clustering (All Features - PCA reduced)")
plt.xlabel("PCA 1")
plt.ylabel("PCA 2")
plt.show()
