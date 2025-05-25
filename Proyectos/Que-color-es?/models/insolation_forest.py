from models.trainmodel import model_train
from sklearn.ensemble import IsolationForest
from trainmodel import pl
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
class AnomalyCleaner(model_train):
    def __init__(self):
        self.cleaned_df = None
        self.df = None
        self.feature_columns = None
        self.anomalies = None

    def load_data(self, input_data):
        self.df = super().load_data(input_data)

    def train_model(self, column):
        if self.df is None:
            raise ValueError("No se han cargado los datos.")

        self.feature_columns = [
            col for col in self.df.columns
            if col != column and self.df[col].dtype in (pl.Float64, pl.Int64)
        ]

        if not self.feature_columns:
            raise ValueError("ho hay columnas numéricas disponibles para el entrenamiento.")

        df_pd = self.df.to_pandas()

        iso = IsolationForest(contamination=0.2, random_state=42)
        df_pd["anomaly"] = iso.fit_predict(df_pd[self.feature_columns])

        self.anomalies = df_pd[df_pd["anomaly"] == -1]
        df_clean = df_pd[df_pd["anomaly"] == 1].drop(columns=["anomaly"])

        self.cleaned_df = pl.from_pandas(df_clean)

    def get_clean_data(self):
        if self.cleaned_df is None:
            raise ValueError("Los datos todavia no se han processado.")
        return self.cleaned_df

    def export_clean_json(self, path="data/processed/cleaned_data.json"):
        if self.cleaned_df is None:
            raise ValueError("no hay datos a exportar.")
        self.cleaned_df.write_json(path)
        print(f"✔️ Fichero JSON exportado en: {path}")

    def show_anomalies(self):
        if self.anomalies is None or self.anomalies.empty:
            print("ℹ️ No se han detectado anomalies en este modelo.")
            return

        print("📊 Anomalias detectadas:")
        print(self.anomalies)

        sns.pairplot(self.anomalies[self.feature_columns])
        plt.suptitle("Anomalias detectadas (Isolation Forest)", y=1.02)
        plt.tight_layout()
        plt.show()

"""if __name__ == "__main__":

    cleaner = AnomalyCleaner()
    cleaner.load_data("data/processed/color_sensor_data_processed.json")
    cleaner.train_model("Color")
    cleaner.show_anomalies()               
    cleaner.export_clean_json()"""
