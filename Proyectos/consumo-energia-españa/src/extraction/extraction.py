import pandas as pd
import requests
from extraction.constant_API import *
from extraction.extractioninterface import ExtractionInterface
class extraction(ExtractionInterface):
   def get_valuesEOSIS(self):
      res = requests.get(URL_ESIOS, headers=Headers_ESIOS)
      data = res.json()
      df = pd.DataFrame(data['indicator']['values'])
      return df

   def get_valuesAEMET(self,start,final):
      aemet = f"https://opendata.aemet.es/opendata/api/valores/climatologicos/diarios/datos/fechaini/{start}T00:00:00UTC/fechafin/{final}T23:59:59UTC/todasestaciones/"
      res = requests.get(aemet, params=PARAMS_AEMET)
      data = res.json()
      if 'datos' in data:
         data = requests.get(data['datos'])
         data = data.json()
      return data