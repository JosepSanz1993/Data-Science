from datetime import datetime
from sklearn.metrics import classification_report,confusion_matrix
from sklearn.metrics import precision_score,recall_score,f1_score, accuracy_score
from utils.generate_docu import TrainingResultDocument

class IsolationForestResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "IsolationForest"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
       
        report = classification_report(y_test, y_pred, output_dict=True)
        report_confusion = confusion_matrix(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        acc = accuracy_score(y_test, y_pred)

        return {
            "model_name": self.model_name,
            "timestamp": datetime.now().isoformat(),
            "parameters": parameters,
            "metrics": {
                "classification_report": report,
                "confusion_matrix": report_confusion.tolist(),
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
                "accuracy": acc,
                "contamination": getattr(model, 'contamination', None),
                "n_estimators": getattr(model, 'n_estimators', None),
                "max_samples": getattr(model, 'max_samples', None)
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }