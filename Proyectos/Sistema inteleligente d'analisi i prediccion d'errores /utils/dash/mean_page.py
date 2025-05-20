import streamlit as st
from utils.dash.constant import *
import pandas as pd
class MeanPage:
    def make_eyelashes(self,data):
        tab1, tab2, tab3 = st.tabs(TABS)
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
            st.markdown("Confusion Matrix")
            confusion_matrix = data[0]['metrics']['confusion_matrix']
            if confusion_matrix is not None:
                df_confusion = pd.DataFrame(confusion_matrix)
                st.dataframe(df_confusion.style.format(precision=2))
            st.markdown("Precision")
            st.write(data[0]['metrics']['precision'])
            st.markdown("Recall")
            st.write(data[0]['metrics']['recall'])
            st.markdown("F1 Score")
            st.write(data[0]['metrics']['f1_score'])
            st.markdown("ROC AUC")
            st.write(data[0]['metrics']['roc_auc'])
            st.markdown("Accuracy")
            st.write(data[0]['metrics']['accuracy'])
            if data[0]['model_name'] == "Autoencoder":
                st.markdown("Mean Squared Error")
                st.line_chart(data[0]['metrics']['mse'])
                st.markdown("Mean Absolute Error")
                st.line_chart(data[0]['metrics']['mae'])
            elif data[0]['model_name'] == "IsolationForest":
                st.write(f"contamination: {data[0]['metrics']['contamination']}")
                st.write(f"n_estimators: {data[0]['metrics']['n_estimators']}")
                st.write(f"max_samples: {data[0]['metrics']['max_samples']}")
            elif data[0]['model_name'] == "RandomForestClassifier":
                st.write(f"n_estimators: {data[0]['metrics']['n_estimators']}")

        with tab3:
            st.subheader("Graphs")
            model_name = data[0]['model_name']
            report = data[0]['metrics']['classification_report']
            if isinstance(report, dict):
                df_report = pd.DataFrame(report).transpose()
                df_report = df_report.drop(['accuracy'], errors='ignore') 
                df_plot = df_report[['precision', 'recall', 'f1-score']]
                st.markdown("### Precision, Recall i F1-Score per classe")
                st.bar_chart(df_plot)
                
            if model_name == "Autoencoder":
                st.markdown("### Evolució del MSE per mostra")
                mse = data[0]['metrics'].get('mse', [])
                if mse:
                    mse_df = pd.DataFrame({'MSE': mse})
                    st.line_chart(mse_df)