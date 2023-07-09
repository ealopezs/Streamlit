
#  PROYECTO CONSOLIDACION STREAMLIT: FUNCION app.py

# Importaciones
import streamlit as st
import streamlit.components.v1 as stc
from eda_app import run_eda_app
from ml_app import run_ml_app

# Función main()
def main():
    
    menu = ["Home", "EDA", "ML", "Info"]
    opcion= st.sidebar.selectbox("Menú", menu)
    
    if(opcion=="Home"):
        stc.html("<p style='background-color:blue;color:white; text-align:center'> App para la detección de DM (Diabtes Mellitus) </p>", height=100)
        st.subheader("Home")
        st.text("Dataet que contiene señales y síntomas que pueden indicar diabetes o posiblidad de diabetes.")
        
        st.subheader("Fuentes de datos")
        st.code("https://statics.teams.cdn.office.net/evergreen-assets/safelinks/1/atp-safelinks.html")
        
        st.subheader("Contenidos de la App")
        lst = ['EDA Section: Análisis exploratorio de los datos', 
               'ML Section: Predicción de Diabetes basada en ML (Machine Learning)']
        for i in lst:
            st.markdown("- " + i)
        
    elif(opcion=="EDA"):
     run_eda_app() 
    elif(opcion=="ML"):
     run_ml_app()
    elif(opcion=="Info"):
        st.subheader("Info")
        st.text("MBIT, Proyecto de Consolidación - librería Streamlit.")
        stc.iframe("https://www.xataka.com/")


if __name__ == '__main__':
	main()