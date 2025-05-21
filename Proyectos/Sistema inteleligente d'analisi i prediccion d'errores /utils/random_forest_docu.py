from datetime import datetime
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.metrics import precision_score,recall_score,f1_score,roc_auc_score
from utils.generate_docu import TrainingResultDocument

class RandomForestResultDocument(TrainingResultDocument):
    def __init__(self):
        self.model_name = "RandomForestClassifier"

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        acc = accuracy_score(y_test, y_pred) #Total true predictions percentage
        report = classification_report(y_test, y_pred, output_dict=True) # Classification report
        report_confusion = confusion_matrix(y_test, y_pred) # Confusion matrix
        precision = precision_score(y_test, y_pred) # Number of correct total true predictions 
        recall = recall_score(y_test, y_pred) #Number of real true predictions detected
        f1 = f1_score(y_test, y_pred) # Hermeneutic mean between precision and recall
        roc_auc = roc_auc_score(y_test, y_pred) # Area under the ROC curve

        return {
            "model_name": self.model_name,
            "timestamp": datetime.isoformat(datetime.now()),
            "parameters": parameters,
            "metrics": {
                "accuracy": acc,
                "classification_report": report,
                "confusion_matrix": report_confusion.tolist(),  # Convert to list for JSON serialization
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
                "roc_auc": roc_auc,
                "n_estimators": getattr(model, 'n_estimators', None),
                "max_depth": getattr(model, 'max_depth', None)
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }