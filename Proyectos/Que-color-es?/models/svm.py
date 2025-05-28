import models.trainmodel as pl
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report
from models.trainmodel import model_train
import matplotlib.pyplot as plt

class SVMColorClassifier(model_train):
    def __init__(self,path):
        self.model = None
        self.path = path
        self.le = LabelEncoder()
        self.scaler = StandardScaler()
    
    def train_model(self, label_col):
        df = self.load_data(self.path)
        df_pd = df.to_pandas()
    
        X = df_pd.drop(columns=[label_col])
        y = df_pd[label_col]
        
        y_enc = self.le.fit_transform(y)

        X_train, X_test, y_train, y_test = train_test_split(X, y_enc, test_size=0.3, random_state=42)
        self.model = make_pipeline(StandardScaler(), SVC(kernel='rbf', C=1, gamma='scale'))
        self.model.fit(X_train, y_train)
        y_pred = self.model.predict(X_test)
        
        cm = confusion_matrix(y_test, y_pred)
        print("Matriz de confusión:")
        print(cm)
        plt.title('Matriz de confusión SVM')
        plt.figure(figsize=(10, 7))
        plt.imshow(cm, cmap='Blues', interpolation='nearest')
        plt.xlabel('Predicción')
        plt.ylabel('Realidad')
        plt.show()


        labels = sorted(set(y_test))
        target_names = self.le.inverse_transform(labels)
        cr = classification_report(y_test, y_pred, labels=labels, target_names=self.le.classes_)
        print("\nInforme de classificación:")
        print(cr)
        plt.title('Reporte de clasificación SVM')
        plt.figure(figsize=(10, 7))
        plt.imshow(confusion_matrix(y_test, y_pred, labels=labels), cmap='Blues', interpolation='nearest')
        plt.xlabel('Predicción')
        plt.ylabel('Realidad')
        plt.show()

        
    def predict_color(self, sample_dict):
        import pandas as pd
        X_sample = pd.DataFrame([sample_dict])
        y_pred_enc = self.model.predict(X_sample)
        return self.le.inverse_transform(y_pred_enc)[0]
    

