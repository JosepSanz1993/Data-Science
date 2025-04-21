from scripts.var_constant import *
from scripts.simulate_data import simulate
from scripts.processed_data import processed
from models.Insolation_Forest.Insolation_model import Insolation
from models.Autoencoders.Auto import Auto
from models.Random_Forest.random_model import Random_F
from models.MLP.mlp import MLP
from models.SVM.svm import SVM
from bd.mongo_db import MongoDB

#librerias
sim = simulate()
pro = processed()
In = Insolation(OUTPUT_PATH_PROCESSED)
A = Auto(OUTPUT_PATH_PROCESSED)
RF = Random_F(OUTPUT_PATH_PROCESSED)
mlp = MLP(OUTPUT_PATH_PROCESSED)
svm = SVM(OUTPUT_PATH_PROCESSED)
mongo = MongoDB(MONGO_DB_URI, MONGO_DB_NAME)

if __name__ == "__main__":
    #Simulamos los datos
    sim.simulate_data()

    #Processamiento de datos
    df = pro.data_load(OUTPUT_PATH_SIMULATED)
    df = pro.preprocess_data(df)
    pro.save_processed_data(df,OUTPUT_PATH_PROCESSED)

    #Modelo Autoencoders
    modelo = A.train_model()
    A.save_model(modelo,AUTOENCODER_MODEL_RESULT)

    #Modelo insolation
    modelo = In.train_model()
    In.save_model(modelo,INSOLATION_MODEL_RESULT)

    #Modelo Random Forest
    modelo = RF.train_model()
    RF.save_model(modelo,RANDOM_FOREST_MODEL_RESULT)

    #Modelo MLP
    modelo = mlp.train_model()
    mlp.save_model(modelo,MLP_MODEL_RESULT)
    
    #Modelo SVM
    modelo = svm.train_model()
    svm.save_model(modelo,SVM_MODEL_RESULT)