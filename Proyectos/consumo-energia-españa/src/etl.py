from extraction.extraction import extraction
from datetime import date, timedelta
import polars as pl
from extraction.extraction import pd
class ETL:
    def __init__(self,ini,final,days):
        self.__datelist = self.__date_list(ini,final,days)
        self.__extract = extraction()

    def __date_list(self, ini, final,days):
        delta = timedelta(days=days)
        dates = []
        while ini <= final:
            dates.append(ini.strftime("%Y-%m-%d"))
            ini += delta
        return dates
    
    def get_df_temp(self):
        values = ["fecha","tmed","provincia"]
        d_list = self.__datelist
        list_temp = []
        for i in range(len(d_list)-1):
            data = self.__extract.get_valuesAEMET(d_list[i],d_list[i+1],list_temp)
        return pd.DataFrame(list(map(lambda x:{key : x.get(key) for key in values},data)))
    
