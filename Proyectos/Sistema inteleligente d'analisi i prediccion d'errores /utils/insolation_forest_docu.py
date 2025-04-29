from datetime import datetime
from sklearn.metrics import classification_report
from utils.generate_docu import TrainingResultDocument

class IsolationForestResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "IsolationForest"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        # L'algorisme retorna 1 (normal) i -1 (anòmal)
        report = classification_report(y_test, y_pred, output_dict=True)

        return {
            "model_name": self.model_name,
            "timestamp": datetime.now().isoformat(),
            "parameters": parameters,
            "metrics": {
                "classification_report": report,
                "contamination": getattr(model, 'contamination', None),
                "n_estimators": getattr(model, 'n_estimators', None),
                "max_samples": getattr(model, 'max_samples', None)
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }