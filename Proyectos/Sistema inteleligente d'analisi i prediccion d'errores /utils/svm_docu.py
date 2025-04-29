from datetime import datetime
from sklearn.metrics import accuracy_score, classification_report
from utils.generate_docu import TrainingResultDocument

class SVMResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "SVM"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)

        return {
            "model_name": self.model_name,
            "timestamp": datetime.now().isoformat(),
            "parameters": parameters,
            "metrics": {
                "accuracy": acc,
                "classification_report": report,
                "kernel": getattr(model, 'kernel', None),
                "C": getattr(model, 'C', None),
                "gamma": getattr(model, 'gamma', None)
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }