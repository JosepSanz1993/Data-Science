import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from eda.edainterface import ConsumoInterface
from extraction.constant_API import dia_semana_num
class AnalisisConsumo(ConsumoInterface):
    
    def __init__(self):
        self.df = None
        
    def data_load(self, filepath: str):
        self.df = pd.read_csv(filepath, parse_dates=['fecha'])
        if 'hora' not in self.df.columns:
            self.df['hora'] = self.df['fecha'].dt.hour
        if 'día de la semana' not in self.df.columns:
            self.df['día de la semana'] = self.df['fecha'].dt.dayofweek
        if 'tipo_dia' not in self.df.columns:
            self.df['día de la semana (int)'] = self.df['día de la semana'].map(dia_semana_num)
            self.df['tipo_dia'] = self.df['día de la semana (int)'].apply(lambda x: 'Fin de setmana' if x >= 5 else 'Laborable')
        if 'año_mes' not in self.df.columns:
            self.df['año_mes'] = self.df['fecha'].dt.to_period('M')
    
    def hourly_distribution(self):
        consumo_horario = self.df.groupby('hora')['consumo'].mean()
        print(consumo_horario)
        plt.figure(figsize=(10, 5))
        plt.plot(consumo_horario.index, consumo_horario.values, marker='o')
        plt.title("Distribución horaria del consumo eléctrico")
        plt.xlabel("Hora del día")
        plt.ylabel("Consumo medio")
        plt.grid(True)
        plt.show()
    
    def comparative_type(self):
        consumo_diario = self.df.groupby(['fecha', 'tipo_dia'])['consumo'].sum().reset_index()
        plt.figure(figsize=(6, 5))
        sns.boxplot(data=consumo_diario, x='tipo_dia', y='consumo')
        plt.title("Consumo diario: laborables vs fines de semana")
        plt.show()
    
    def consumption_by_region(self):
        if 'provincia' in self.df.columns:
            consumo_region = self.df.groupby('provincia')['consumo'].mean().sort_values(ascending=False)
            plt.figure(figsize=(12, 6))
            consumo_region.plot(kind='bar')
            plt.title("Consumo medio por provincia")
            plt.ylabel("Consumo medio")
            plt.xticks(rotation=45)
            plt.show()
    
    def evolucion_mensual(self):
        consumo_mensual = self.df.groupby('mes')['consumo'].sum()
        plt.figure(figsize=(10, 5))
        consumo_mensual.plot(marker='o')
        plt.title("Evolución mensual del consumo eléctrico")
        plt.xlabel("Mes")
        plt.ylabel("Consumo total")
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.show()