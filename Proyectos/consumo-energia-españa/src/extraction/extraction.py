import pandas as pd
import requests
from extraction.constant_API import *
from extraction.extractioninterface import ExtractionInterface
from esios import ESIOSClient
import os
os.environ['ESIOS_API_KEY'] = TOKEN_ESIOS
class extraction(ExtractionInterface):
   def get_valuesEOSIS(self,name,start,end):
      client = ESIOSClient()
      endpoint = client.endpoint(name=name)
      df = endpoint.list() 
      indicator = endpoint.select(670)
      df = indicator.historical(start=start,end=end)
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
