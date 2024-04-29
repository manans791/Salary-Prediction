# Salary Predictor

In today's world, determining an appropriate salary for individuals can be a challenging task. To address this issue, I have developed a basic model called Salary Predictor. The model is based on key factors such as education level, years of experience, job designation, age, and gender. By analyzing these features, the model provides an estimated prediction of the salary a person deserves.

## Requirements

- Data: The dataset used for this project was obtained from [Kaggle](https://www.kaggle.com/datasets/mrsimple07/salary-prediction-data).
- Python libraries: pandas, numpy, scikit-learn, Flask

## Scope of Project

The scope of the project includes:

- Data cleaning: Removal of outliers, handling null values and incorrect values, Exploratory Data Analysis (EDA).
- Preprocessing: Encoding categorical variables using techniques like one-hot encoding and label encoding.
- Model development: Training a linear regression model on the preprocessed data.
- Hyperparameter tuning: Using grid search cross-validation (GridSearchCV) to find the best parameters for the linear regression model.
- Web application: Using Flask to develop a user-friendly interface for inputting individual characteristics and obtaining salary predictions.
- Hosting: Deployment of the web application for accessibility.

## Conclusion

The Salary Predictor model successfully provides an estimated salary based on the input features. In the future, improvements could involve using datasets with additional features such as quantification of work impact and performance scores. Additionally, exploring alternative machine learning algorithms like random forest could potentially enhance prediction accuracy.
