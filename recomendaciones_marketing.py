import pandas as pd

# Cargar datos
df = pd.read_csv("clientes_segmentados.csv")

# Definir nombres de segmentos (opcional si ya existen)
nombres_clusters = {
    0: "Clientes Leales",
    1: "Clientes Nuevos",
    2: "Clientes en Riesgo",
    3: "Clientes Potenciales"
}

# Recomendaciones específicas por cluster
recomendaciones = {
    0: "Ofrecer programa de fidelización",
    1: "Enviar descuentos de bienvenida",
    2: "Reactivar con promociones",
    3: "Incentivar siguiente compra"
}

# Aplicar mapeo a nuevas columnas
df["Segmento"] = df["Cluster"].map(nombres_clusters)
df["Recomendacion"] = df["Cluster"].map(recomendaciones)

# Guardar archivo final
df.to_csv("clientes_segmentados.csv", index=False)
print("✅ Archivo guardado: clientes_segmentados.csv con columnas 'Segmento' y 'Recomendacion'")
