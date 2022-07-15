import streamlit as st
import joblib
model = joblib.load('ADMISSION PREDICTION')
st.title('WILL YOU BE GET ADMITTED? ENTER THE DETAILS BELOW TO CHECK YOUR CHANCES!')
list = ['GRE Score','TOEFL Score','University Rating','SOP','LOR','CGPA','RESEARCH PROGRESS(Answer in 0 or 1)','end']
if st.button('Start'):
  a1 = number_input('Enter',key = 0)
  if st.button('Next',key = 0):
    a2 = number_input('Enter',key = 1)
    if st.button('Next',key = 1):
      a3 = number_input('Enter',key = 2)
      if st.button('Next',key = 2):
        a4 = number_input('Enter',key = 3)
        if st.button('Next',key = 3):
          a5 = number_input('Enter',key = 4)
          if st.button('Next',key = 4):
            a6 = number_input('Enter',key = 5)
            if st.button('Next',key = 5):
              a7 = number_input('Enter',key = 6)
      
    

op = model.predict([[a1,a2,a3,a4,a5,a6,a7]])
if st.button('SUBMIT!'):
  st.title(str(op[0]*100) + '%')
      
