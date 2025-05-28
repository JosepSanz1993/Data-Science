from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report,confusion_matrix
from models.trainmodel import model_train
from models.trainmodel import pl
import matplotlib.pyplot as plt
import numpy as np

class ColorClassifier(model_train):
    def __init__(self):
        self.encoder = LabelEncoder()
        self.model = None
        self.features = None
        self.labels = None

    def preprocess(self, df: pl.DataFrame, target_column: str):
        self.features = df.drop(target_column).to_numpy()
        self.labels = self.encoder.fit_transform(df[target_column].to_numpy())

    def train_model(self,target_column):
        self.preprocess(self.df, target_column)
        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.labels, test_size=0.2, random_state=42
        )
        self.model = MLPClassifier(hidden_layer_sizes=(10, 10), max_iter=500, random_state=1)
        self.model.fit(X_train, y_train)

        y_pred = self.model.predict(X_test)
        unique_labels = np.unique(y_test)
        print("Classificación:")
        print(classification_report(y_test, y_pred, labels=unique_labels, target_names=self.encoder.classes_))
        plt.title('Reporte de clasificación mlp')
        plt.figure(figsize=(10, 7))
        plt.imshow(confusion_matrix(y_test, y_pred, labels=unique_labels), cmap='Blues', interpolation='nearest')
        plt.xlabel('Predicción')
        plt.ylabel('Realidad')
        plt.show()


        print("Matriz de confusión:")
        print(confusion_matrix(y_test, y_pred, labels=unique_labels))
        plt.title('Matriz de confusión mlp')
        plt.figure(figsize=(10, 7))
        plt.imshow(confusion_matrix(y_test, y_pred, labels=unique_labels), cmap='Blues', interpolation='nearest')
        plt.xlabel('Predicción')
        plt.ylabel('Realidad')
        plt.show()

    def predict_color(self, input_array):
        if self.model is None:
            raise Exception("El modelo no ha sido entrenado.")
        pred = self.model.predict([input_array])
        return self.encoder.inverse_transform(pred)[0]

    def load_data(self, input_data):
        self.df = super().load_data(input_data)
