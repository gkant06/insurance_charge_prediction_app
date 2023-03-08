import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

df = pd.read_csv('insurance.csv')

# Generate some example data
X = df.iloc[:, 0:-1]
y = df.charges

# Create a LinearRegression object
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Make predictions using the model
y_pred = model.predict(X)

# Evaluate the model using mean squared error
mse = mean_squared_error(y, y_pred)

print(mse)

st.subheader('Here is a charge predictor calculator that will calculate your insurance charges based on information you enter below!')

# Adding input options
sex_map = {'Female': 0, 'Male': 1}
gender_options = ['Female','Male']
sex = st.radio('Gender', gender_options)
sex_flag = sex_map[sex]  # Convert sex to binary flag using the dictionary

age = st.number_input('Enter your age', min_value = 18)

# Instead, enter height and weight, add BMI calc
bmi = st.number_input('Enter your BMI', min_value=10, max_value=45)

# No. of children

ch_options = set(df.children)
children = st.selectbox("Enter your no. of children", ch_options)

# Smoking
smoke_map = {'No': 0, 'Yes': 1}
smoking_options = ['No','Yes']
smoking = st.radio('Are you a smoker?', smoking_options)
smoke_flag = smoke_map[smoking]  # Convert sex to binary flag using the dictionary

# Region
region_options = set(df.region)
region = st.selectbox('Select the region you reside in', region_options)

# Enter info

#st.button('Next')

input_dict = {'age': age,
              'sex': sex_flag,
              'bmi': bmi,
              'children': children,
              'smoker': smoke_flag,
              'region': region}

input_df = pd.DataFrame([input_dict])

# Make a prediction using the model
prediction = model.predict(input_df)[0]

# Display the predicted insurance charge to the user
st.subheader('Predicted Insurance Charge')
st.write(f'${prediction:.2f}')