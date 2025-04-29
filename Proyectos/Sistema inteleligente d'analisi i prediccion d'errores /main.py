from scripts.var_constant import *
from scripts.simulate_data import simulate
from scripts.processed_data import processed
from models.Insolation_Forest.Insolation_model import Insolation
from models.Autoencoders.Auto import Auto
from models.Random_Forest.random_model import Random_F
from models.MLP.mlp import MLP
from models.SVM.svm import SVM
from bd.mongo_db import MongoDB
from utils.auto_docu import AutoencoderResultDocument
from utils.insolation_forest_docu import IsolationForestResultDocument
from utils.mlp_doc import MLPResultDocument
from utils.svm_docu import SVMResultDocument
from utils.random_forest_docu import RandomForestResultDocument

#librerias
sim = simulate()
pro = processed()
In = Insolation(OUTPUT_PATH_PROCESSED)
A = Auto(OUTPUT_PATH_PROCESSED)
RF = Random_F(OUTPUT_PATH_PROCESSED)
mlp = MLP(OUTPUT_PATH_PROCESSED)
svm = SVM(OUTPUT_PATH_PROCESSED)
iso_doc = IsolationForestResultDocument()
mlp_doc = MLPResultDocument()
svm_doc = SVMResultDocument()
rand_doc = RandomForestResultDocument()
mongo = MongoDB(MONGO_DB_URI, MONGO_DB_NAME)

if __name__ == "__main__":
    #Simulamos los datos
    #sim.simulate_data()

    #Processamiento de datos
    #df = pro.data_load(OUTPUT_PATH_SIMULATED)
    #df = pro.preprocess_data(df)
    #pro.save_processed_data(df,OUTPUT_PATH_PROCESSED)

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

    #Modelo SVM
    modelo,y_test,y_pred,parameters = svm.train_model()
    svm.save_model(modelo,SVM_MODEL_RESULT)
    docu = svm_doc.generate(modelo, y_test, y_pred,parameters, SVM_MODEL_RESULT, SCALER_SVM_RESULT)
    mongo.insert_data("svm_results", docu)

    #Cerramos la conexión a la base de datos
    mongo.client.close()