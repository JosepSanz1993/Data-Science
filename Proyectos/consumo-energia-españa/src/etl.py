from extraction.extraction import extraction
from datetime import date, timedelta
from extraction.extraction import pd
class ETL:
    def __init__(self):
        self.__datelist = self.__date_list()
        self.__extract = extraction()
    def __date_list(self):
        i = date(2023,1,1)
        f = date(2023,12,31)
        delta = timedelta(days=14)
        dates = []
        while i <= f:
            dates.append(i.strftime("%Y-%m-%d"))
            i += delta
        return dates
    def get_df_temp(self):
        d_list = self.__date_list()
        i = 0
        list_temp = []
        while i< len(self.date_list()):
            if self.__date_list[i] != "2023-12-31":
                data = self.__extract.get_valuesAEMET(d_list[i],d_list[i+1])
                list_temp.append(data)
                i+=1
        return pd.DataFrame(list_temp)
    
    def get_csv_temp(self,df,name):
        df.to_csv(f"data/raw/{name}")
