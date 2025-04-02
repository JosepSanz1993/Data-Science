import requests
import pandas as pd
from extractioninterface import ExtractionInterface
class extraction(ExtractionInterface):
   def __get_dataframeEOSIS(self, response):
      try:
         data = response.json()
         dataframe = pd.DataFrame(data["1001"]["values"])
         dataframe.rename(columns={"value": "demanda_mw"}, inplace=True)
      except ValueError as e:
         print(f"Error parsing JSON: {e}")
         dataframe = None
      return dataframe
   
   def __get_dataframeAEMET(self, response):
      try:
         data = response.json()
         url_data = data.get("datos")
         if url_data:
            response = requests.get(url_data)
            if self.__is_connection_enabled(response):
               dataframe = pd.DataFrame(response.json())
               dataframe = dataframe[["fecha", "provincia", "tmed"]]
               dataframe.rename(columns={"tmed": "temperatura_media"}, inplace=True)
         else:
            print("No URL found in the response.")
      except ValueError as e:
         print(f"Error parsing JSON: {e}")
         dataframe = None
      return dataframe

   def __move_dataframe(self, dataframe,file):
      try:
         dataframe.to_csv(file, index=False)
         print("Dataframe moved to output.csv")
      except Exception as e:
         print(f"Error moving dataframe: {e}")

   def __is_connection_enabled(self, response):
      if response.status_code == 200:
         return True
      else:
         return False
      
   def get_valuesEOSIS(self,url,headers,params,timeout,file):
      try:
         response = requests.get(url, headers=headers, params=params,timeout=timeout)
         if self.__is_connection_enabled(response):
            df = self.__get_dataframeEOSIS(response)
            if df is not None:
               self.__move_dataframe(df,file)
            else:
               print("No data found in the response.")
         else:
            print(f"Error: {response.status_code}")
      except requests.exceptions.RequestException as e:
         print(f"⚠️ Error en la petició: {response.status_code} - {response.text}")
         print(f"Request failed: {e}")
   
   def get_valuesAEMET(self,url,params,timeout,file):
      try:
         response = requests.get(url, params=params,timeout=timeout)
         if self.__is_connection_enabled(response):
            df = self.__get_dataframeAEMET(response)
            if df is not None:
               self.__move_dataframe(df,file)
            else:
               print("No data found in the response.")
         else:
            print(f"Error: {response.status_code}")
      except requests.exceptions.RequestException as e:
         print(f"⚠️ Error en la petició: {response.status_code} - {response.text}")
         print(f"Request failed: {e}")