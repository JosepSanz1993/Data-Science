import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.preprocessing import MinMaxScaler
from models.model.model import model_train
from scripts.var_constant import SCALER_RANDOM_FOREST_RESULT

class Random_F(model_train):
    def __init__(self,input_data):
        self.__df = self.load_data(input_data)

    def train_model(self):
        #Preprosesamianto de datos
        features = self.__df.select([
        "cpu_usage", "ram_usage", "disk_usage", "temperature", "network_latency"]).to_numpy()
        labels = self.__df["anomaly"].to_numpy()
        X = features
        y = labels
        scaler = MinMaxScaler()
        X_scaled = scaler.fit_transform(X)
        joblib.dump(scaler, SCALER_RANDOM_FOREST_RESULT)
        
        #Entrar modelo con Random Forest
        X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        #Realizar Predicciones
        y_pred = model.predict(X_test)

        #Mostrar resultados
        print(confusion_matrix(y_test, y_pred))
        print(classification_report(y_test, y_pred))

        return model

