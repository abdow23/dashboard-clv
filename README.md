# dashboard-clv
Sistema de recomendación y predicción de CLV para PYMES
# 🎯 Sistema de Recomendación y Predicción de CLV para PYMES

Este proyecto forma parte del Trabajo Final del Máster en Visualización de Datos y tiene como objetivo construir un sistema interactivo para analizar el valor de los clientes (CLV), segmentarlos mediante clustering y generar recomendaciones personalizadas para acciones de marketing.

---

## 📌 Funcionalidades del Proyecto

- Predicción del **Customer Lifetime Value (CLV)**.
- Segmentación automática de clientes mediante **K-Means Clustering**.
- Generación de **recomendaciones personalizadas de marketing**.
- Visualización interactiva a través de un **dashboard en Streamlit**.

---

## 📁 Estructura del Proyecto

├── dashboard.py # Dashboard interactivo en Streamlit
├── calcular_clv.py # Script para calcular el CLV
├── clustering_clientes.py # Segmentación automática con KMeans
├── recomendaciones_marketing.py # Asignación de recomendaciones
├── datos_retail/ # Carpeta con datasets (input/output)
│ └── clientes_limpios.csv
├── requirements.txt # Librerías necesarias
└── README.md # Este archivo


---

## 🧪 Cómo Ejecutar el Proyecto

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/dashboard-clv.git
   cd dashboard-clv
Instala los requisitos:
pip install -r requirements.txt



Ejecuta el dashboard:

streamlit run dashboard.py

Requisitos Técnicos:

Python 3.8+

Streamlit

Pandas

NumPy

Plotly

scikit-learn

openpyxl


Enlace al Dashboard Online:



👤 Autor
Abdenour Souda
Máster en Visualización de Datos
Julio 2025
