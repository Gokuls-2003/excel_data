import streamlit as st
import pandas as pd
#import plotly.express as px

st.set_page_config(page_title = 'Excel plotter')
st.title('Excel plotter📈')
st.subheader('Feed me with your Excel file')

uploaded_file = st.file_uploader('Choose a XLSX file', type='xlsx')
if uploaded_file:
    st.markdown('----')
    df = pd.read_excel(uploaded_file, engine='openpyxl')
    st.dataframe(df)
    x_column = st.selectbox('Selecgitt X-axis Column:', df.columns)
    y_column = st.selectbox('Select Y-axis Column:', df.columns)
    fig = px.bar(df, x=x_column, y=y_column, template='plotly_dark')
    st.plotly_chart(fig)
    
    
    
    
    
