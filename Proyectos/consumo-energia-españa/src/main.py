#Classe principal del proyecto
# Importar las librerías y path necesarias
from etl import date,ETL
from transformation.transformation import Transform
init = date(2023,1,1)
final = date(2023,12,31)
days = 14
path_aemet = "data/raw/Aemet_2023.csv"
path_Esios = "data/raw/Aemet_2023.csv"

#Importar las instancias de clase
etl = ETL(init,final,days)
trans_Aemet = Transform(path_aemet)
trans_Esios = Transform(path_aemet)

#crear un csv con los datos de la api AEMET
#etl.get_df_temp().to_csv("data/raw/Aemet_2023.csv")

#crear un csv para los datos de Esios
#etl.get_df_esios('offer_indicators','2023-01-01','2023-12-31').to_csv("data/raw/ESIOS_2023.csv")

#Transformaciones del csv de Aemet
#trans_Aemet.change_to_datetime("fecha")
#trans_Aemet.round_to_hours("fecha")
#trans_Aemet.calculate_auxiliary_columns("fecha")
#trans_Aemet.save_to_folder("data/processed/energia_temp.csv")
