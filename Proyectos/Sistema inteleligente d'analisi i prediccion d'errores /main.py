from scripts.var_constant import *
from scripts.simulate_data import simulate
from scripts.processed_data import processed

#llibrerias
sim = simulate()
pro = processed()

if __name__ == "__main__":
    #Simulamos los datos
    #sim.simulate_data()
    #Processamiento de datos
    df = pro.data_load(OUTPUT_PATH_SIMULATED)
    df = pro.preprocess_data(df)
    pro.save_processed_data(df,OUTPUT_PATH_PROCESSED)
