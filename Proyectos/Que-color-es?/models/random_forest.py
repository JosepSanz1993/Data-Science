from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from models.trainmodel import model_train
class RandomForestColorClassifier(model_train):
    def __init__(self):
        super().__init__()
        self.model = None
        self.encoder = LabelEncoder()
        self.scaler = StandardScaler()
        self.fitted = False 

    def preprocess(self, df, target_column):
        df = df.rename({col: col.strip().capitalize() for col in df.columns})
        self.df = df

        X = df.drop(target_column)
        y = df[target_column]

        self.features = X.to_numpy()
        self.labels = self.encoder.fit_transform(y)

        self.features = self.scaler.fit_transform(self.features)

    def plot_confusion_matrix(self, y_true, y_pred, labels):
        cm = confusion_matrix(y_true, y_pred, labels=labels)
        plt.figure(figsize=(10, 8))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
                    xticklabels=self.encoder.inverse_transform(labels),
                    yticklabels=self.encoder.inverse_transform(labels))
        plt.xlabel("Predicción")
        plt.ylabel("Valor Real")
        plt.title("Matriz de Confusión")
        plt.tight_layout()
        plt.title("Matriz de Confusión random Forest")
        plt.show()

    def train_model(self, target_column,path):
        self.preprocess(self.load_data(path), target_column)

        X_train, X_test, y_train, y_test = train_test_split(
            self.features, self.labels, test_size=0.2, random_state=42
        )

        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_train, y_train)
        self.save_model(self.model,'random.pkl')
        self.save_encoder(self.encoder, 'random_encoder.pkl')
        self.save_scaler(self.scaler,"random_scaler.pkl")
        y_pred = self.model.predict(X_test)
        unique_labels = np.unique(y_test)

        print("Classificación:")
        print(classification_report(
            y_test,
            y_pred,
            labels=unique_labels,
            target_names=self.encoder.inverse_transform(unique_labels)
        ))

        self.plot_confusion_matrix(y_test, y_pred, labels=unique_labels)
        self.fitted = True

    def predict_color(self, input_dict):
        if not self.fitted:
            raise RuntimeError("Modelo no entrenado")

        expected_features = ["Red", "Green", "Blue", "Clear", "Lux"]
        input_ordered = [input_dict[feature] for feature in expected_features]

        input_scaled = self.scaler.transform([input_ordered])
        prediction = self.model.predict(input_scaled)
        predicted_color = self.encoder.inverse_transform(prediction)[0]
        print(f"🔮 Color predecido: {predicted_color}")
        return predicted_color
