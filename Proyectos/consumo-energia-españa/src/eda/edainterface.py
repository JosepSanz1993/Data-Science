from abc import ABC, abstractmethod

class ConsumoInterface(ABC):
    
    @abstractmethod
    def cargar_datos(self, filepath: str):
        pass
    
    @abstractmethod
    def distribucion_por_hora(self):
        pass
    
    @abstractmethod
    def comparativa_dia_tipo(self):
        pass
    
    @abstractmethod
    def consumo_por_region(self):
        pass
    
    @abstractmethod
    def evolucion_mensual(self):
        pass