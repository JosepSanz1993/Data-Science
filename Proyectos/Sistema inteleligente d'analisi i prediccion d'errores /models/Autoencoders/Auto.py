import numpy as np
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from models.model.model import model_train

class Auto(model_train):
    def __init__(self,input_data):
        self.__df = self.load_data(input_data)

    def train_model(self):
        #Seleccionar los campos
        X = self.__df.select(["cpu_usage", "ram_usage", "disk_usage", "temperature", "network_latency"]).to_numpy()
        #Separar las variables en entrenamiento y test
        X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)
        #Crear el modelo
        model = MLPRegressor(hidden_layer_sizes=(8, 4, 8),activation='relu',solver='adam',max_iter=200,random_state=42)
        #Entrenar modelo
        model.fit(X_train, X_train)
        #Realizar la prediccion con X_test
        X_pred = model.predict(X_test)
        mse = np.mean(np.power(X_test - X_pred, 2), axis=1)
        # Lindar para la deteccion de anomalias
        threshold = np.percentile(mse, 95)
        y_pred = ["Normal" if err < threshold else "Anomaly" for err in mse]
        y_true = ["Normal"] * len(y_pred)
        #Mostrar la classificacion
        print(classification_report(y_true, y_pred))
        return model
