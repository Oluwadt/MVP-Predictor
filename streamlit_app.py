import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
  fig, ax = plt.subplots()
  categories = df["RANK"].unique()
  colors = plt.cm.get_cmap("tab10", len(categories))  # Generate a colormap

  for i, category in enumerate(categories):
      cat_data = df[df["RANK"] == category]
      ax.scatter(cat_data["YEAR"], cat_data["PTS"], label=f"Category {category}", color=colors(i))
  
  # Add labels, title, and legend
  ax.set_xlabel("Year")
  ax.set_ylabel("PPG")
  ax.legend(title="Category")

  st.pyplot(fig)
  # st.scatter_chart(data=df, x='YEAR', y='PTS', color='RANK')
