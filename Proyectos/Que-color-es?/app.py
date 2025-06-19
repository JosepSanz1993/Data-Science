import streamlit as st
from models.mlp import ColorClassifier
from models.svm import SVMColorClassifier
from models.random_forest import RandomForestColorClassifier
from models.kmeans import KMeansColorClassifier
from models.insolation_forest import AnomalyCleaner
from scripts.global_var import DATA_PROCESSED, DATA_CLEANED,DATA_NOT_PROCESSED
from scripts.etl import ETL
import pandas as pd

st.set_page_config(page_title="Clasificador de Colores", layout="centered")
st.title("🎨 Clasificador Inteligente de Colores")

st.sidebar.title("🔧 Configuración del modelo")
use_anomaly_detection = st.sidebar.checkbox("Activar detección de anomalías", value=False)
model_type = st.sidebar.selectbox("Modelo de clasificación", ["MLP", "SVM", "Random Forest"])
show_kmeans = st.sidebar.checkbox("Visualizar clusters K-Means")

st.header("📥 Entrada de datos del sensor")
col1, col2 = st.columns(2)
with col1:
    red = st.number_input("🔴 Rojo (Red)", 0, 255, 110)
    green = st.number_input("🟢 Verde (Green)", 0, 255, 120)
    blue = st.number_input("🔵 Azul (Blue)", 0, 255, 115)
with col2:
    clear = st.number_input("💡 Claridad (Clear)", 0, 1000, 360)
    lux = st.number_input("☀️ Lux", 0, 1000, 85)

etl = ETL(DATA_NOT_PROCESSED)
etl.save_json(DATA_PROCESSED)

if use_anomaly_detection:
    st.info("🔍 Aplicando limpieza de anomalías...")
    anomaly = AnomalyCleaner()
    anomaly.load_data(DATA_PROCESSED)
    anomaly.train_model("Color")
    anomaly.export_clean_json(DATA_CLEANED)
    data_path = DATA_CLEANED
else:
    data_path = DATA_PROCESSED

input_dict = {
    "Red": red,
    "Green": green,
    "Blue": blue,
    "Clear": clear,
    "Lux": lux
}
input_list = [red, green, blue, clear, lux]

if "history" not in st.session_state:
    st.session_state.history = []

if st.button("🎯 Predecir Color"):
    if model_type == "MLP":
        model = ColorClassifier()
        model.load_data(data_path)
        model.train_model("Color")
        prediction = model.predict_color(input_list)

    elif model_type == "SVM":
        model = SVMColorClassifier(data_path)
        model.train_model("Color")
        prediction = model.predict_color(input_dict)

    elif model_type == "Random Forest":
        model = RandomForestColorClassifier()
        model.train_model("Color", data_path)
        prediction = model.predict_color(input_dict)

    st.session_state.history.append({
        "Modelo": model_type,
        "Input": input_dict,
        "Predicción": prediction
    })

    st.success(f"✅ Color predicho: **{prediction}**")

if st.session_state.history:
    st.subheader("📜 Historial de predicciones")
    hist_df = pd.DataFrame(st.session_state.history)
    st.dataframe(hist_df)

if show_kmeans:
    st.subheader("📊 Visualización de clusters (K-Means)")
    kmeans = KMeansColorClassifier(DATA_PROCESSED)
    st.pyplot(kmeans.visualize_clusters("Color"))  
    var = kmeans.check_cluster_Var("Cluster", "Color")
    try:
        st.info(f"📈 Varianza entre clusters: **{float(var):.4f}**")
    except (ValueError, TypeError):
        st.warning(f"⚠️ No s'ha pogut calcular la variança. Valor rebut: {var}")
   