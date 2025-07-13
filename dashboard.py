import pandas as pd
import streamlit as st
import plotly.express as px

# Cargar datos
df = pd.read_csv("clientes_segmentados.csv")

# Mapeo de clusters numéricos a nombres legibles
nombres_clusters = {
    0: "Clientes Leales",
    1: "Clientes Nuevos",
    2: "Clientes en Riesgo",
    3: "Clientes Potenciales"
}

recomendaciones_clusters = {
    0: "Ofrecer programa de fidelización",
    1: "Enviar descuentos de bienvenida",
    2: "Reactivar con promociones",
    3: "Incentivar siguiente compra"
}

# Aplicar mapeo a columnas nuevas
df["Segmento"] = df["Cluster"].map(nombres_clusters)
df["Recomendacion"] = df["Cluster"].map(recomendaciones_clusters)

# Título
st.title("Dashboard de Clientes y Recomendaciones")

# Gráfico de dispersión CLV vs Frecuencia
fig = px.scatter(
    df,
    x="FrecuenciaMensual",
    y="CLV",
    color="Segmento",
    hover_data=["CustomerID", "TotalGastado", "NumCompras"],
    title="Distribución de Clientes por Cluster (CLV vs Frecuencia Mensual)",
)
st.plotly_chart(fig)

# Filtro por segmento legible
st.header("Filtrar clientes por segmento")
opciones_legibles = df["Segmento"].unique()
opcion_elegida = st.selectbox("Selecciona un segmento (cluster):", opciones_legibles, key="filtro_segmento")

# Filtrar y mostrar tabla
df_filtrado = df[df["Segmento"] == opcion_elegida]
st.write(f"Clientes en el segmento: {opcion_elegida}")
st.dataframe(df_filtrado[[
    "CustomerID", "TotalGastado", "CLV", "FrecuenciaMensual", "Segmento", "Recomendacion"
]])
