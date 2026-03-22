# Bienestar y Supervivencia Equina
## Que nos dicen los datos sobre el estado emocional y fisico de los caballos?

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-green)
![Kaggle](https://img.shields.io/badge/Datos-Kaggle-20BEFF)
![Tema](https://img.shields.io/badge/Tema-Bienestar%20Equino-brown)
![Estado](https://img.shields.io/badge/Estado-Completo-brightgreen)

---

## Descripcion

Este proyecto analiza datos clinicos de **299 caballos**
para identificar patrones de estres, dolor y bienestar,
y predecir la supervivencia usando Machine Learning.
Se construyo un **Indice de Bienestar propio** basado en
indicadores clinicos reales.

> *"Los datos clinicos cuentan una historia de sufrimiento
> o bienestar antes de que cualquier diagnostico sea posible"*

---

## Objetivos

- Analizar indicadores clinicos de estres y bienestar
- Identificar factores de riesgo de mortalidad equina
- Construir un indice de bienestar propio
- Clasificar caballos por nivel de riesgo con ML
- Comunicar hallazgos con visualizaciones avanzadas

---

## Preguntas que responde este analisis

1. Que indicadores fisicos se asocian con mayor mortalidad?
2. La edad influye en la supervivencia de los caballos?
3. Que variable predice mejor si un caballo sobrevivira?
4. Puede un modelo clasificar correctamente el nivel de riesgo?
5. Como se distribuye el bienestar en el plantel analizado?

---

## Visualizaciones principales

| Grafico | Descripcion |
|---------|-------------|
| ![supervivencia](images/distribucion_supervivencia.png) | Distribucion de supervivencia |
| ![bienestar](images/bienestar_vs_outcome.png) | Bienestar vs resultado clinico |
| ![pulso](images/pulso_por_outcome.png) | Pulso por resultado |
| ![temperatura](images/temperatura_por_outcome.png) | Temperatura por resultado |
| ![dolor](images/dolor_vs_outcome.png) | Dolor vs supervivencia |
| ![correlaciones](images/correlaciones_clinicas.png) | Mapa de correlaciones |
| ![indice](images/bienestar_por_outcome.png) | Indice de bienestar por resultado |
| ![edad](images/edad_vs_outcome.png) | Impacto de la edad |
| ![confusion](images/matriz_confusion_equino.png) | Matriz de confusion ML |
| ![importancia](images/importancia_variables_equino.png) | Variables mas importantes |

---

## Machine Learning

Se entrenó un clasificador **Random Forest** para predecir
si un caballo sobrevivira, morira o sera sacrificado.

### Resultados del modelo

| Clase | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Lived | 0.70 | 0.83 | 0.76 |
| Died | 0.53 | 0.53 | 0.53 |
| Euthanized | 0.50 | 0.11 | 0.18 |
| **Accuracy** | | | **65%** |

### Hallazgos clave

- La **proteina total en sangre** es el predictor
  mas importante de supervivencia
- Los caballos **jovenes** tienen el doble de mortalidad
  que los adultos (45.8% vs 24%)
- Un caballo con indicadores saludables fue clasificado
  como LIVED con **86% de probabilidad**

---

## Indice de Bienestar Propio

Se diseño un indice original (0-9) basado en:

| Indicador | Peso |
|-----------|------|
| Pulso | 3 puntos |
| Temperatura | 2 puntos |
| Dolor | 3 puntos |
| Peristalsis | 2 puntos |

| Nivel | Rango | Tasa de supervivencia |
|-------|-------|-----------------------|
| Alto | 8-9 | 60% |
| Moderado | 5-7 | 79% |
| Bajo | 2-4 | 45% |
| Critico | 0-1 | 18% |

---

## Estructura del proyecto
```
bienestar-equino/
│
├── images/
│   └── (todas las visualizaciones)
│
├── Analisis_Bienestar_Equino.ipynb
├── README.md
└── requirements.txt
```

---

## Tecnologias utilizadas

- **Python 3.12**
- **Pandas** — manipulacion de datos
- **Matplotlib / Seaborn** — visualizacion avanzada
- **Scikit-learn** — Random Forest, StandardScaler
- **Google Colab** — entorno de desarrollo
- **GitHub** — control de versiones

---

## Como ejecutar el proyecto

1. Clona el repositorio:
```bash
git clone https://github.com/George1902/bienestar-equino.git
```

2. Instala las dependencias:
```bash
pip install -r requirements.txt
```

3. Descarga el dataset desde Kaggle:
   [Horse Survival Dataset](https://www.kaggle.com/datasets/yasserh/horse-survival-dataset)
   y guardalo como `horse.csv`

4. Abre el cuaderno en Google Colab o Jupyter

---

## requirements.txt
```
pandas
matplotlib
seaborn
scikit-learn
jupyter
```

---

## Fuente de datos

**Horse Survival Dataset**
Kaggle — Yasser H
Dataset: https://www.kaggle.com/datasets/yasserh/horse-survival-dataset

---

## Autor

**Jorge Ojeda**
Estudiante — Oracle Next Education (ONE) — Alura LATAM
Especializacion: Ciencia de Datos
2026

---

## Licencia

Proyecto de uso educativo y libre distribucion.
Los datos estan disponibles publicamente en Kaggle.
