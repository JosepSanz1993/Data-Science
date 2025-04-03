import pandas as pd
class file:
    def __init__(self,csv):
        self.__csv = csv

    def open(self):
        return pd.read_csv(self.__csv)
    
    def move_folder(self,df,path):
        df.to_csv(path)

    def set_csv(self,csv):
        self.__csv = csv

    def get_csv(self):
        return self.__csv