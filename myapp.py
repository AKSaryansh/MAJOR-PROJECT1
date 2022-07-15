import streamlit as st
import joblib
model = joblib.load('ADMISSION PREDICTION')
st.title('WILL YOU BE GET ADMITTED? ENTER THE DETAILS BELOW TO CHECK YOUR CHANCES!')
if st.button('Start'):
  a1 = st.number_input('Enter your GRE SCORE')
if st.button('Next'):
  a2 = st.number_input('Enter your TOEFL Score')
if st.button('Next'):
  a3 = st.number_input('Enter your University Rating')
if st.button('Next'):
  a4 = st.number_input('Enter your SOP')
if st.button('Next'):
  a5 = st.number_input('Enter your LOR')
if st.button('Next'):
  a6 = st.number_input('Enter your CGPA')
if st.button('Next'):
  a7 = st.number_input('Have you done some Research (Answer in 1 or 0)')
op = model.predict([[a1,a2,a3,a4,a5,a6,a7]])
if st.button('SUBMIT!'):
  st.title(str(op[0]*100) + '%')
  
