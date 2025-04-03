from transformationinterface import TransformationInterface
from file.work_file import file, pd
class tranform(TransformationInterface):
    def __init__(self, csv):
        self.__f = file(csv)
        self.__d = self.__f.open()
    def change_to_datatime(self,name):
        self.__d[name] = pd.to_datetime(self.__d[name])
    def round_to_hours(self,name):
          df = self.__d[name] = pd.to_datetime(self.__d[name])
          df[name] = df[name].round('H')
    def calculate_to_auxiliar(self,name):
         self.__d['hora'] = self.__d[name].dt.hour
         self.__d['dia_setmana'] = self.__d[name].dt.day_name()
         self.__d['mes'] = self.__d[name].dt.month
    def move_to_folder(self,df,path):
         self.__f.move_folder(df,path)

