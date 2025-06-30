import pandas as pd
import streamlit as st
import plotly.express as px

df=pd.read_csv('New Data.csv')
st.set_page_config(layout='wide',
                  page_title='Home Page',
                  page_icon='🪙')

st.sidebar.success('select page above')
st.markdown('<h1 style= "text-align:center; color: cyan ;">Home Page for Dashboard</h1>', unsafe_allow_html= True)

col1, col2, col3=st.columns([3,3,3])

with col2:
    
    st.markdown('<h3 style="text-align: center; color : MediumAquaMarine;">Dataset</h3>', unsafe_allow_html=True)
    st.dataframe(df.head(200), 800, 800)
