from extraction.extraction import extraction
from datetime import date, timedelta
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
        d_list = self.__datelist
        list_temp = []
        for i in range(len(d_list)-1):
            data = self.__extract.get_valuesAEMET(d_list[i],d_list[i+1])
            list_temp.append(data)
        return pd.DataFrame(list_temp).sample(5)
    
    def get_csv_temp(self,df,name):
        df.to_csv(f"data/raw/{name}")
