from abc import ABC, abstractmethod
class AnalisisDatos(ABC):
    @abstractmethod
    def calculate_consumption_statistics(self):
        pass

    @abstractmethod
    def calculate_correlation(self):
        pass

    @abstractmethod
    def fit_linear_regression(self):
        pass