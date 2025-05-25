from abc import ABCMeta,abstractmethod
import polars as pl
class model_train(metaclass=ABCMeta):
    def load_data(self,input_data):
        return pl.read_json(input_data)
    @abstractmethod
    def train_model(self,colum):
        pass
   