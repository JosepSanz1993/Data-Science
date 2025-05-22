from trainmodel import model_train
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

class RandomForestModel(model_train):
    def __init__(self, data):
        self.data = self.load_data(data)
        self.data = self.data.to_pandas()

    def train_model(self,colum):
        X = self.data.drop(columns=[colum])
        y = self.data[colum]
        y_encoded = y.astype("category").cat.codes
        category_mapping = dict(enumerate(y.astype("category").cat.categories))

        X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)
        clf = RandomForestClassifier(random_state=42)
        clf.fit(X_train, y_train)
        y_pred = clf.predict(X_test)

        all_classes = list(category_mapping.keys())
        cm = confusion_matrix(y_test, y_pred, labels=all_classes)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=[category_mapping[i] for i in all_classes])
        
        plt.figure(figsize=(10,8))
        disp.plot(cmap=plt.cm.Blues)
        plt.xticks(rotation=45, ha='right') 
        plt.title("Matriz de Confusión - Random Forest")
        plt.tight_layout()
        plt.show()
