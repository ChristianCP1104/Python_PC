import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans, AgglomerativeClustering
from sklearn.preprocessing import StandardScaler

# Cargar el archivo CSV
df = pd.read_csv('./data/airbnb.csv', sep=',')

# Seleccionar las columnas relevantes para el agrupamiento
features = ['price', 'overall_satisfaction', 'reviews']
data = df[features]

# Convertir las columnas a valores numéricos y manejar valores faltantes
data = data.apply(pd.to_numeric, errors='coerce')
data = data.dropna()

# Normalizar los datos
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# Reindexar el DataFrame de datos limpios para asegurarnos de que coincida con el DataFrame original
data = data.reset_index(drop=True)

# 1. K-means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans_labels = kmeans.fit_predict(scaled_data)

# Número de etiquetas coincida con el número de filas en el DataFrame limpio
assert len(kmeans_labels) == len(data)

# Añadir las etiquetas de clúster al DataFrame original
df.loc[data.index, 'kmeans_cluster'] = kmeans_labels

# 2. Agglomerative Clustering
agg_clustering = AgglomerativeClustering(n_clusters=3)
agg_labels = agg_clustering.fit_predict(scaled_data)

# Número de etiquetas coincida con el número de filas en el DataFrame limpio
assert len(agg_labels) == len(data)

# Añadir las etiquetas de clúster al DataFrame original
df.loc[data.index, 'agg_cluster'] = agg_labels

# Visualización de K-means Clustering
plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
sns.scatterplot(data=df, x='price', y='overall_satisfaction', hue='kmeans_cluster', palette='viridis', s=50, alpha=0.7)
plt.title('K-means Clustering')
plt.xlabel('Price')
plt.ylabel('Review Scores Rating')

# Visualización de Agglomerative Clustering
plt.subplot(1, 2, 2)
sns.scatterplot(data=df, x='price', y='overall_satisfaction', hue='agg_cluster', palette='viridis', s=50, alpha=0.7)
plt.title('Agglomerative Clustering')
plt.xlabel('Price')
plt.ylabel('Review Scores Rating')

plt.tight_layout()
plt.show()
