from abc import ABCMeta,abstractmethod
import polars as pl
import joblib
from scripts.global_var import SAVE_MODEL
class model_train(metaclass=ABCMeta):
    def load_data(self,input_data):
        return pl.read_json(input_data)
    
    @abstractmethod
    def train_model(self,colum,target_column):
        pass

    def save_model(self,model,name):
        joblib.dump(model,SAVE_MODEL+name)

    def save_scaler(self,scaler,name):
        joblib.dump(scaler,SAVE_MODEL+name)

    def save_encoder(self,encoder,name):
        joblib.dump(encoder,SAVE_MODEL+name)

