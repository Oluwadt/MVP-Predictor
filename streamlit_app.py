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
  year = st.selectbox("Year", list(range(1991, 2026)))
  year_players = df[df["YEAR"] == year]['PLAYER'].values
  player = st.selectbox("Player", year_players)
  
  mask_player = df["PLAYER"] == player
  mask_year = df["YEAR"] == year
  player_df = df[mask_player & mask_year]
  
  # ppg = st.slider("Points Per Game", 0.0, 15.5, 100.0)
  # ast = st.slider("Assists Per Game", 0.0, 4.5, 40.0)
  # oreb = st.slider("Offensive Rebounds Per Game", 0.0, 4.5, 40.0)
  # dreb = st.slider("Defensive Rebounds Per Game", 0.0, 4.5, 40.0)

  # input_data = {
  #   'PPG': ppg,
  #   'AST': ast,
  #   'OREB': oreb,
  #   'DREB': dreb
  # }
  # input_df = pd.DataFrame(input_data, index=[0])
player_df
st.markdown(f"""
<div style="padding: 1.5rem; background-color: #f9fbfc; border-radius: 0.5rem; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);">
    <h3 style="margin: 0; color: #4CAF50;">{player_df['PLAYER'].values[0]} Year: {player_df['YEAR']}</h3>
    <p style="margin: 0.5rem 0 0; color: #333;">PPG: {player_df['PTS']} APG: {player_df['AST']} RPG: {player_df['REB']}
    BLK: {player_df['BLK']} STL: {player_df['STL']} TOV: {player_df['TOV']}</p>
</div>
""", unsafe_allow_html=True)
