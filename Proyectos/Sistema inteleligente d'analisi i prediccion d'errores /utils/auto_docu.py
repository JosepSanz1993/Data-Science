from datetime import datetime
from sklearn.metrics import classification_report, mean_squared_error
from utils.generate_docu import TrainingResultDocument

class AutoencoderResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "Autoencoder"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        # Si es tracta de detecció d’anomalies, y_test i y_pred poden ser 0/1 o 1/-1
        try:
            report = classification_report(y_test, y_pred, output_dict=True)
        except Exception:
            report = {}

        # MSE de reconstrucció si aplica
        mse = mean_squared_error(y_test, y_pred) if y_test is not None else None

        return {
            "model_name": self.model_name,
            "timestamp": datetime.now().isoformat(),
            "parameters": parameters,
            "metrics": {
                "classification_report": report if report else None,
                "mse": mse
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }