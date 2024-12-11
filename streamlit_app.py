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
  # category_names = {1: "Low", 2: "High", 3: "Very High"}
  # df["Category Name"] = df["RANK"].map(category_names)

  # fig, ax = plt.subplots()
  # categories = df["Category Name"].unique()
  # colors = plt.cm.get_cmap("tab10", len(categories))

  # for i, category in enumerate(categories):
  #     cat_data = df[df["Category Name"] == category]
  #     ax.scatter(
  #       cat_data["EFF"], 
  #       cat_data["FG_PCT"], 
  #       label=f"{category}", 
  #       color=colors(i),
  #       edgecolor='none',
  #       s=50
  #     )

  # plt.ylim(0, 1.5)
  # # Add labels, title, and legend
  # ax.set_xlabel("Efficiency", fontsize=12)
  # ax.set_ylabel("PPG", fontsize=12)
  # ax.legend(title="MVP Chance", title_fontsize=12, fontsize=10, loc="upper left", frameon=False)

  # st.pyplot(fig)
  
  # st.scatter_chart(data=df, x='YEAR', y='PTS', color="MVP Chance")

  # Define x-axis range
  x_min, x_max = 1990, 2025  # Customize the range as needed
  
  # Create Altair scatter plot
  chart = alt.Chart(df).mark_circle(size=100).encode(
      x=alt.X("YEAR", scale=alt.Scale(domain=[x_min, x_max])),  # Set x-axis range
      y="PTS",
      color=alt.Color("MVP Chance", title="MVP Chance"),  # Custom legend
      tooltip=["YEAR", "PTS", "MVP Chance"]  # Optional: Add tooltips
  ).properties(
      title="Scatter Chart with Custom X-Axis Range"
  )
  
  # Display the chart in Streamlit
  st.altair_chart(chart, use_container_width=True)
