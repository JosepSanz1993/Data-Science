from abc import ABCMeta, abstractmethod
class ExtractionInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_valuesEOSIS(self,url,headers,params,timeout):
        pass
    @abstractmethod
    def get_valuesAEMET(self,url,params,timeout):
        pass
    @abstractmethod
    def __get_dataframeEOSIS(self,response):
        pass
    @abstractmethod
    def __get_dataframeAEMET(self,response):
        pass
    @abstractmethod
    def __move_dataframe(self,dataframe,name_file):
        pass
    @abstractmethod
    def __is_connection_enabled(self,response):
        pass
