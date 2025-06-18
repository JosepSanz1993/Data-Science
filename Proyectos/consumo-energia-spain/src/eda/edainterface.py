from abc import ABC, abstractmethod

class ConsumoInterface(ABC):
    
    @abstractmethod
    def data_load(self, filepath: str):
        pass
    
    @abstractmethod
    def hourly_distribution(self):
        pass
    
    @abstractmethod
    def comparative_type(self):
        pass
    
    @abstractmethod
    def consumption_by_region(self):
        pass
    
    @abstractmethod
    def evolucion_mensual(self):
        pass