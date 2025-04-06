from abc import ABCMeta, abstractmethod
import pandas as pd
class TransformationInterface(metaclass=ABCMeta):
    @abstractmethod
    def load_data(self, file_path: str) -> pd.DataFrame:
        pass

    @abstractmethod
    def preprocess_dates(self, df: pd.DataFrame) -> pd.DataFrame:
        pass
    
    @abstractmethod
    def merge_datasets(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        pass

    @abstractmethod
    def save_data(self, df: pd.DataFrame, file_path: str) -> None:
        pass