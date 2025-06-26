import streamlit as st 


st.write("Buliding own app")


st.title('Cosmos College')

st.markdown('Sports')

st.header('1200ml')

st.checkbox('Pick option',['yes','NO','Ask Someoneelse'])
st.radio('Gender',['Male','Female'])
st.selectbox('pick a fruit ',['Apple','Mango','Orange'])
st.multiselect('choose a planet ',['Jupyter','March','Earth'])
st.slider('pick a number',0,50)
st.success('you did it !')
st.error('Error Occured ')
st.warning('this is the warning ')
st.info('it is easy to build stramlit app')
st.button("Click here ")
st.number_input('Enter your input :',0,200)

st.sidebar.title('Here it comes ')