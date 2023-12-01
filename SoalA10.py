import pickle

import streamlit as st
import pandas as pd
import os
import datetime
import numpy as np
import altair as alt
import time
import streamlit as st
import matplotlib.pyplot as plt

st.title('WELCOME')

menu = ['Home', 'Dashboard', 'Profile']
selected_menu = st.sidebar.selectbox('Menu', menu)

if selected_menu == 'Home':
    st.subheader('Welcome to Home Page DHARIZZ')
    st.image('image2.jpeg', use_column_width=True)

    # Read dataset (csv)
    data = pd.read_csv('data2.csv')

    # Display a sample of the dataset
    st.subheader('Sample of the Dataset:')
    st.write(data.head(10))

    # Create a function to generate the plot
    def plot_bar_chart(data):
        fig, ax = plt.subplots()
        if np.issubdtype(data.dtype, np.number):
            data.plot(kind='bar', ax=ax)
        else:
            data.value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

    # Create a select box for the user to choose the feature to plot
    features = data.columns.tolist()
    selected_feature = st.selectbox('Choose the feature to plot', features)

    # Filter the data based on the selected feature
    filtered_data = data[selected_feature]

    # Plot the bar chart based on the selected feature
    plot_bar_chart(filtered_data)

elif selected_menu == 'Dashboard':
    st.subheader('Welcome to Dashboard DHARIZZ')
    st.image('image2.jpeg', use_column_width=True)

    # Read dataset (csv)
    data = pd.read_csv('data2.csv')

    # Your dashboard-specific code goes here
    st.write("This is the Dashboard page. You can add your specific content here.")

# Other pages can be added similarly
elif selected_menu == 'Profile':
    st.subheader('Welcome to Profile Page DHARIZZ')

    # Add a form for personal biodata
    st.subheader('Personal Biodata:')
    name = st.text_input('Name', '')
    age = st.number_input('Age', 0, 150, 0)
    address = st.text_area('Address', '')

    # Add a file uploader for a photo
    st.subheader('Upload Photo:')
    uploaded_file = st.file_uploader("Choose a photo...", type="jpg")

    # Display the submitted biodata
    st.subheader('Submitted Biodata:')
    st.write(f'Name: {name}')
    st.write(f'Age: {age}')
    st.write(f'Address: {address}')

    # Display the uploaded photo
    if uploaded_file is not None:
        st.image(uploaded_file, caption='Uploaded Photo', use_column_width=True)
