import polars as pl
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from models.model.model import model_train
class Insolation(model_train):
    def __init__(self,input_data):
        self.__df = self.load_data(input_data)
    
    def train_model(self):
        #Seleccionar los campos
        X = self.__df.select(["cpu_usage", "ram_usage", "disk_usage", "temperature", "network_latency"]).to_pandas() 
        #Separar las variables en entrenamiento y test
        X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
        #Crear el modelo
        model = IsolationForest(contamination=0.05, random_state=42)
        #Entrenar modelo
        model.fit(X_train)
        #Realizar la prediccion con X_test
        y_pred = model.predict(X_test)
        #Convertir las predicciones a un formato comprensible (1 para normal, -1 para anomalia)
        y_pred = ["Normal" if label == 1 else "Anomaly" for label in y_pred]
        #Mostrar la classificacion
        print(classification_report(["Normal"] * len(X_test), y_pred))
        return model

