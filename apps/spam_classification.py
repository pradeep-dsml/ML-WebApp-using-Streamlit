import streamlit as st
import joblib

model_path="spam_classification_model.joblib"
def app():
  model=joblib.load(model_path)
  
  text=st.text_input("type your text here")
  
  if st.button("Predict"):
    result=model.predict(text)
    
  if result==0
    st.write("your text is not spam!")
  else
    st.write("your text is spam!")
  # st.success("the text is {}"format(result))
