import streamlit as st
import joblib
model = joblib.load('ADMISSION PREDICTION')
st.title('WILL YOU BE GET ADMITTED? ENTER THE DETAILS BELOW TO CHECK YOUR CHANCES!')
if st.button('Start'):
  a1 = st.number_input('Enter your GRE Score')
  a2 = st.number_input('Enter your TOEFL Score')
  a3 = st.number_input('Enter your University Rating')
  a4 = st.number_input('Enter your SOP')
  a5 = st.number_input('Enter your LOR')
  a6 = st.number_input('Enter your CGPA')
  a7 = st.number_input('Enter your RESEARCH PROGRESS(Answer in 0 or 1)')


op = model.predict([[a1,a2,a3,a4,a5,a6,a7]])
if st.button('SUBMIT!'):
  if op[0] < 0:
    st.title('Please Enter Appropriate Values!')
  else:
    st.title(str(op[0]*100) + '%')
      
    
