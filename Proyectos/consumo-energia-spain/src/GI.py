import tkinter as tk
from tkinter import filedialog, messagebox
from stats.stats import AnalisisConsumoTemperatura
class GraphicInterface:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Análisis de Consumo y Temperatura")
        self.win.geometry("600x400")

        # Botón y etiqueta
        self.create_button()
        self.etiqueta_resultado = tk.Label(self.win, text="Resultados de la estadística", justify=tk.LEFT, anchor="w")
        self.etiqueta_resultado.pack(pady=10, fill='both', expand=True)

    def load_data(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            try:
                analisis = AnalisisConsumoTemperatura(filepath)
                estadisticas = analisis.calculate_consumption_statistics()
                regresion = analisis.fit_linear_regression()
                correlacion = analisis.calculate_correlation()

                resultado = "\n".join([
                    "--- Estadísticas de Consumo ---",
                    *(f"{k}: {v:.2f}" for k, v in estadisticas.items()),
                    "",
                    "--- Regresión Lineal ---",
                    *(f"{k}: {v:.4f}" if isinstance(v, float) else f"{k}: {v}" for k, v in regresion.items()),
                    "",
                    f"--- Correlación (R²) ---\nR² calculado: {correlacion:.4f}"
                ])
                self.etiqueta_resultado.config(text=resultado)
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo analizar el archivo.\n{e}")
    
    def create_button(self):
        button = tk.Button(self.win, text="Cargar CSV", command=self.load_data)
        button.pack(pady=10)

    def show(self):
        self.win.mainloop()
