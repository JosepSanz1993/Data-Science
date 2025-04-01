from abc import ABCMeta, abstractmethod
class TransformationInterface(metaclass=ABCMeta):
    @abstractmethod
    def change_to_datatime(self,file):
        pass
    @abstractmethod
    def round_to_hours(self,file):
        pass
    @abstractmethod
    def calculate_to_auxiliar(self,file):
        pass
    @abstractmethod
    def join_dataset_for_date_and_region(self,file):
        pass
    @abstractmethod
    def move_to_folder(self,file,folder):
        pass