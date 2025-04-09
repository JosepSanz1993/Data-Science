#Classe principal del proyecto
# Importar las librerías y path necesarias
from etl import date,ETL
import pandas as pd
from extraction.constant_API import *
import numpy as np
from eda.eda import AnalisisConsumo
from GI import GraphicInterface
init = date(2023,1,1)
final = date(2023,12,31)
days = 14
path_aemet = "data/raw/Aemet_2023.csv"
path_esios = "data/raw/Esios_2023.csv"
path_pre_esios = "data/preprocessed/Esios_2023_pre.csv"
path_pre_aemet = "data/preprocessed/Aemet_2023_pre.csv"
path_energy = "data/processed/energia_temp.csv"
values = ["fecha","tmed","provincia"]

# Crear una instancia de las clases
Etl_Esios = ETL(None,path_esios)
Etl_Aemet = ETL((init,final,days),path_aemet)
Analisis = AnalisisConsumo()
GI = GraphicInterface() 

# Extraer los datos de la API ESIOS
df = Etl_Esios.get_df_esios("Valor (€/kWh)")

#transformar los datos
df.dropna(inplace=True)
df.columns = df.columns.str.lower()
df['fecha'] = df['fecha']+ ' ' + df['hora']
df.drop(columns='hora', inplace=True)
df.rename(columns={"consumo por hora (kwh)": "consumo"}, inplace=True) 
Etl_Esios.set_path(path_pre_esios)
Esios_df = Etl_Esios.get_transform()
Etl_Esios.save_data(Esios_df, path_pre_esios)

#crear un csv con los datos de la api AEMET
df = Etl_Aemet.get_df_temp(values)
Etl_Aemet.save_data(df, path_aemet)
df.dropna(inplace=True)
df['tmed'] = df['tmed'].apply(lambda x: float(x.replace(',','.')))
df = df.groupby(['provincia','fecha']).agg({'tmed': 'mean'})
df.reset_index(inplace=True)
df.rename(columns={"tmed":"temp_media"})
Aemet_df = Etl_Aemet.get_transform()
Etl_Aemet.set_path(path_pre_aemet)
Etl_Aemet.save_data(Aemet_df, path_pre_aemet)

# Unir los datos de las dos APIs
Esios_df['fecha'] = pd.to_datetime(Esios_df['fecha']).dt.date
Aemet_df['tmed'] = Aemet_df['tmed'].str.replace(',','.')
Aemet_df['fecha'] = pd.to_datetime(Aemet_df['fecha']).dt.date
df_final = pd.merge(Esios_df, Aemet_df, on=['provincia', 'fecha', 'hora', 'día de la semana', 'mes'], how='outer')
df_final['consumo'] = df_final['consumo'].apply(lambda x: np.random.randint(1000, 3000) if pd.isnull(x) else x)
df_final = df_final.sort_values(by=['provincia','fecha','hora'])
df_final['tmed'] = pd.to_numeric(df_final['tmed'], errors='coerce')
df_final = df_final.dropna(subset=['tmed'])
df_final = df_final.groupby(['fecha','provincia']).agg({'consumo':'sum','tmed':'mean'}).reset_index()
df_final.rename(columns={'consumo':'consumo_total','tmed':'temperatura_media'},inplace=True)
Etl_Esios.set_path(path_energy)
Etl_Esios.save_data(df_final, path_energy)

#Análisis Exploratorio (EDA)
Analisis.data_load(path_esios)
Analisis.hourly_distribution()
Analisis.comparative_type()
Analisis.consumption_by_region()
Analisis.evolucion_mensual()

#Estadística
GI.show()




