#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:51:20 2024

@author: adriandominguezcastro
"""

import streamlit as st
import numpy as np
import pandas as pd
from io import StringIO

import matplotlib.pyplot as plt
import seaborn as sb

#import pickle
import joblib

import urllib.request




# Variable de estado para controlar la página actual
state = st.experimental_get_query_params().get("state", ["project_description"])[0]

# Add a title
st.title('Wine Quality Prediction Project using Machine Learning')

# Add space
st.write("")
st.markdown("---")

# Create a horizontal menu using buttons
menu_items = ['Project Description', 'Exploratory Data Analysis', 'Wine Quality Prediction']

# Create columns to display buttons horizontally
col1, col2, col3 = st.columns(3)

# Add buttons to columns
selected_item_home = col1.button('Project Description')
selected_item_eda = col2.button('Exploratory Data Analysis')
selected_item_wqp = col3.button('Wine Quality Prediction')


# Display different content based on the selected menu item
if state == "project_description":
    st.header("Project Description")
    # Add your project description content here
    
    st.write('')
    st.markdown("---")
    # Add an image
    st.image('https://github.com/DrAdrianDC/Portfolio-for-Data-Science/blob/main/Project-1-Wine-Quality-Prediction/DSC01511.JPG', caption='Photo by the author during a trip to Porto, Portugal in November 2019', width=500) #use_column_width=True)


    # Add space
    st.write("")
    st.markdown("---")

    st.header("Project Description")
    st.write("<br>", unsafe_allow_html=True)
    st.empty()
    st.write("<br>", unsafe_allow_html=True)
    st.write(" Wine has been part of human civilization for centuries. Beyond the cultural significance, the wine industry is a powerful economic sector. In modern times, machine learning predictions can provide valuable insights for winemakers and the wine industry in general to make informed decisions on innovation, efficiency and improving the quality of the their wines to meet market demands.")         
   
    # Add space
    st.empty()
    st.write("<br>", unsafe_allow_html=True)
    
    st.write(" The main goal is to build a robust machine learning model that can accurately predict the quality of wines using physicochemical variables such as acidity, alcohol concentration, pH, etc. In this classification problem, the quality of wine can be represented as a discrete variable, often categorized into classes such as bad, and good quality. Various classification algorithms such as logistic regression, random forests, xgboost, and a deep neural network are considered.")
    
    st.empty()
    st.write("<br>", unsafe_allow_html=True)
    
    st.write(" The project involve several key steps as following:")
    st.markdown("**Data Collection:** We gather a dataset containing various physicochemical properties of wines, such as acidity, alcohol concentration, pH, and quality ratings.")
    st.markdown("https://www.kaggle.com/datasets/yasserh/wine-quality-dataset")
    st.markdown("**Exploratory Data Analysis (EDA):** We perform EDA to understand the relationships between the features and the target variable (quality), and to identify any patterns or anomalies in the data.")

    st.markdown("**Model Selection and Training:** We select a suitable machine learning algorithm and train it on the preprocessed data.")
    st.markdown("**Deployment:** Once deploy the model to make predictions on new, unseen data.")

    st.empty()
    st.write("<br>", unsafe_allow_html=True)
    st.header("Conclusions:")
    st.markdown("---")
    st.write("The most relevant results obtained for the Machine Learning algorithms explored are (order based on Validation Accuracy):")
    st.write(" * Random Forest ( 77.26%)")
    st.write(" * XGBoost ( 76.38%)")
    st.write(" * Deep Neural Network (75.22%)")
    st.write(" * Logistic Regression (73.4%)")
    st.write("The accuracy of the wine quality prediction results can be improved by increasing the amount of data obtaining a superior balance between the different class of wine quality studied here.")
    st.write("In addition, a search of hyperparameters, the use of regularization, and a simplification of the model are alternatives to consider to avoid potential overfitting and a overall model performance.")     




    
elif state == "exploratory_data_analysis":
      st.header("Exploratory Data Analysis")
      st.write('')
      st.markdown("---")
      st.header("Exploratory Data Analysis")
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
      
      
      
      
      
      # Download the CSV file
      url = 'https://github.com/DrAdrianDC/Portfolio-for-Data-Science/raw/main/Project-1-Wine-Quality-Prediction/WineQT.csv'
      urllib.request.urlretrieve(url, 'WineQT.csv')

      
      # Load the data
      df = pd.read_csv('WineQT.csv')
      #df = pd.read_csv('https://github.com/DrAdrianDC/Portfolio-for-Data-Science/blob/main/Project-1-Wine-Quality-Prediction/WineQT.csv')
    
      st.markdown('#### Summary of the dataset')
      # Capture the output of df.info()
      string_buffer = StringIO()
      df.info(buf=string_buffer)
      info_str = string_buffer.getvalue()

      # Display the captured info in Streamlit
      st.text(info_str)
      
      # Adding space
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
      
      #descriptive statistical measures of the dataset.
      st.markdown('#### Descriptive statistical measures of the dataset')
      pd.set_option('display.max_rows', None)
      
      st.write(df.describe().T)
      
    
      # Reset display options to default
      pd.reset_option('display.max_rows')
      
      # Adding space
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
      
      # Plot of the physicochemical attributes of wine dataset
      st.markdown('#### Plot of physicochemical attributes of wine dataset')
      plt.figure(num=None)
      histograms = df.hist(bins=20, figsize=(10, 10))
      st.pyplot(plt)
      
      #Display the dataframe
      #st.write(df)
      
      # Adding space
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
      
      st.markdown('###### Remarks:')
      
      # List 
      remarks = [
      "The quality of wine varies from 3 to 8, with 5.657 as an average quality.",
      "Total sulfur dioxide varies between 6 to 289.",
      "The average density of wine is  0.9967.",
      "The alcohol level in average is 10.4421, with a maximum level of 14.9 and a minimum level of 8.4.",
      "pH level varies between 2.74 to 4.01."
     
      
      
      ]

      # Enumerate and display the sentences
      for index, remarks in enumerate(remarks, start=1):
       st.write(f"{index}. {remarks}")
      
      # Adding space
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
      
      st.markdown('#### How it looks the wine quality in the dataset ?')
      #plt.figure(figsize=(5, 5))
      plt.figure(num=None, figsize=(10, 6))  # Set the figure size
      plot_quality = sb.countplot(df['quality'])
      plot_quality.set_xticklabels(plot_quality.get_xticklabels(), fontsize=10)
      plot_quality.set_yticklabels(plot_quality.get_yticklabels(), fontsize=10)

# Add text labels to the bars
      for p in plot_quality.patches:
          x = p.get_x() + p.get_width() / 2
          y = p.get_height()
          plot_quality.annotate(format(p.get_height(), '.0f'),
                          (x, y),
                          ha='center',
                          va='center',
                          xytext=(0, 6),
                          textcoords='offset points',
                          fontsize=10)

      st.pyplot(plt)

      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      st.markdown('###### There are a total of 6 different qualities of wine')
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
       
      # Analyzing the correlation between features
      st.markdown("#### How each of the features relates to wine quality?")
      
      # Adding space
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
     # st.markdown(" How each of the features relates to wine quality? ")
     
      st.markdown('###### Note: In the correlation matrix, correlation between two variables, in the range of -1 to 1. If two variables have a high correlation, we can neglect one variable from those two.')
      
      # Adding space
      st.write("<br>", unsafe_allow_html=True)
      st.empty()
      
      plt.figure(figsize=(21, 21))
      heatmap = sb.heatmap(df.corr(), annot=True, cmap= 'coolwarm' ,cbar=True, annot_kws={"fontsize":22})
      cbar = heatmap.collections[0].colorbar
      cbar.ax.tick_params(labelsize=22)
      heatmap.set_xticklabels(heatmap.get_xticklabels(), fontsize=24)
      heatmap.set_yticklabels(heatmap.get_yticklabels(), fontsize=24)
      st.pyplot(plt)
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      st.write("What are the features strongly correlated to wine quality? Top features are:")
      st.write(df.corr()['quality'].sort_values(ascending=False))
      
      
      st.markdown(" #### Plot alcohol vs quality")
      st.markdown("**The alcohol content is the feature most strongly correlated with wine quality.** Therefore, it is interesting to analyze whether there is a clear pattern of high alcohol levels being associated with high quality.")
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      st.write("The plot visualizes the relationship between the 'quality' and 'alcohol' variables in your dataset")
      st.write("Each bar's height corresponds to the average alcohol content for wines of a particular quality level.")
      plt.figure(num=None)
      sb.barplot(x='quality', y='alcohol', data=df, edgecolor=None, linewidth=0)
      st.pyplot(plt)
      
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      st.write("The bars are generally increasing from left to right, it suggests that higher quality wines tend to have higher alcohol content on average")
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      
      st.header("Data Processing")
      st.markdown("----")
      
      # Data Processing
      
      # Scale the dataset by quality
      st.write("The dataset can be viewed as classification or regression tasks. The target variable 'quality' is a integer value. In order to treat as a classification problem,  we scale the dataset by quality.")
      
      items =['quality > 5 is “good”','quality <= 5 is “bad”']
     
      for item in items:
       st.markdown(f"- {item}")
      
      df['quality'] = df.quality.apply( lambda x:1 if x>5 else 0) 
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      # Adding space
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      
      # Plot quality classification 
      
      df['quality'].value_counts()
      
      plt.figure(num=None)
      sb.countplot(data = df, x = 'quality', saturation=0.5)
      plt.title("Types of Wine")
      plt.xticks([-1,0,1,2], ['','bad wine','good wine',''])
      st.pyplot(plt)
      
      
    

elif state == "wine_quality_prediction":
      st.header("Wine Quality Prediction")

    
      st.write('')
      st.markdown("---")


      st.title("Wine Quality Prediction")
# Adding space      
      st.write('')
      st.markdown("---")
      
      # Create columns to display buttons horizontally
      col1, col2, col3 = st.columns(3)

# Crear botones y cajas de texto para ingresar los datos

      fixed_acidity = col1.number_input("Fixed Acidity", 0.0, 100.0, 7.5)
      volatile_acidity =col2.number_input("Volatile Acidity", 0.0, 100.0, 0.5)
      citric_acidity = col3.number_input("Citric Acidity", 0.0, 100.0, 0.0)
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      residual_sugar = col1.number_input("Residual Sugar", 0.0, 100.0, 1.5)
      chlorides = col2.number_input("Chlorides", 0.0, 100.0, 0.05)
      free_sulfur_dioxide = col3.number_input("Free Sulfur Dioxide", 0.0, 1000.0, 10.0)
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      total_sulfur_dioxide = col1.number_input("Total Sulfur Dioxide", 0.0, 1000.0, 25.0)
      density = col2.number_input("Density", 0.0, 2.0, 0.95)
      pH = col3.number_input("pH", 0.0, 14.0, 3.5)
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      sulphates = col1.number_input("Sulphates", 0.0, 10.0, 0.5)
      alcohol = col2.number_input("Alcohol", 0.0, 100.0, 9.5)
      st.write("")
      st.markdown("")
    
       #Cargar el modelo entrenado
     # model = joblib.load("LogReg_joblib.pkl")
      model = joblib.load("RF_joblib.pkl")
      

      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      st.write("")
      st.markdown("---")
        
        
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      st.write("Note: The model used on the Prediction is the one based on the Random Forest algorithm.")
      st.write("")
      
      st.empty()
      st.write("<br>", unsafe_allow_html=True)
      st.write("")
      
# Definir la función para predecir la calidad del vino
      def predict_quality(fixed_acidity, volatile_acidity, citric_acidity, residual_sugar, chlorides,
                     free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol):
       input_data = np.array([[fixed_acidity, volatile_acidity, citric_acidity, residual_sugar, chlorides,
                             free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]])
       prediction = model.predict(input_data)
       return prediction
    
      if st.button("Predict", key="predict_button"):
        prediction = predict_quality(fixed_acidity, volatile_acidity, citric_acidity, residual_sugar, chlorides,
                                  free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol)
        
        
        # Mostrar el resultado de la predicción
        if prediction[0] == 0:
            st.write("Predicted wine quality: Bad")
        elif prediction[0] == 1:
            st.write("Predicted wine quality: Good")
        
      #  st.write(f"Predicted wine quality: {prediction[0]}")
        st.write("")
        st.markdown("")
        

         
      
# Update the state based on the selected menu item
if selected_item_home:
    st.experimental_set_query_params(state="project_description")
elif selected_item_eda:
    st.experimental_set_query_params(state="exploratory_data_analysis")
elif selected_item_wqp:
    st.experimental_set_query_params(state="wine_quality_prediction")  

           
