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
  category_names = {1: "Low", 2: "Medium", 3: "High"}
  df["Category Name"] = df["RANK"].map(category_names)

  fig, ax = plt.subplots()
  categories = df["Category Name"].unique()
  colors = plt.cm.get_cmap("tab10", len(categories))

  for i, category in enumerate(categories):
      cat_data = df[df["RANK"] == category]
      ax.scatter(
        cat_data["YEAR"], 
        cat_data["PTS"], 
        label=f"Category {category}", 
        color=colors(i),
        edgecolor='none',
        s=50
      )

  plt.ylim(0, 50)
  # plt.xlim(1990, 2025)
  # Add labels, title, and legend
  ax.set_xlabel("Year", fontsize=12)
  ax.set_ylabel("PPG", fontsize=12)
  ax.legend(title="MVP Chance", title_fontsize=12, fontsize=10, loc="upper left", frameon=False)

  st.pyplot(fig)
  # st.scatter_chart(data=df, x='YEAR', y='PTS', color='RANK')
