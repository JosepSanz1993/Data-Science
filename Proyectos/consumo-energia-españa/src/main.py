#Classe principal del proyecto
# Importar las librerías necesarias
from etl import date,ETL
init = date(2023,1,1)
final = date(2023,12,31)
days = 14
#Importar las instancias de clase
etl = ETL(init,final,days)
print(etl.get_df_temp())
