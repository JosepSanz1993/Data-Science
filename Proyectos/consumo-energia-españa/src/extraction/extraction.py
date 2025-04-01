import requests
import json
import pandas as pd
from datetime import datetime
from src.extraction.extractioninterface import extractioninterface
from src.extraction.constant import HEADERS, ESIOSREQUEST, URL_AEMET

class extraction(extractioninterface):
    def get_valuesEosis(self):
        try:
            response = requests.get(ESIOSREQUEST, headers=HEADERS)
            if response.status_code == 200:
                data = response.json()
                # Convert the JSON data to a pandas DataFrame
                df = pd.DataFrame(data)
                # Save the DataFrame to a CSV file
                df.to_csv('consumo-energia-españa/src/extraction/esios.csv', index=False)
            else:
                print(f"Error: {response.status_code}")
            print("Data extraction completed successfully.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
    def get_valuesAemet(self):
        try:
            response = requests.get(URL_AEMET)
            if response.status_code == 200:
                data = response.json()
                if "datos" in data:
                    data_url = data["datos"]
                    data_response = requests.get(data_url)
                    if data_response.status_code == 200:
                        data_json = data_response.json()
                        # Convert the JSON data to a pandas DataFrame
                        df = pd.DataFrame(data_json)
                        # Save the DataFrame to a CSV file
                        df.to_csv('consumo-energia-españa/src/extraction/aemet.csv', index=False)
                    else:
                        print(f"Error: {data_response.status_code}")
            else:
                print(f"Error: {response.status_code}")
            print("Data extraction completed successfully.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
        return requests.get(URL_AEMET)
    

        
