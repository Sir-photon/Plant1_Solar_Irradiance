# Plant1_Solar_Irradiance
Solar Irradiance Prediction Model Development and Deployment

PLANT1 IRRADIANCE FORECAST API

## My Portfolio project

This project proposes a solution for solar irradiance forecasting, which is critical for optimizing grid-integrated renewable energy systems and intelligent energy management. Accurate irradiance prediction helps to reduce energy losses, improve grid stability, and support predictive maintenance of solar installations.

## My Proposed Solution:

Development of Machine Learning-based Solar Irradiance Forecasting Model with FastAPI

This project utilizes historical irradiance and environmental data to develop a machine learning model capable of predicting solar irradiance. The model is served through a FastAPI application to provide real-time predictions via an API.

## *Objectives*

- Develop a machine learning algorithm that can effectively predict solar irradiance using historical and environmental features.

- Analyze irradiance trends and enable visualization for user understanding.

- Deploy the model into a FastAPI web application for programmatic access.

- Develop a RESTful API to make predictions accessible to external applications.

- Test the system and evaluate model performance with metrics like R² and MSE.

## Method

*START*

Data Acquisition

Gathered environmental and irradiance datasets including temperature, module temperature, and time features.

Data Preprocessing

Feature engineering with lag variables, rolling statistics, and cyclical time features (sin/cos transformations).

Handling missing values and scaling if necessary.

Data Exploration and Analysis

Explored relationships between temperature, irradiation, and time features.

Visualized trends and correlations to guide feature selection.

Model Training, Testing, and Evaluation

Trained XGBoost regression model with lag and rolling features.

Evaluated using R² and MSE to measure forecasting performance.

Model Deployment

Saved trained model and feature columns using joblib.

Integrated model into a FastAPI application for inference.

WebApp Development

Built minimal FastAPI app with /predict endpoint.

Input validation using Pydantic models to ensure correct API requests.

Development of API

API accepts feature input in JSON format and returns predicted irradiance.

/docs endpoint automatically generated via FastAPI Swagger UI for testing and demonstration.

END

## Conclusion

This project demonstrates the complete pipeline for solar irradiance forecasting from data acquisition, ML model training, evaluation, to API deployment.

It showcases skills in:

Feature engineering for time-series forecasting

Machine learning model development (XGBoost)

API development with FastAPI

Preparing production-ready ML artifacts for deployment
