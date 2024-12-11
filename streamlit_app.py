import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt

st.title('🏀 NBA MVP Predictor')

st.info("This app predicts the players most likely to win this year's NBA MVP award based on past data.")

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
  category_labels = {1: "Low", 2: "High", 3: "Very High"}
  df["MVP Chance"] = df["RANK"].map(category_labels)
  
  # Define x-axis range
  x_min, x_max = 1990, 2025  # Customize the range as needed
  
  # Create Altair scatter plot
  chart = alt.Chart(df).mark_circle(size=100).encode(
      x=alt.X("YEAR", scale=alt.Scale(domain=[x_min, x_max])),  # Set x-axis range
      y="PTS",
      color=alt.Color("MVP Chance", title="MVP Chance"),  # Custom legend
      tooltip=["YEAR", "PTS", "MVP Chance"]  # Optional: Add tooltips
  )
  
  # Display the chart in Streamlit
  st.altair_chart(chart, use_container_width=True)

with st.sidebar:
  st.header("Stats")
  ppg = st.slider("Points Per Game", 0, 15, 100)
  ast = st.slider("Assists Per Game", 0, 4, 40)
  oreb = st.slider("Offensive Rebounds Per Game", 0, 4, 30)
  dreb = st.slider("Defensive Rebounds Per Game", 0, 4, 30)
