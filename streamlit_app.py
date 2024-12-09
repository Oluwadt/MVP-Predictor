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
  c = (
   alt.Chart(df)
   .mark_circle()
   .encode(x="MIN", y="PTS", size="RANK", color="RANK", tooltip=["1", "2", "3"])
)

st.altair_chart(c, use_container_width=True)
  # st.scatter_chart(data=df, x='MIN', y='PTS', color='RANK')
