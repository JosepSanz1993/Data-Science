#Classe principal del proyecto
# Importar las librerías necesarias
from etl import date,ETL
from etl import pd
init = date(2023,1,1)
final = date(2023,12,31)
days = 14
#Importar las instancias de clase
etl = ETL(init,final,days)
#crear un csv con los datos de la api AEMET
etl.get_df_temp().to_csv("data/raw/Aemet_2023.csv")
