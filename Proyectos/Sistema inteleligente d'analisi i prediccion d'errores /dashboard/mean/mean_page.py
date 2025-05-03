from dashboard.pages.mean import st
from constant import *
import pandas as pd
class MeanPage:
    def make_eyelashes(self,data):
        tab1, tab2 = st.tabs(TABS)
        with tab1:
            st.title(f"Results of {data['model_name']}")
            st.write(f"Timestamp: {data['timestamp']}")
            st.subheader("Parameters")
            st.josn(data['parameters'])
            st.subheader("Stored Files")
            st.write(f"Model: {data['saved_model']}")
            if data.get('scaler') is not None:
                st.write(f"Scaler: {data['scaler']}")
            else:
                st.write("No scaler used")

        with tab2:
            st.subheader("Metrics of the model")
            st.markdown("Classification Report")
            report = data["metrics"]['classification_report']
            df = pd.DataFrame(report).transpose()
            st.dataframe(df.style.format(precision=2))
            if data['model_name'] == "Autoencoder":
                st.markdown("Mean Squared Error")
                st.line_chart(data['metrics']['mse'])
            elif data['model_name'] == "IsolationForest":
                st.write(data['metrics']['contamination'])
                st.write(data['metrics']['n_estimators'])
                st.write(data['metrics']['max_samples'])
            elif data['model_name'] == "RandomForestClassifier":
                st.write(data['metrics']['n_estimators'])


           