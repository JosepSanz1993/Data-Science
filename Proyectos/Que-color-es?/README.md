# ¿Qué color es?

Este proyecto tiene como objetivo desarrollar un sistema de clasificación automática de colores utilizando algoritmos de aprendizaje automático. La aplicación permite entrenar modelos y predecir colores a partir de datos procesados.

## 📁 Estructura del proyecto

Que-color-es?/
│
├── main.py # Script principal para ejecución de la aplicación
├── requirements.txt # Dependencias necesarias
├── .gitignore # Archivos y carpetas ignoradas por Git
│
├── models/ # Contiene los modelos de machine learning implementados
│ ├── mlp.py # Perceptrón multicapa
│ ├── svm.py # Máquinas de vectores de soporte
│ ├── kmeans.py # Algoritmo de clustering K-means
│ ├── random_forest.py # Bosques aleatorios
│ ├── insolation_forest.py # Isolation Forest (detección de anomalías)
│ └── trainmodel.py # Script para entrenamiento de modelos
│
├── scripts/ # Scripts auxiliares
│ ├── etl.py # Proceso de extracción, transformación y carga de datos
│ └── global_var.py # Variables globales utilizadas por el proyecto
│
├── data/ # Datos utilizados por el proyecto
│ ├── raw/ # Datos en bruto
│ └── processed/ # Datos procesados
│
└── README.md

## 🚀 Requisitos

Instala los paquetes necesarios con:

```bash
pip install -r requirements.txt

Modelos disponibles-->MLP (Perceptrón multicapa)
                   -->SVM (Support Vector Machine)
                   -->Random Forest
                   -->K-Means
                   -->Isolation Forest
                   
📊 Datos-->Los datos se encuentran en la carpeta data/, separados en raw/ (datos originales) y processed/ (tras ETL).

Ejecutar proyecto--> Sin el insolation en terminal Python main.py
                 --> Con Insolation en terminal Python main --detect-anomalies. 
