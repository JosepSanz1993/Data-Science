from trainmodel import model_train
from sklearn.ensemble import IsolationForest
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

class IsolationForestModel(model_train):
    def __init__(self, json_path):
        self.json_path = json_path
        self.numeric_cols = ["Red", "Green", "Blue", "Clear", "Lux"]
        self.df = None
        self.model = None

    def preprocess(self):
        pl_df = self.load_data(self.json_path)
        self.df = pl_df.to_pandas()
        self.df[self.numeric_cols] = self.df[self.numeric_cols].astype(float)

    def inject_errors(self, n_errors=15):
        idxs = np.random.choice(self.df.index, size=n_errors, replace=False)
        for idx in idxs:
            col = np.random.choice(self.numeric_cols)
            self.df.at[idx, col] = float(self.df[col].min()) / 10

    def detect_anomalies(self):
        X = self.df[self.numeric_cols]
        iso = IsolationForest(contamination=0.05, random_state=42)
        self.df["anomaly"] = iso.fit_predict(X)

    def train_model(self, target_col):
        self.preprocess()
        self.inject_errors()
        self.detect_anomalies()

        df_clean = self.df[self.df["anomaly"] == 1]
        X = df_clean[self.numeric_cols]
        y = df_clean[target_col]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
        clf = DecisionTreeClassifier(random_state=42)
        clf.fit(X_train, y_train)
        self.model = clf
        y_pred = clf.predict(X_test)

        labels = sorted(y.unique())
        cm = confusion_matrix(y_test, y_pred, labels=labels)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)
        plt.figure(figsize=(10,8))
        disp.plot(cmap=plt.cm.Blues)
        plt.xticks(rotation=45, ha='right') 
        plt.title("Matriz de confusión (sin anomalias)")
        plt.tight_layout()
        plt.show()


        plt.figure(figsize=(8, 6))
        sns.scatterplot(data=self.df, x="Red", y="Green", hue="anomaly", palette={1: "blue", -1: "red"})
        plt.title("Anomalias detectadas con Isolation Forest (Red vs Green)")
        plt.xlabel("Red")
        plt.ylabel("Green")
        plt.legend(title="Anomaly")
        plt.show()






