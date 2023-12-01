import pickle

import streamlit as st
import pandas as pd
import os
import datetime
import numpy as np
import altair as alt
import time
import streamlit as st

model = pickle.load(open('model_prediksi_harga_mobil.sav', 'rb'))


with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

#ambil waktu saat ini
now = datetime.datetime.now()

#format waktu tanggal
formatted_now = now.strftime("%d/%m/%Y %H:%M:%S")

#tampilkan waktu tanggal
st.write("Waktu tanggal up to date: " + formatted_now)



st.title('Prediksi Harga Mobil')
st.image('car.jpg')

#open file csv
df1 = pd.read_csv("CarPrice.csv")

view = st.sidebar.selectbox('Tampilkan data', ['Dataset', 'Grafik Highway-mpg', 'Grafik curbweight', 'Grafik horsepower'])

if view == 'Dataset':
    st.header("Dataset")
    st.dataframe(df1)

elif view == 'Grafik Highway-mpg':
    st.write("Grafik Highway-mpg")
    chart_highwaympg = df1['highwaympg']
    st.line_chart(chart_highwaympg)

elif view == 'Grafik curbweight':
    st.write("Grafik curbweight")
    chart_curbweight = df1['curbweight']
    st.line_chart(chart_curbweight)

elif view == 'Grafik horsepower':
    st.write("Grafik horsepower")
    chart_horsepower = pd.DataFrame(df1, columns=["horsepower"])
    st.line_chart(chart_horsepower)

#input nilai dari variable independent
highwaympg = st.number_input('highwaympg')
curbweight = st.number_input('curbweight')
horsepower = st.number_input('horsepower')

if st.button('Prediksi'):
    #prediksi variable yang telah diinputkan
    car_prediction = model.predict([[highwaympg, curbweight, horsepower]])

    # convert ke string
    harga_mobil_str = np.array(car_prediction)
    harga_mobil_float = float(harga_mobil_str)

    #tampilkan hasil prediksi
    st.write(f'Prediksi harganya adalah {harga_mobil_float:.2f}')


progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)
time.sleep(1)
my_bar.empty()

st.button("Refresh")