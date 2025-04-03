from abc import ABC, abstractmethod
class ExtractionInterface(ABC):
    @abstractmethod
    def get_valuesEOSIS(self,name,start,end):
        pass
    @abstractmethod
    def get_valuesAEMET(self,start,final,result):
        pass
   