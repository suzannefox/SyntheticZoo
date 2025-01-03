import streamlit as st
import pandas as pd
import plotly.express as px
import datetime
from datetime import timedelta

df_Calendar = pd.read_csv('./data/Zoo-Calendar.csv')

st.set_page_config(page_title="Daily Visits During 2024")

# Create an interactive line chart
fig = px.line(df_Calendar, x="date", y="visits", title="Visits Over the Year 2024",
              labels={"date": "Date", "visits": "Number Of Visits", "weekend": "Weekend"},
              hover_data={"weekend": True} )
    
# fig.update_layout(
#     xaxis_title="Date",
#     yaxis_title="Visits",
#     template="plotly_white",  # Optional: cleaner template
#     xaxis=dict(rangeslider=dict(visible=True))  # Enable range slider
# )

# # Mark Bank Holidays
# for date in df_Calendar[df_Calendar["type"] != 'Normal Day']["date"]:

#     date1 = datetime.datetime.strptime(date, '%Y-%m-%d')
#     date2 = date1 + timedelta(days=1)
#     date2 = date2.strftime("%Y-%m-%d")
    
#     fig.add_vrect(
#         x0=date,
#         x1=date2,
#         label=dict(
#             text="Bank Holiday",
#             textposition="top center",
#         ),
#         fillcolor="green",
#         opacity=0.25,
#         line_width=0,
#     )

# # Customize the range slider with a light grey background
# fig.update_layout(
#     template="plotly_white",
#     xaxis=dict(
#         title="Date Range Slider",
#         rangeslider=dict(
#             visible=True,         # Enable the range slider
#             bgcolor="lightgrey",  # Set the background color of the slider
#         ),
#     ),
#     yaxis=dict(title="Number of Visits"),
# )

st.plotly_chart(fig, use_container_width=True)