from transformation.transformationinterface import TransformationInterface
import pandas as pd
from extraction.constant_API import dias_esp, meses_es
class Transform(TransformationInterface):
    def load_data(self, file_path: str) -> pd.DataFrame:
        return pd.read_csv(file_path)
    
    def preprocess_dates(self, df: pd.DataFrame) -> pd.DataFrame:
        df['fecha'] = pd.to_datetime(df['fecha'])
        df['fecha'] = df['fecha'].dt.round('h')
        df['hora'] = df['fecha'].dt.hour
        df['día de la semana'] = df['fecha'].dt.day_name().map(dias_esp)
        df['mes'] = df['fecha'].dt.month.map(meses_es)
        return df

    def merge_datasets(self, df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        merged_df = pd.merge(df1, df2, on=['fecha', 'provincia'], how='inner')
        return merged_df

    def save_data(self, df: pd.DataFrame, file_path: str) -> None:
        df.to_csv(file_path, index=False)
