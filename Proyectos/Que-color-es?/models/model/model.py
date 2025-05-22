from abc import ABCMeta,abstractmethod
import polars as pl
import joblib
import os
class model_train(metaclass=ABCMeta):
    def load_data(self,input_data):
        return pl.read_json(input_data)
    
    def save_model(self,model,output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        joblib.dump(model, output_path)
        print(f"Modelo desado en: {output_path}")

    @abstractmethod
    def train_model(self):
        pass

   