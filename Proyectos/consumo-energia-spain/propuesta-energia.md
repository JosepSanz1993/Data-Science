# Proyecto: Análisis del Consumo Energético en España

Este proyecto tiene como objetivo un flujo completo de análisis de datos reales, desde su extracción hasta la visualización interactiva, con foco en el consumo energético y su relación con la temperatura ambiental en distintas regiones de España. 

---

## Objetivos

1. **Formular preguntas de investigación relevantes**: 
  
   1. **¿En qué franjas horarias y días de la semana se registra la mayor demanda eléctrica en España?**  
      Analizarás la demanda energética en intervalos horarios y por días, buscando identificar cuándo se produce el mayor consumo y si existen patrones sistemáticos entre días laborables y fines de semana.

   2. **¿Qué comunidades autónomas presentan mayores niveles de consumo eléctrico promedio diario?**  
      Compararás la demanda media entre regiones, observando diferencias geográficas que puedan reflejar condiciones climáticas, densidad poblacional o actividad industrial.

   3. **¿Existe una relación entre la temperatura ambiental y el nivel de consumo eléctrico en las distintas regiones de España?**  
      Combinarás los datos de consumo con los de temperatura, estudiarás su correlación y ajustarás una regresión lineal simple para entender si hay una asociación significativa.

   4. **¿Cuáles son los patrones estacionales del consumo energético en España durante el año?**  
      Analizarás la evolución temporal agregada por meses, para detectar tendencias estacionales como incrementos en verano o invierno.

2. **Extraer y transformar datos desde APIs oficiales**  
   → Descargar datos de consumo eléctrico horario desde REE/ESIOS y de temperatura desde AEMET.  
   → Unificarlos en un solo dataset cruzando por fecha y comunidad autónoma.

3. **Realizar un análisis exploratorio completo (EDA)**  
   → Visualizar distribución de consumo por hora, día y región. Detectar outliers. Analizar diferencias entre días laborables y fines de semana.

4. **Calcular estadísticas descriptivas e inferenciales**  
   → Calcular medidas básicas, correlaciones y ajustar una regresión lineal para estudiar el efecto de la temperatura.

5. **Crear un dashboard interactivo**  
   → Construir visualizaciones en Power BI o Tableau que sigan un hilo narrativo. Incluir gráficos temporales, regionales y explicativos.

6. **Ejecutar el pipeline completo desde un script**  
   → Centralizar todo en `main.py`, para poder lanzar el flujo con un solo comando.

7. **Documentar adecuadamente**  
   → Redactar README completo, con instrucciones, resultados esperados, capturas, gifs y estructura clara del proyecto.


---

## Fuentes de Datos

- **Consumo eléctrico**: REE / ESIOS API → Indicador `1001` de demanda real horaria.
  - Registro y documentación: https://api.esios.ree.es/

- **Temperatura**: AEMET OpenData → Datos de temperatura diaria por provincia.
  - Registro y documentación: https://opendata.aemet.es/

Ambas requieren obtener una clave de acceso.

---

## Estructura del Proyecto

Tu proyecto debe seguir exactamente esta estructura:

```
consumo-energia-espana/
├── data/
│   ├── raw/             # Archivos descargados tal cual
│   └── processed/       # Dataset final unificado
├── notebooks/           # Exploraciones, pruebas y análisis visuales
├── dashboards/          # Archivo final del dashboard (.pbix o .twbx)
├── src/                 # Scripts con funciones reutilizables
│   ├── etl.py
│   ├── eda.py
│   ├── stats.py
│   └── main.py
├── requirements.txt     # Lista de dependencias
├── .gitignore           # Exclusiones
├── README.md            # Este archivo
└── TODO.md              # Lista de tareas a completar
```

---

## Instrucciones de Instalación y Ejecución

1. Clonar el repositorio:
```bash
git clone https://github.com/tu_usuario/consumo-energia-espana.git
cd consumo-energia-espana
```
2. Crear y activar entorno virtual:
```bash
python3 -m venv venv
source venv/bin/activate  # (En Windows: venv\Scripts\activate)
```
3. Instalar dependencias:
```bash
pip install -r requirements.txt
```
4. Ejecutar pipeline completo:
```bash
python src/main.py
```

---

## Flujo del Proyecto

### Paso 1: Extracción de Datos
- Usa el token de ESIOS para obtener la demanda eléctrica por hora del año 2023.
- Usa la clave de AEMET para descargar la temperatura media diaria por provincia para 2023.
- Guarda ambos archivos en `data/raw/`.

### Paso 2: Transformación
- Convierte columnas de fechas a formato datetime.
- Redondea horas si es necesario.
- Calcula columnas auxiliares: `hora`, `día de la semana`, `mes`.
- Une los datasets por fecha y región (si es posible).
- Guarda resultado final en `data/processed/energia_temp.csv`.

### Paso 3: Análisis Exploratorio (EDA)
- Analiza la distribución de consumo por hora (línea)
- Compara consumo entre días laborables y fines de semana (boxplot)
- Evalúa diferencias entre regiones (barplot o mapa si puedes)
- Analiza evolución mensual del consumo (línea por mes)

### Paso 4: Estadística
- Calcula promedio, desviación, mínimo y máximo de consumo diario.
- Calcula la correlación entre temperatura y consumo.
- Ajusta una regresión lineal simple: consumo ~ temperatura.
- Anota pendiente, intercepto, R² y p-valor.

### Paso 5: Dashboard
- Importa `energia_temp.csv` en Power BI o Tableau.
- Incluye 3 visualizaciones obligatorias:
  - Línea de consumo diario
  - Mapa de consumo por comunidad autónoma
  - Dispersión de consumo vs temperatura
- Añade conclusiones y KPIs arriba.
- Exporta el archivo y guárdalo en `dashboards/`.

### Paso 6: Pipeline ejecutable
- El archivo `main.py` debe ejecutar:
  - extracción
  - limpieza y transformación
  - guardado
  - EDA y estadística

---

## Checklist

### ✔️ Proceso
- Preguntas planteadas desde el inicio
- EDA y visualizaciones realizadas
- Estadísticas descriptivas e inferenciales implementadas
- Transformaciones correctamente aplicadas

### ✔️ Código
- Funciones encapsuladas y reutilizables
- Scripts separados por propósito (ETL, análisis, estadísticas)
- `main.py` ejecuta el flujo completo

### ✔️ Repositorio
- Estructura respetada
- `.gitignore` evita archivos innecesarios
- Dataset limpio en carpeta correspondiente

### ✔️ Documentación
- README completo, claro y útil
- Explicación del objetivo, pasos y resultados
- Gifs o imágenes incluidos

### ✔️ Replicabilidad
- `requirements.txt` completo
- Entorno reproducible
- Proyecto se ejecuta con un solo comando

---

## Recursos Extra

- [API REE](https://api.esios.ree.es/)
- [API AEMET](https://opendata.aemet.es/)
- [Power BI Desktop](https://powerbi.microsoft.com/es-es/desktop/)
- [Tableau Public](https://public.tableau.com/)
- [Licecap (crear gifs)](https://www.cockos.com/licecap/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)
