from datetime import datetime
from sklearn.metrics import accuracy_score, classification_report
from utils.generate_docu import TrainingResultDocument

class RandomForestResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "RandomForestClassifier"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        return {
            "model_name": self.model_name,
            "timestamp": datetime.utcnow(),
            "parameters": parameters,
            "metrics": {
                "accuracy": acc,
                "classification_report": report,
                "n_estimators": getattr(model, 'n_estimators', None),
                "max_depth": getattr(model, 'max_depth', None)
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }