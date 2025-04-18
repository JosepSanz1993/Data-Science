from scripts.var_constant import *
from scripts.simulate_data import simulate
from scripts.processed_data import processed
from models.Insolation_Forest.Insolation_model import Insolation
#librerias
sim = simulate()
pro = processed()
In = Insolation(OUTPUT_PATH_PROCESSED)
if __name__ == "__main__":
    #Simulamos los datos
    sim.simulate_data()

    #Processamiento de datos
    df = pro.data_load(OUTPUT_PATH_SIMULATED)
    df = pro.preprocess_data(df)
    pro.save_processed_data(df,OUTPUT_PATH_PROCESSED)

    #Modelo insolation
    modelo = In.train_model()
    In.save_model(modelo,INSOLATION_MODEL_RESULT)