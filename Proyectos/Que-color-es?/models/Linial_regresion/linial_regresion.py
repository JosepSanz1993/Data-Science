from models.model.model import model_train
import numpy as np
from sklearn.linear_model import LinearRegression
from scripts.global_var import *

class l_regresion(model_train):
    def __init__(self):
        self.data = self.load_data(DATA_PROCESSED)

    def train_model(self):
      pass

l = l_regresion()
