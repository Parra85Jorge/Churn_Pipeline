# app.py
import streamlit as st
import requests

# URL de la API de FastAPI
API_URL = "http://127.0.0.1:8000/predict"

# Título de la aplicación
st.title("Predicción de Clase con FastAPI y Streamlit")

# Instrucciones para el usuario
st.write("Ingresa las características del modelo para obtener una predicción")

# Entradas de características del modelo

Age = st.number_input("Edad", min_value=18.0, max_value=100.0, step=1.0, value=30.0)
Gender = st.selectbox("Género", ["Male", "Female"])
Tenure  = st.number_input("Tenure", min_value=1.0, max_value=60.0, step=1.0, value=1.0)
Usage_Frequency = st.number_input("Usage_Frequency", min_value=1.0, max_value=30.0, step=1.0, value=1.0)
Support_Calls = st.number_input("Support_Calls", min_value=0.0, max_value=10.0, step=1.0, value=1.0)
Payment_Delay = st.number_input("Payment_Delay", min_value=0.0, max_value=30.0, step=1.0, value=1.0)
Subscription_Type = st.selectbox("Subscription_Type", ["Standard", "Basic", "Premium"])
Contract_Length = st.selectbox("Contract_Length", ["Annual", "Quarterly", "Monthly"])
Total_Spend = st.number_input("Total_Spend", min_value=100.0, max_value=1000.0, step=1.0, value=100.0)
Last_Interaction = st.number_input("Last_Interaction", min_value=0.0, max_value=30.0, step=1.0, value=1.0)

# Botón para realizar la predicción
if st.button("Predecir"):
    # Crear el payload de datos para enviar a la API
    payload = {
        'Age': Age, 
        'Gender': Gender, 
        'Tenure': Tenure, 
        'Usage_Frequency': Usage_Frequency, 
        'Support_Calls': Support_Calls,
        'Payment_Delay': Payment_Delay, 
        'Subscription_Type': Subscription_Type, 
        'Contract_Length': Contract_Length,
        'Total_Spend': Total_Spend, 
        'Last_Interaction': Last_Interaction
    }
    
    try:
        # Realizar la solicitud POST a la API
        response = requests.post(API_URL, json=payload)
        print(payload)
        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            prediction = response.json()["predicted_class"]
            st.success(f"Predicción de Clase: {prediction}")
        else:
            st.error("Error en la predicción. Revisa los datos de entrada y vuelve a intentarlo.")
    except requests.exceptions.RequestException:
        st.error("Error al conectar con la API. Asegúrate de que está corriendo.")
