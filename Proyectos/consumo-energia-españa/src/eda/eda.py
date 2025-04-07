import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from edainterface import edainterface
class AnalisisConsumo(edainterface):
    
    def __init__(self):
        self.df = None
        
    def cargar_datos(self, filepath: str):
        self.df = pd.read_csv(filepath, parse_dates=['fecha'])
        if 'hora' not in self.df.columns:
            self.df['hora'] = self.df['fecha'].dt.hour
        if 'día de la semana' not in self.df.columns:
            self.df['día de la semana'] = self.df['fecha'].dt.dayofweek
        if 'tipo_dia' not in self.df.columns:
            self.df['tipo_dia'] = self.df['día de la semana'].apply(lambda x: 'Fin de setmana' if x >= 5 else 'Laborable')
        if 'año_mes' not in self.df.columns:
            self.df['año_mes'] = self.df['fecha'].dt.to_period('M')
    
    def distribucion_por_hora(self):
        consumo_horario = self.df.groupby('hora')['consumo'].mean()
        plt.figure(figsize=(10, 5))
        plt.plot(consumo_horario.index, consumo_horario.values, marker='o')
        plt.title("Distribución horaria del consumo eléctrico")
        plt.xlabel("Hora del día")
        plt.ylabel("Consumo medio")
        plt.grid(True)
        plt.show()
    
    def comparativa_dia_tipo(self):
        consumo_diario = self.df.groupby(['fecha', 'tipo_dia'])['consumo'].sum().reset_index()
        plt.figure(figsize=(6, 5))
        sns.boxplot(data=consumo_diario, x='tipo_dia', y='consumo')
        plt.title("Consumo diario: laborables vs fines de semana")
        plt.show()
    
    def consumo_por_region(self):
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