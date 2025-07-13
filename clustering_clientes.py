import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Cargar los datos
df = pd.read_csv("datos_retail/clv_clientes.csv")

# Seleccionar las columnas numéricas más relevantes
columnas_cluster = ["CLV", "FrecuenciaMensual", "ValorPromedioCompra"]
X = df[columnas_cluster]

# Escalar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Método del codo para encontrar el mejor número de clusters
inercia = []
rangos = range(1, 11)

for k in rangos:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    inercia.append(kmeans.inertia_)

# Mostrar gráfico del codo
plt.figure(figsize=(8, 4))
plt.plot(rangos, inercia, marker='o')
plt.xlabel("Número de clusters (k)")
plt.ylabel("Inercia")
plt.title("Método del codo para K-Means")
plt.grid(True)
plt.tight_layout()
plt.show()

# Elegir el número óptimo de clusters (por ejemplo, 4)
k_optimo = 4
kmeans_final = KMeans(n_clusters=k_optimo, random_state=42)
df["Cluster"] = kmeans_final.fit_predict(X_scaled)

# Guardar resultado
df.to_csv("datos_retail/clientes_segmentados.csv", index=False)
print("✅ Segmentación completada y guardada en: datos_retail/clientes_segmentados.csv")

# Visualización 2D
plt.figure(figsize=(8, 6))
sns.scatterplot(x=df["CLV"], y=df["FrecuenciaMensual"], hue=df["Cluster"], palette="Set2")
plt.title("Segmentación de clientes por CLV y Frecuencia")
plt.xlabel("CLV")
plt.ylabel("Frecuencia mensual")
plt.legend(title="Cluster")
plt.grid(True)
plt.tight_layout()
plt.show()
