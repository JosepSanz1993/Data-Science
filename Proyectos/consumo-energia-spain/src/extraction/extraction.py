import pandas as pd
import requests
from extraction.constant_API import *
from extraction.extractioninterface import ExtractionInterface
class extraction(ExtractionInterface):
   def get_valuesEOSIS(self,path):
      df = pd.read_csv(path)
      return df


   def get_valuesAEMET(self,start,final,result):
      aemet = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{start}T00:00:00UTC/fechafin/{final}T23:59:59UTC/todasestaciones/"
      res = requests.get(aemet, params=PARAMS_AEMET,timeout=20)
      data = res.json()
      if 'datos' in data:
         data = requests.get(data['datos'])
         data = data.json()
         result.extend(data)
      return result
