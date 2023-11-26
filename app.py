import streamlit as st
import numpy as np
import pickle 
from sklearn.metrics import accuracy_score

st.title('Diabetes Prediction')

loaded_model = pickle.load(open('Diabetesmodel.pkl', 'rb'))

def disease(input_data):
    input_data_arr = np.asarray(input_data)
    input_data_reshape = input_data_arr.reshape(1, -1)

    prediction = loaded_model.predict(input_data_reshape)

    if (prediction[0] == 0):
        return st.success('The person has diabetes')
    else:
        return st.error('The person has diabetes')

def main():
    st.write('Prediction model')

    BMI = st.number_input('Enter BMI (Body Mass Index)')
    Insulin = st.number_input('Enter Insulin', step=2)
    Glucose = st.number_input('Enter Glucose', step=2)
    Age = st.number_input('Enter Age', step=2)

    diagnosis = ''

    if st.button('Predict'):
        diagnosis = disease([Glucose, Insulin, BMI, Age])

if __name__ == '__main__':
    main()