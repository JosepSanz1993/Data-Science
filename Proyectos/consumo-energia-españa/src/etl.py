from extraction.extraction import extraction,pd
from datetime import date, timedelta
from transformation.transformation import Transform
class ETL:
    def __init__(self,date,path):
        if date is not None:
            self.__datelist = self.__date_list(date[0],date[1],date[2])
        self.__extract = extraction()
        self.__path = path
        self.__transform = Transform()

    def __date_list(self, ini, final,days):
        delta = timedelta(days=days)
        dates = []
        while ini <= final:
            dates.append(ini.strftime("%Y-%m-%d"))
            ini += delta
        return dates
    
    def get_df_esios(self,drop_column):
        df = self.__extract.get_valuesEOSIS(self.__path)
        df = df.drop(columns=drop_column)
        return df
    
    def get_df_temp(self,values):
        d_list = self.__datelist
        list_temp = []
        for i in range(len(d_list)-1):
            data = self.__extract.get_valuesAEMET(d_list[i],d_list[i+1],list_temp)
        return pd.DataFrame(list(map(lambda x:{key : x.get(key) for key in values},data)))
    
    def set_path(self,path):
        self.__path = path
        
    def get_transform(self):
        df = self.__transform.load_data(self.__path)
        df = self.__transform.preprocess_dates(df)
        return df
    

