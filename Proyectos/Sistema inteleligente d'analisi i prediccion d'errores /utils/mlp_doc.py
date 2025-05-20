from datetime import datetime
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import precision_score, recall_score, f1_score
from utils.generate_docu import TrainingResultDocument

class MLPResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "MLPClassifier"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path):
        acc = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred, output_dict=True)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        report_confusion = confusion_matrix(y_test, y_pred)
        return {
            "model_name": self.model_name,
            "timestamp": datetime.isoformat(datetime.now()),
            "parameters": parameters,
            "metrics": {
                "accuracy": acc,
                "classification_report": report,
                "confusion_matrix": report_confusion.tolist(),
                "precision": precision,
                "recall": recall,
                "f1_score": f1
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }