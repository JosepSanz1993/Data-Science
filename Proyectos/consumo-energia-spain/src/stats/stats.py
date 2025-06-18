from stats.statsinterface import AnalisisDatos
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from scipy import stats
class AnalisisConsumoTemperatura(AnalisisDatos):
    
    def __init__(self, path_csv):
        self.df = pd.read_csv(path_csv)
        self.df.dropna(inplace=True)
    
    def calculate_consumption_statistics(self):
        consumo_promedio = self.df['consumo'].mean()
        consumo_desviacion = self.df['consumo'].std()
        consumo_minimo = self.df['consumo'].min()
        consumo_maximo = self.df['consumo'].max()

        return {
            "Promedio": consumo_promedio,
            "Desviación estándar": consumo_desviacion,
            "Mínimo": consumo_minimo,
            "Máximo": consumo_maximo
        }

    def calculate_correlation(self):
        X = self.df[['tmed']]  
        y = self.df['consumo']  

        modelo = LinearRegression()
        modelo.fit(X, y)
        y_pred = modelo.predict(X)

        r2 = modelo.score(X, y)
        return r2

    def fit_linear_regression(self):
        X = self.df[['tmed']] 
        y = self.df['consumo'] 

        modelo = LinearRegression()
        modelo.fit(X, y)
        pendiente = modelo.coef_[0]
        intercepto = modelo.intercept_

        y_pred = modelo.predict(X)
        r2 = modelo.score(X, y)
        
        p_valor = stats.pearsonr(self.df['tmed'], self.df['consumo'])

        return {
            "Pendiente": pendiente,
            "Intercepto": intercepto,
            "R²": r2,
            "p-valor": p_valor
        }