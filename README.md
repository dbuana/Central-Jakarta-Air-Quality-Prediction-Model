# Air Quality Prediction Using Machine Learning

Machine learning side project that predicts the air quality levels in the Central Jakarta area using environmental pollutant measurements. 

---

## Project Overview

In the populated capital of Indonesia, air pollution has been a major environmental and health issue for years. This project utilizes air quality data from Central Jakarta to create a predictive model capable of estimating maximum air quality index based on the concentration of the pollutants.  

The project implements two machine learning models:

• Linear Regression (baseline model)  
• Random Forest Regressor (non-linear ensemble model)

---

## Dataset

The dataset contains air quality measurements from monitoring in different times in the Central Jakarta area.

Exploratory variables:

| Feature | Description |
|------|------|
| PM10 | Particulate Matter ≤10 micrometers |
| SO2 | Sulfur Dioxide concentration |
| CO | Carbon Monoxide concentration |
| O3 | Ozone concentration |
| NO2 | Nitrogen Dioxide concentration |

Target variable:
| Target | Description |
|------|------|
| max | Maximum air quality index value |

Additional columns include:
- `tanggal` (date)
- `categori` (air quality category)

---
8. **Time-Series Prediction**
