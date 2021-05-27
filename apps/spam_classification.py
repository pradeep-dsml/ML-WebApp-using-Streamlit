
import streamlit as st
import joblib

def app():
  st.title("this is spam classification app")
  model_path="https://github.com/pradeep-dsml/ML-WebApp-using-Streamlit/blob/main/apps/spam_classification_model.joblib"
  model=joblib.load(model_path)
  
  text=st.text_input("type your text here")
  
  if st.button("Predict"):
    result=model.predict(text)
    
  st.success("your text is {}".format(result))
  
  """
    if result == "0"
      st.write("your text is not spam!")
    else
      st.write("your text is spam!")
  # st.success("the text is {}"format(result))
    
  """
