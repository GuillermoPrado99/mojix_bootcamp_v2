import streamlit as st
import pandas as pd

st.title('Stock / Inventory Discrepancy')

st.header('Presenting the Expected / Counted Databases')

st.subheader('Expected')
df_expected = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Expected.csv", encoding="latin-1", dtype=str)
st.dataframe(df_expected)

st.subheader('Counted')
df_counted = pd.read_csv("https://storage.googleapis.com/mojix-devops-wildfire-bucket/analytics/bootcamp_2_0/Bootcamp_DataAnalysis_Counted.csv", encoding="latin-1", dtype=str)
st.dataframe(df_counted)

st.markdown("---")

st.header('Plotting Expected / Counted Products')

df1 = df_expected['Retail_Product_Level1Name'].value_counts()
st.bar_chart(df1)

st.markdown("---")

st.caption('by Guillermo Prado')
