#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  2 17:01:19 2025

@author: less-is-more
"""

import numpy as np
import pickle
import streamlit as st

#loading the saved model
loaded_model = pickle.load(open('/home/less-is-more/Documents/DataScience-Ml/CarPricePrediction/trained_model.sav', 'rb'))

#Creating a function to do the prediction
def car_price_prediction(input_data):
    
    #changing the input_data to a numpy array
    input_data_as_numpy_array =np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    price = prediction[0]
    return  price

def main():
    #Giving the web app title
    st.title('Car Price Prediction Web App')
    
    #getting the input data from the user
    Year = st.text_input('Year')
    Present_Price = st.text_input('Present price of the vehicle')
    Kms_Driven = st.text_input('Milage driven')
    Fuel_type = st.text_input('For (Petrol= 0, Diesel= 1, CNG= 3 )')
    Seller_Type = st.text_input('For (Dealer = 0. Individual= 1)')
    Transmission = st.text_input('For (Manual=0, Automatic=1)')
    Owner = st.text_input('Write 0')
    
    
    #code for prediction
    prediction1= ''

    #creating a button for prediction
    if st.button('Predict Price'):
       # Convert user inputs to numerical types, handle potential errors
       try:
           year = int(Year)
           present_price = float(Present_Price)
           kms_driven = int(Kms_Driven)
           fuel_type = int(Fuel_type)
           seller_type = int(Seller_Type)
           transmission = int(Transmission)
           owner = int(Owner)

           # Prepare the input data as a list of numerical values
           input_data = [year, present_price, kms_driven, fuel_type, seller_type, transmission, owner]

           # Call the prediction function
           predicted_price = car_price_prediction(input_data)
           st.success(predicted_price)

       except ValueError:
           st.error("Please enter valid numerical values for all the fields.")

    
if __name__ == '__main__':
     main()    