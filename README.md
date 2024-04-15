# Stroke Prediction Project 

## Introduction
The goal of the Healthcare Stroke Prediction Project is to utilize various health indicators from a collected dataset to predict the likelihood of stroke events in individuals. This project involves data cleaning, exploratory analysis, feature engineering, and the application of several machine-learning techniques to achieve reliable stroke prediction. 

The notebook can be found [here](https://github.com/EllePancake/Stroke-Prediction-Project/blob/main/Healthcare%20Stroke%20Project.ipynb)

## Project Objectives
- To understand the relationship between health indicators and the occurrence of strokes.
- To clean and prepare the dataset for modeling.
- To engineer features that enhance the predictive power of the models.
- To compare different machine learning models based on their performance.
- To predict the likelihood a patient will have a stroke.

## Table of Contents
1. **Introduction and Goals**
   - Outline of the project's aim and the main objectives.
2. **Initial Analysis with Pandas**
   - Preliminary data examination to understand the dataset structure and content.
3. **Data Cleaning**
   - Handling missing values, anomalies, and data type corrections to improve data quality.
4. **Outlier Detection**
   - Identification and treatment of outliers to standardize data inputs.
5. **Feature Engineering**
   - Creation of new features from existing data to boost model accuracy and performance.
6. **Splitting Data**
   - Preparation of training and testing datasets with both original and engineered features.
7. **Exploratory Analysis**
   - Detailed analysis including:
     - **Categorical Univariate Insights**: Distribution of categorical data.
     - **Numerical Univariate Insights**: Distribution and behavior of numerical features.
     - **Age-Groups Analysis**: Investigation of health indicators across different age groups.
     - **BMI & BMI Categories**: Exploration of BMI distributions and their impact on health outcomes.
8. **Statistical Inference**
   - Testing hypotheses to derive statistically significant conclusions from the data.
9. **Baseline ML Model**
   - Development of a baseline model to set a performance benchmark.
10. **SMOTE and Scaling Techniques**
    - Application of SMOTE for addressing class imbalance and various scaling methods to normalize features.
11. **Machine Learning Models**
    - Evaluation of models including K-Nearest Neighbors, Random Forest, XGBoost, and LightGBM.
    - Discussion on the implications of using SMOTE with each model.
12. **Improvement Suggestions**
    - Recommendations for enhancing model performance and data handling.

## Additional Analysis

After the initial notebook, I looked into a GridSearchCV alternative and used Optuna to further investigate the LightGBM model and attempt to achieve better results.

The Light GBM Notebook is [here](https://github.com/EllePancake/Stroke-Prediction-Project/blob/main/Digging%20into%20the%20Light%20GBM%20Model.ipynb)

## Model Deployment

If you want to follow the exact steps I followed to deploy the model you can find the guide I used [here](https://towardsdatascience.com/introduction-to-ml-deployment-flask-docker-locust-b87b5bd78a17) and the file I used to export the model [here](https://github.com/EllePancake/Stroke-Prediction-Project/blob/main/Deployment%20of%20Model%20-%20Pickle.ipynb). 

The packages needed: pandas, lightgbm, pickle, flask

### Step 1: Download the necessary files and place them into the folder you'll be working in.
- [The Main App](https://github.com/EllePancake/Stroke-Prediction-Project/blob/main/app.py)
- [The Model](https://github.com/EllePancake/Stroke-Prediction-Project/blob/main/model.pkl)
- [The Test File](https://github.com/EllePancake/Stroke-Prediction-Project/blob/main/app_test.py) (optional)

### Step 2: Run "python app.py" in your terminal. Make sure you're working from the folder the files are in. 
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/7f2a32fc-e9a5-4f19-8973-8876ba18d33c)

### Step 3: Hover over one of the websites and click on visit to navigate to the website. 
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/099c920e-7619-430a-a79c-7a9447c3bc5f)

### Step 4: Complete the form by selecting the correct option from the dropdown, selecting hypertension and/or heart disease, and filling in the numbers for Age, Avg Glucose Level, and BMI.
- Age: takes takes positive integers
- Avg Glucose Level: takes positive floats
- BMI: takes positive floats
  
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/0431c3d8-8146-4fbe-8ab6-91b2acbd8c6e)

### Step 5: See the result for your input!
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/f0218bf5-f0c3-4872-8888-c4d7c864ebb7)

### Step 6 (optional): You can also try the model this way. Open the app_test.py file, replace the figures with your own, and save the file.
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/f7ef01f6-11ca-4194-b420-719f69a41023)

### Step 7 (optional): Run "python app_test.py" in your terminal. Make sure you're working from the folder the files are in. 
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/e8e30497-684d-4906-99b2-cdab872790f4)

### Step 8 (optional): See the result for your input in the terminal!
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/9ccf57ae-9eec-477d-9a86-c6444900da50)

### Step 9: Press CTRL + C to terminate the program. 
![image](https://github.com/TuringCollegeSubmissions/lrodri-ML.2.5/assets/107210379/d0ae7be3-aebc-4ab0-8316-85efa0757df5)
