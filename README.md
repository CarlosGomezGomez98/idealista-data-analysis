# Recomendador de Precios de Inmuebles en Barcelona

### Análisis del mercado inmobiliario mediante Web Scraping, Clustering y modelos de Regresión.

> **Nota para el reclutador:** Este proyecto es el resultado de mi Trabajo de Fin de Máster en Big Data, donde apliqué un pipeline completo de ciencia de datos para analizar y predecir los precios de la vivienda en uno de los mercados más dinámicos de España.

## 📜 Descripción

[cite_start]Este proyecto nace de la creciente dificultad para el acceso a la vivienda en España, especialmente en grandes ciudades como Barcelona[cite: 69, 70, 71]. [cite_start]Motivado por este contexto, el objetivo principal fue desarrollar una herramienta de machine learning capaz de **estimar con precisión el precio de venta de un inmueble en Barcelona** a partir de sus características[cite: 78].

[cite_start]Para lograrlo, se realizó un proceso integral que abarca desde la recolección de datos mediante **web scraping** de más de 12,000 anuncios en Idealista [cite: 75][cite_start], hasta el entrenamiento y la evaluación de múltiples modelos de regresión y clustering, culminando en una **interfaz gráfica interactiva** para el usuario final[cite: 1348, 1351].

## ✨ Características Principales

* [cite_start]**Recolección de Datos Automatizada:** Se implementó un scraper con `Selenium` y `Beautiful Soup` para extraer datos detallados de Idealista, superando las medidas de anti-scraping del portal[cite: 399, 402].
* [cite_start]**Ingeniería de Características:** Limpieza y preprocesamiento exhaustivo de los datos, incluyendo la creación de nuevas variables a partir de datos textuales (ej. `ascensor`) [cite: 627][cite_start], codificación de variables categóricas [cite: 612] [cite_start]y gestión de valores nulos[cite: 643].
* [cite_start]**Segmentación del Mercado con Clustering:** Se aplicó el algoritmo **K-Means** para segmentar el mercado en 4 clústeres distintos [cite: 858][cite_start], identificando arquetipos de propiedades desde económicas hasta lujo[cite: 880, 901, 920, 939].
* [cite_start]**Modelado Predictivo Avanzado:** Se entrenaron y evaluaron 7 algoritmos de regresión distintos [cite: 1165][cite_start], incluyendo `Lasso` [cite: 1166][cite_start], `Random Forest` [cite: 1173][cite_start], `Gradient Boosting` [cite: 1175][cite_start], `XGBoost` y Redes Neuronales (`MLPRegressor`)[cite: 1178].
* [cite_start]**Interfaz de Usuario Interactiva:** Se desarrolló una aplicación web con `Streamlit` que permite a cualquier usuario introducir las características de una vivienda y obtener una estimación de su precio al instante[cite: 1348, 1351, 1353].

## 🛠️ Stack Tecnológico

| Área | Tecnologías y Librerías |
| :--- | :--- |
| **Análisis y Modelado** | [cite_start]`Python`, `Pandas`, `NumPy`, `Scikit-learn` [cite: 2225, 2228, 2229, 2230, 2231, 2232, 2233, 2234, 2236, 2237][cite_start], `XGBoost` [cite: 2237][cite_start], `Matplotlib` [cite: 2240][cite_start], `Seaborn` [cite: 2242] |
| **Web Scraping** | [cite_start]`Selenium` [cite: 1440, 1441][cite_start], `Beautiful Soup` [cite: 1435][cite_start], `undetected-chromedriver` [cite: 1443] |
| **Aplicación Web** | [cite_start]`Streamlit` [cite: 2820] |
| **Desarrollo** | [cite_start]`Jupyter Notebooks`, `Joblib` [cite: 2243] |

## 📊 Resultados Destacados

Tras un riguroso proceso de validación cruzada y optimización de hiperparámetros, se obtuvieron los siguientes resultados:

* [cite_start]El modelo con mejor rendimiento fue **Gradient Boosting** (entrenado con el dataset sin outliers), alcanzando un **coeficiente de determinación (R²) de 0.812**[cite: 1256, 1309]. Esto significa que el modelo es capaz de explicar aproximadamente el 81% de la variabilidad del precio de la vivienda.
* [cite_start]El análisis de clustering con K-Means ($k=4$) reveló 4 segmentos de mercado bien definidos[cite: 858]:
    1.  [cite_start]**Clúster 0:** Propiedades estándar, funcionales y accesibles[cite: 880].
    2.  [cite_start]**Clúster 1:** Propiedades amplias, bien equipadas y de gama alta[cite: 901].
    3.  [cite_start]**Clúster 2:** Propiedades pequeñas y económicas, con pocas comodidades[cite: 920].
    4.  [cite_start]**Clúster 3:** Propiedades de lujo y exclusivas con comodidades premium[cite: 939].

### Demostración de la Interfaz

[cite_start]Captura de la aplicación desarrollada con Streamlit que permite predicciones en tiempo real[cite: 1376].

![Interfaz de Streamlit](https://i.imgur.com/2A2G1nK.png)

## 🔧 Cómo Empezar

Para ejecutar este proyecto de forma local, sigue estos pasos:

**1. Prerrequisitos**
* Asegúrate de tener Python 3.8 o superior instalado.

**2. Clonar el Repositorio**
```bash
git clone [https://github.com/tu-usuario/tu-repositorio.git](https://github.com/tu-usuario/tu-repositorio.git)
cd tu-repositorio
