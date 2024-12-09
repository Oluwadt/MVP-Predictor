import streamlit as st
import pandas as pd

st.title('🏀 NBA MVP Predictor')

st.info("This app predicts the players most likely to win this year's NBA MVP award.")

with st.expander('Data'):
  st.write('**Raw Data**')
  df = pd.read_csv('https://raw.githubusercontent.com/Oluwadt/NBA-MVP-Predictor/refs/heads/main/combined_past_data.csv')
  df

  st.write('**X**')
  X = df.drop(['RANK', 'PLAYER'], axis=1)
  X

  st.write('**y**')
  y = df[['PLAYER', 'RANK']]
  y

with st.expander('Data Visualization'):
  st.scatter_chart(data=df, x='YEAR', y='PTS', color='RANK')
