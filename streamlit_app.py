import streamlit as st
import pickle

@st.cache_resource
def load_model():
    return pickle.load(open('insurance_model.pkl','rb'))




st.title("Insurance Predictor App")
st.write("This app will predict the probabilty of a person taking insurance from age")
cont = st.container(border=True)
age = cont.slider(label="Select Age",min_value=1,max_value=120)
print(age)
clicked = st.button(label='Predict')
if clicked:
    model = load_model()
    ins = model.predict([[age]])
    cont2 = st.container(border=True)
    if ins[0]==0:
        cont2.write('This person is not going to buy insurance')
    if ins[0]==1:
        cont2.write('This person is going to buy insurance')

    
    cont2.write()

