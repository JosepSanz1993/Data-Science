from trainmodel import model_train
import numpy as np
from sklearn.linear_model import LinearRegression
class l_regresion(model_train):
    def __init__(self, data):
        self.data = self.load_data(data)

    def train_model(self):
      pass

l = l_regresion("data/raw/color_sensor_data.csv")
