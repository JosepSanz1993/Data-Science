import requests
import pandas as pd
from datetime import datetime
from extractioninterface import ExtractionInterface
class extraction(ExtractionInterface):
   def get_values(self,url,headers,timeout):
      try:
         response = requests.get(url, headers=headers, timeout=timeout)
         if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)
            df.to_csv('consumo-energia-españa/data/raw/data.csv', index=False)
         else:
            print(f"Error: {response.status_code}")
      except requests.exceptions.RequestException as e:
         print(f"Request failed: {e}")
