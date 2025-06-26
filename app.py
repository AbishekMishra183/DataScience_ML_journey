# input feilds haru banaune ho 

import streamlit as st 

st.set_page_config(
    page_title='Diabetes Predection App'

)

st.title('Diabiates Predection')
st.header('Input you data:')

Gulcose=st.number_input('Gulcose',min_value=0,max_value=400,value=20)
blood_pressure=st.number_input('Blood Pressure',0,200,0)