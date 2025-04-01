import requests
import json
import pandas as pd
from datetime import datetime
from src.extraction.extractioninterface import extractioninterface
from src.extraction.constant import HEADERS, ESIOSREQUEST, URL_AEMET

class extraction(extractioninterface):
    def get_valuesEosis(self):
        return requests.get(ESIOSREQUEST, headers=HEADERS)
    def get_valuesAemet(self):
        return requests.get(URL_AEMET)
    

        
