import streamlit as st
import joblib
model = joblib.load('ADMISSION PREDICTION')
st.title('WILL YOU BE GET ADMITTED? ENTER THE DETAILS BELOW TO CHECK YOUR CHANCES!')
list = ['GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA','RESEARCH PROGRESS(Answer in 0 or 1)']
list_for_input = [1,2,3,4,5,6,7]
if st.button('Start'):
  for i in range(0,7):
      list_for_input[i] = st.number_input(f'Enter your {list[i]}')
      
  
op = model.predict([list_for_input])
if st.button('SUBMIT!'):
  st.title(str(op[0]*100) + '%')
      
