from abc import ABCMeta, abstractmethod
class ExtractionInterface(metaclass=ABCMeta):
    @abstractmethod
    def get_valuesEosis(self):
        pass
    @abstractmethod
    def get_valuesAemet(self):
        pass
