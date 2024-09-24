# Rossmann_Pharmaceuticals

# Rossmann Store Sales Prediction

This project is a machine learning-based solution for predicting daily sales in Rossmann Pharmaceuticals stores up to 6 weeks in advance. The goal is to help Rossmann plan store operations by forecasting future sales. The project also includes an API for serving predictions in real-time.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Technologies Used](#technologies-used)
3. [Setup Instructions](#setup-instructions)
4. [Model Training](#model-training)
5. [API Usage](#api-usage)
6. [Folder Structure](#folder-structure)

## Project Overview

This project tackles the prediction of sales for Rossmann stores using historical data of sales, customers, promotions, holidays, and competition information. The data is sourced from [Kaggle's Rossmann Store Sales dataset](https://www.kaggle.com/c/rossmann-store-sales/data).

The project has been broken down into the following main tasks:

1. **Exploration of customer purchasing behavior**: Analyze customer behavior with respect to promotions, holidays, and competition.
2. **Prediction of store sales**: Build machine learning and deep learning models for sales prediction.
3. **API Deployment**: Provide a REST API for real-time predictions of store sales.

## Technologies Used

- **Python 3.10+**
- **Flask**: For building the REST API.
- **Sklearn**: For data preprocessing and machine learning models.
- **Pandas & Numpy**: For data manipulation.
- **Matplotlib & Seaborn**: For data visualization.
- **TensorFlow/PyTorch**: For building deep learning models (LSTM).
- **Pickle**: For model serialization.

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/fro-su/Rossmann_Pharmaceuticals.git
cd Rossmann_Pharmaceutical
```

### 2. Install Dependencies

First, ensure you have Python 3.10+ installed. Then, create a virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate   # For Linux/Mac
venv\Scripts\activate      # For Windows

pip install -r requirements.txt
```

### 3. Set Up the Dataset

- Download the dataset from [Kaggle's Rossmann Store Sales competition](https://www.kaggle.com/c/rossmann-store-sales/data).
- Place the dataset files (`train.csv`, `test.csv`, etc.) in the `data/` folder.

### 4. Run the Flask Application

To serve the model predictions via API, run the Flask application:

```bash
python app/app.py
```

By default, the application will be served at `http://127.0.0.1:5000`.

## Model Training

### 1. Preprocessing & Feature Engineering

The preprocessing step involves converting categorical features into numeric ones, handling missing values, and extracting additional features from datetime columns (such as weekdays, holidays, etc.). The code for data preprocessing is located in the `notebooks/` folder.

### 2. Machine Learning Model (Random Forest Regressor)

To train the Random Forest model, follow the steps provided in the Jupyter notebooks (`train_model.ipynb`). After training, the model is serialized and saved using Pickle.

### 3. Deep Learning Model (LSTM)

An LSTM model is implemented to capture temporal dependencies in sales data. The LSTM model is located in the `notebooks/` folder, and its predictions can also be served by the API.

## API Usage

### 1. Prediction Endpoint

- **Endpoint**: `/predict`
- **Method**: POST
- **Content-Type**: `application/json`

The model will return the predicted sales for the given input data.

### 2. Error Handling

If there is an issue with the request, such as missing fields or invalid input, the API will return an error message.
