from datetime import datetime
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.metrics import precision_score,recall_score,f1_score,auc,roc_curve
from utils.generate_docu import TrainingResultDocument
class AutoencoderResultDocument(TrainingResultDocument):
    def __init__(self,mse,mae):
        self.model_name = "Autoencoder"
        self.mse = mse
        self.mae = mae

    def generate(self, model, y_test, y_pred, parameters, saved_model_path, saved_scaler_path=None):
        
        report = classification_report(y_test, y_pred, output_dict=True)
        report_confusion = confusion_matrix(y_test, y_pred)
        precision = precision_score(y_test, y_pred)
        recall = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        fpr,tpr,_= roc_curve(y_test, y_pred)
        roc_auc = auc(fpr,tpr)
        acc = accuracy_score(y_test, y_pred)

        return {
            "model_name": self.model_name,
            "timestamp": datetime.now().isoformat(),
            "parameters": parameters,
            "metrics": {
                "classification_report": report if report else None,
                "mse": self.mse.tolist(),
                "mae": self.mae.tolist(),
                "confusion_matrix": report_confusion.tolist() if report_confusion is not None else None,
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
                "roc_auc": roc_auc,
                "accuracy": acc
            },
            "saved_model": saved_model_path,
            "saved_scaler": saved_scaler_path
        }