# Air Quality Prediction Using Machine Learning

Machine learning side project that predicts the air quality levels in the Central Jakarta area using environmental pollutant measurements. 

This project explores the relationship between pollutant concentrations and the overall air quality index using regression models. 

---

## Project Overview

Air pollution is a major environmental and public health issue in many urban areas.  
This project uses historical air quality data from DKI Jakarta to build predictive models capable of estimating the maximum air quality index value based on pollutant measurements.

The project implements two machine learning models:

• Linear Regression (baseline model)  
• Random Forest Regressor (non-linear ensemble model)

The Random Forest model significantly improves predictive performance compared to the linear baseline.

---

## Dataset

Dataset contains historical air quality measurements from monitoring stations in Jakarta.

Features used in the model:

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

## Machine Learning Pipeline

The workflow implemented in this project includes:

1. **Data Loading**
2. **Data Cleaning**
3. **Feature Selection**
4. **Train/Test Split**
5. **Model Training**
6. **Model Evaluation**
7. **Visualization**
8. **Time-Series Prediction**
