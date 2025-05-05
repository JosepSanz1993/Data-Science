import streamlit as st
from utils.dash.constant import *
import pandas as pd
class MeanPage:
    def make_eyelashes(self,data):
        tab1, tab2 = st.tabs(TABS)
        with tab1:
            st.title(f"Results of {data[0]['model_name']}")
            st.write(f"Timestamp: {data[0]['timestamp']}")
            st.subheader("Parameters")
            st.json(data[0]['parameters'])
            st.subheader("Stored Files")
            st.write(f"Model: {data[0]['saved_model']}")
            if data[0]['saved_scaler'] is not None:
                st.write(f"Scaler: {data[0]['saved_scaler']}")
            else:
                st.write("No scaler used")

        with tab2:
            st.subheader("Metrics of the model")
            st.markdown("Classification Report")
            report = data[0]["metrics"]['classification_report']
            df = pd.DataFrame(report).transpose()
            st.dataframe(df.style.format(precision=2))
            if data[0]['model_name'] == "Autoencoder":
                st.markdown("Mean Squared Error")
                st.line_chart(data[0]['metrics']['mse'])
            elif data[0]['model_name'] == "IsolationForest":
                st.write(f"contamination: {data[0]['metrics']['contamination']}")
                st.write(f"n_estimators: {data[0]['metrics']['n_estimators']}")
                st.write(f"max_samples: {data[0]['metrics']['max_samples']}")
            elif data[0]['model_name'] == "RandomForestClassifier":
                st.write(f"n_estimators: {data[0]['metrics']['n_estimators']}")


           