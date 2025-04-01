from abc import ABCMeta, abstractmethod
class ExtractionInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_values(self,url,headers,timeout):
        pass
