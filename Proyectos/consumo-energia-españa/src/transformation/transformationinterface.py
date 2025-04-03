from abc import ABCMeta, abstractmethod
class TransformationInterface(metaclass=ABCMeta):
    @abstractmethod
    def change_to_datatime(self,name):
        pass
    @abstractmethod
    def round_to_hours(self,name):
        pass
    @abstractmethod
    def calculate_to_auxiliar(self,name):
        pass
    @abstractmethod
    def move_to_folder(self,df,path):
        pass
    