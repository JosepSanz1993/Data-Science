#Classe principal del proyecto
# Importar las librerías y path necesarias
from etl import date,ETL
from transformation.transformation import tranform
init = date(2023,1,1)
final = date(2023,12,31)
days = 14
path_aemet = "data/raw/Aemet_2023.csv"
#Importar las instancias de clase
etl = ETL(init,final,days)
trans = tranform(path_aemet)
#crear un csv con los datos de la api AEMET
#etl.get_df_temp().to_csv("data/raw/Aemet_2023.csv")
#Transformaciones del csv de Aemet


