
# PROYECTO DE CONSOLIDACION STREAMLIT: FUNCION eda_app.py

# Importaciones: streamlit, pandas, matplotlib, seaborn
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Función principal que emplearemos en la APP
def run_eda_app():

	# Todo el código a escribir va aquí
  submenu = ["Descriptivo", "Gráfico"]
  opcion= st.sidebar.selectbox("SubMenu", submenu)
  
  st.title("Sección EDA")
 
  
   #Carga dataframe
  df = pd.read_csv("data/diabetes_data_upload.csv")
  df_clean = pd.read_csv("data/diabetes_data_upload_clean.csv")
  
  if(opcion=="Descriptivo"):
      st.subheader("Análisis Descriptivo")
      st.dataframe(df.head())
      
      with st.expander("Tipos de datos"):
          st.dataframe(df.dtypes)
      with st.expander("Resumen descriptivo"): 
          st.dataframe(df_clean.describe())
      with st.expander("Distribución por género (Gender)"):
          st.dataframe(df.value_counts('Gender').astype(str))
      with st.expander("Distribución por clase/label (Class)"): 
          st.dataframe(df.value_counts('class').astype(str))
          
  elif("Gráfico"): 
      st.subheader("Análisis Gráfico") 
      col1, col2 = st.columns(2) 
          
      with col1:
        #st.caption("Gráfico distribuido por género (Gender)")
        with st.expander("Gráfico distribuido por género (Gender)"): 
            fig=plt.figure() 
            df['Gender'].value_counts().plot(kind='pie') 
            st.pyplot(fig)
        with st.expander("Gráfico distribuido por clase (Class)"): 
            fig2=plt.figure()
            df['class'].value_counts().plot(kind='pie')
            st.pyplot(fig2)
        
      with col2: 
          with st.expander("Gender Distribution"): 
              st.dataframe(df.value_counts('Gender').astype(str))
          with st.expander("Class Distribution"): 
            st.dataframe(df.value_counts('class').astype(str))
	
      with st.expander("Distribución por edades (Ages)"): 
          df_ages = pd.read_csv("data/freqdist_of_age_data.csv")
          fig3 = plt.figure()
          sns.barplot(data=df_ages, x='Age', y='count')
          st.pyplot(fig3)
          
      with st.expander("Detección de Outliers"): 
          fig4 = plt.figure()
          sns.boxplot(data=df_clean, x="gender", y="age")
          st.pyplot(fig4)
          
      with st.expander("Gráfico de Correlación"): 
          fig5 = plt.figure()
          sns.heatmap(data=df_clean.corr())
          st.pyplot(fig5)
          #Con Plotly
          #fig6 = px.pie(df_clean.corr())
          #fig6.show()
          
# Fin de la FUNCION







