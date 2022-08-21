import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

fig1 = plt.figure(figsize = (10, 4))
sns.countplot(x = 'Retail_Product_Level1Name', data = df_expected)
st.pyplot(fig1)

fig2 = plt.figure(figsize = (10, 4))
sns.countplot(x = 'Retail_Product_Level1Name', data = df_counted)
st.pyplot(fig2)

st.markdown("---")

st.caption('by Guillermo Prado')
