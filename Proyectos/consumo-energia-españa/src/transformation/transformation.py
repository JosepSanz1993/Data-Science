from transformation.transformationinterface import TransformationInterface
import pandas as pd
import os
class Transform(TransformationInterface):
    def __init__(self, csv_path):
        self.__df = pd.read_csv(csv_path)
        self.__csv_path = csv_path 

    def change_to_datetime(self, column_name):
        self.__df[column_name] = pd.to_datetime(self.__df[column_name])

    def round_to_hours(self, column_name):
        self.__df[column_name] = self.__df[column_name].dt.round('H')

    def calculate_auxiliary_columns(self, column_name):
        self.__df['hora'] = self.__df[column_name].dt.hour
        self.__df['dia_setmana'] = self.__df[column_name].dt.day_name()
        self.__df['mes'] = self.__df[column_name].dt.month

    def merge_with(self, other_csv, on_columns=None, how='outer'):
        if on_columns is None:
            on_columns = ['fecha', 'region']
        
        other_df = pd.read_csv(other_csv)
        other_df[on_columns[0]] = pd.to_datetime(other_df[on_columns[0]]) 
        self.__df = pd.merge(self.__df, other_df, on=on_columns, how=how)

    def save_to_folder(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.__df.to_csv(path, index=False)

    def __str__(self):
        return str(self.__df.head())  