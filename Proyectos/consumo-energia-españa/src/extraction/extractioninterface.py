from abc import ABC, abstractmethod
class ExtractionInterface(ABC):
    @abstractmethod
    def get_valuesEOSIS(self):
        pass
    @abstractmethod
    def get_valuesAEMET(self,start,final):
        pass
   