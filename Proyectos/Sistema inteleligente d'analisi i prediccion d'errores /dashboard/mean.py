import streamlit as st

st.set_page_config(
    page_title="Intelligent Error Detection System",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 Intelligent System for Error Analysis and Prediction")

st.sidebar.title("Navegació")
page = st.sidebar.radio("Ves a la pàgina:", [
    "Auto", "Insolation", "mean", "Random", "Mlp"
])

if page == "Auto":
    st.switch_page("Auto.py")
elif page == "Insolation":
    st.switch_page("Insolation.py")
elif page == "mean":
    st.switch_page("mean.py")
elif page == "Random":
    st.switch_page("Random.py")
elif page == "Mlp":
    st.switch_page("Mlp.py")

st.markdown("""
## Welcome

This application presents the results of different anomaly detection models trained on hybrid IT infrastructure data.  
We use models such as **Random Forest**, **Isolation Forest**, **Multi-Layer Perceptron (MLP)**, and **Autoencoders**.

Use the sidebar to navigate between the different model result pages.

---

### 🔍 Goal

To support IT professionals in identifying anomalies in system metrics like CPU, RAM, disk usage, temperature, and network latency using intelligent models.

### 🧰 Technologies Used

- **Machine Learning**: Random Forest, Isolation Forest, MLP, Autoencoders  
- **Data Source**: MongoDB  
- **Frontend**: Streamlit  
- **Backend**: Python

""")