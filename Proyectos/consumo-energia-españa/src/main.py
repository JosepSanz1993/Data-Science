#Classe principal del proyecto
# Importar las librerías y path necesarias
from etl import date,ETL
import pandas as pd
from extraction.constant_API import *
init = date(2023,1,1)
final = date(2023,12,31)
days = 14
path_aemet = "data/raw/Aemet_2023.csv"
path_esios = "data/raw/Esios_2023.csv"
path_pre_esios = "data/preprocessed/Esios_2023_pre.csv"
values = ["fecha","tmed","provincia"]

# Crear una instancia de la clase ETL
Etl_Esios = ETL(None,path_esios)
Etl_Aemet = ETL((init,final,days),path_aemet)

# Extraer los datos de la API ESIOS
df = Etl_Esios.get_df_esios("Valor (€/kWh)")

#transformar los datos
df.dropna(inplace=True)
df.columns = df.columns.str.lower()
df['fecha'] = df['fecha']+ ' ' + df['hora']
df.drop(columns='hora', inplace=True)
df.rename(columns={"consumo por hora (kwh)": "consumo"}, inplace=True)
Etl_Esios.save_data(df, path_esios)
Etl_Esios.set_path(path_pre_esios)
Esios_df = Etl_Esios.get_transform()

#crear un csv con los datos de la api AEMET
df = Etl_Aemet.get_df_temp(values)
Etl_Aemet.save_data(df, path_aemet)
df.dropna(inplace=True)
df['tmed'] = df['tmed'].apply(lambda x: float(x.replace(',','.')))
df = df.groupby(['provincia','fecha']).agg({'tmed': 'mean'})
df.reset_index(inplace=True)
df.rename(columns={"tmed":"temp_media"})
Aemet_df = Etl_Aemet.get_transform()

#Juntamos los dos dataframes
Etl_Esios.merge_datasets(Esios_df, Aemet_df)
Etl_Esios.save_data(Esios_df, "data/merged/merged_data.csv")

