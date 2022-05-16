import codecademylib3
import pandas as pd
import numpy as np

# code goes here
diabetes_data = pd.read_csv('diabetes.csv')

diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = diabetes_data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

print(diabetes_data.isnull().sum())
print(diabetes_data[diabetes_data.isnull().any(axis=1)])
print(diabetes_data.dtypes)
print(diabetes_data['Outcome'].unique())
print(diabetes_data.shape)
# Data has 768 rows and 9 columns 
print(diabetes_data['Outcome'].unique())
diabetes_data['Outcome'] = diabetes_data['Outcome'].replace('O', 0).astype(int)
print(diabetes_data['Outcome'].unique())

print(diabetes_data.describe(include='all'))
# print(diabetes_data.dtypes)
print(diabetes_data.info('all'))
print(diabetes_data.shape)
#print(diabetes_data.isnull().sum())
# Pregnancies: Number of times pregnant
# Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
# BloodPressure: Diastolic blood pressure
# SkinThickness: Triceps skinfold thickness
# Insulin: 2-Hour serum insulin
# BMI: Body mass index
# DiabetesPedigreeFunction: Diabetes pedigree function
# Age: Age (years)
# Outcome: Class variable (0 or 1)