from scripts.var_constant import *
from scripts.simulate_data import simulate
from scripts.processed_data import processed
from models.Insolation_Forest.Insolation_model import Insolation
from models.Autoencoders.Auto import Auto
from models.Random_Forest.random_model import Random_F
from models.MLP.mlp import MLP
from bd.mongo_db import MongoDB
from utils.auto_docu import AutoencoderResultDocument
from utils.insolation_forest_docu import IsolationForestResultDocument
from utils.mlp_doc import MLPResultDocument
from utils.random_forest_docu import RandomForestResultDocument
from utils.dash.windows import TimeIntervalWindow
import os

#librerias
sim = simulate()
pro = processed()
In = Insolation(OUTPUT_PATH_PROCESSED)
A = Auto(OUTPUT_PATH_PROCESSED)
RF = Random_F(OUTPUT_PATH_PROCESSED)
mlp = MLP(OUTPUT_PATH_PROCESSED)
iso_doc = IsolationForestResultDocument()
mlp_doc = MLPResultDocument()
rand_doc = RandomForestResultDocument()
mongo = MongoDB(MONGO_DB_URI, MONGO_DB_NAME)
window = TimeIntervalWindow()

if __name__ == "__main__":

    #input Data
    second, interval = window.get_inputs()
    
    #Simulamos los datos
    sim.simulate_data(second,interval)

    #Processamiento de datos
    df = pro.data_load(OUTPUT_PATH_SIMULATED)
    df = pro.preprocess_data(df)
    pro.save_processed_data(df,OUTPUT_PATH_PROCESSED)

    #Conexión a la base de datos
    mongo.connect()

    #Modelo Autoencoders
    modelo,y_test,y_pred, parameters,mse = A.train_model()
    A.save_model(modelo,AUTOENCODER_MODEL_RESULT)
    auto_docu = AutoencoderResultDocument(mse)
    docu = auto_docu.generate(modelo, y_test, y_pred, parameters, AUTOENCODER_MODEL_RESULT, None)
    mongo.insert_data("autoencoder_results", docu)

    #Modelo insolation
    modelo,y_test,y_pred,parameters = In.train_model()
    In.save_model(modelo,INSOLATION_MODEL_RESULT)
    docu = iso_doc.generate(modelo, y_test, y_pred, parameters, INSOLATION_MODEL_RESULT, None)
    mongo.insert_data("isolation_forest_results", docu)

    #Modelo Random Forest
    modelo,y_test,y_pred,parameters = RF.train_model()
    RF.save_model(modelo,RANDOM_FOREST_MODEL_RESULT)
    docu = rand_doc.generate(modelo, y_test, y_pred, parameters, RANDOM_FOREST_MODEL_RESULT, SCALER_RANDOM_FOREST_RESULT)
    mongo.insert_data("random_forest_results", docu)

    #Modelo MLP
    modelo,y_test,y_pred,parameters = mlp.train_model()
    mlp.save_model(modelo,MLP_MODEL_RESULT)
    docu = mlp_doc.generate(modelo, y_test, y_pred, parameters, MLP_MODEL_RESULT,SCALER_MLP_RESULT)
    mongo.insert_data("mlp_results", docu)

    #Cerramos la conexión a la base de datos
    mongo.close()

    #Iniciamos la app ejecutando el script de la app
    os.system("streamlit run mean.py")
    
    #Abrimos connexion en mongo
    mongo.connect()

    #Eliminamos connexiones
    mongo.delete_all_data("autoencoder_results")
    mongo.delete_all_data("isolation_forest_results")
    mongo.delete_all_data("random_forest_results")
    mongo.delete_all_data("mlp_results")

    #Cerramos el mongo
    mongo.close()
