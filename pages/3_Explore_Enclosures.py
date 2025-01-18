import streamlit as st
import time
import numpy as np
import pandas as pd

import plotly.graph_objects as go
import base64

st.set_page_config(page_title="Enclosures")

# ------------------------------------------------------------------------------------

df_Enclosures = pd.read_csv('./data/Zoo-Enclosures.csv')
dict_enc_coords = [{'Enclosure_ID':'01/0001', 'x':1.0, 'y':9.0},
                   {'Enclosure_ID':'01/0002', 'x':2.5, 'y':8.5},
                   {'Enclosure_ID':'01/0003', 'x':3.0, 'y':7.5},
                   {'Enclosure_ID':'01/0004', 'x':6.0, 'y':9.0},
                   {'Enclosure_ID':'01/0005', 'x':8.0, 'y':7.5},

                   {'Enclosure_ID':'02/0006', 'x':1.2, 'y':7.5},
                   {'Enclosure_ID':'02/0007', 'x':3.7, 'y':5.8},
                   {'Enclosure_ID':'02/0008', 'x':0.7, 'y':5.5},
                   {'Enclosure_ID':'02/0009', 'x':3.2, 'y':4.0},
                   {'Enclosure_ID':'02/0010', 'x':6.0, 'y':3.0},

                   {'Enclosure_ID':'03/0011', 'x':2.5, 'y':2.5},
                   {'Enclosure_ID':'03/0012', 'x':3.5, 'y':2.7},
                   {'Enclosure_ID':'03/0013', 'x':3.2, 'y':1.2},
                   {'Enclosure_ID':'03/0014', 'x':7.5, 'y':1.5},
                   {'Enclosure_ID':'03/0015', 'x':8.7, 'y':2.0}]

df_Coord = pd.DataFrame(dict_enc_coords)

df_Enclosures = pd.merge(df_Enclosures, df_Coord, on='Enclosure_ID', how='outer')
df_Enclosures['Colour'] = df_Enclosures['Closed_Date'].apply(lambda x: 'Blue' if pd.isna(x) else 'Red')
# df_Enclosures['Text'] = df_Enclosures.apply(lambda row: f"{row['Name']} ({row['Enclosure_ID']}) home for {row['Animal']}\
#                                             {', ' + row['Status'] if row['Status'] == 'Closed' else ''}", axis=1)

df_Enclosures['Text'] = df_Enclosures.apply(lambda row: "".join([
                                            f"{row['Name']} ({row['Enclosure_ID']}) home for {row['Animal']}",
                                            f"{', CLOSED on ' + row['Closed_Date'] if row['Status'] == 'Closed' else ''}"
                                        ]), axis=1)

list_x = df_Enclosures['x'].tolist()
list_y = df_Enclosures['y'].tolist()
list_text = df_Enclosures['Text'].tolist()
list_colour = df_Enclosures['Colour'].tolist()

st.subheader('Zone information')
df_Summary = df_Enclosures[df_Enclosures['Status'] == 'Open'].groupby('Zone').agg({
    'Enclosure_ID': 'nunique',
    'Animal': lambda x: ', '.join(x.astype(str)),
    'Current_Number': 'sum'
})
df_Summary.columns = ["Enclosures","Animals","Number"]
st.write(df_Summary)

# --------------------------------------------------------------------------------------

# Function to encode an image in base64
def encode_image(image_path):
    with open(image_path, "rb") as f:
        return "data:image/png;base64," + base64.b64encode(f.read()).decode()

# Encode the local image
image_path = "./images/Zoo-Map.jpg"  # Replace with your 1024x1024 image path
encoded_image = encode_image(image_path)

# Initialize the figure
fig = go.Figure()

# Add scatter plot trace

fig.add_trace(
    go.Scatter(
        x=list_x,
        y=list_y,
        mode='markers',  # Include text in the mode
        text = list_text,
        textposition="top center",  # Position of the text relative to the marker
        hoverinfo="text",  # Only show the custom text in the hover tooltip
        marker=dict(size=20, 
                    line=dict(width=5,color='White'), 
                    symbol='star-open',
                    color=list_colour,
                    opacity=0.8)
    )
)

fig.add_layout_image(
    dict(
        source=encoded_image,  # Image URL
        xref="x",  # Reference to x-axis
        yref="y",  # Reference to y-axis
        x=0,       # x-coordinate for the image's top-left corner
        y=10,       # y-coordinate for the image's top-left corner
        sizex=10,   # Width of the image
        sizey=10,   # Height of the image
        sizing="contain",  # Preserve aspect ratio within sizex and sizey
        opacity=0.8,       # Semi-transparent
        layer="below"      # Background image
    )
)

fig.update_layout(
    xaxis=dict(
        range=[0, 10],
        title="",
        showgrid=False,       # Remove grid lines
        zeroline=False,       # Remove zero line
        showticklabels=False, # Remove tick labels
        ticks='',             # Remove tick marks
    ),
    yaxis=dict(
        range=[0, 10],
        title="",
        showgrid=False,       # Remove grid lines
        zeroline=False,       # Remove zero line
        showticklabels=False, # Remove tick labels
        ticks='',             # Remove tick marks
    ),
    height=600,  # Height of the graph
    width=600,   # Width of the graph (equal to height for square)
    margin=dict(
    l=0,   # Left margin
    r=100, # Right margin (increase to push plot left)
    t=0,  # Top margin
    b=0   # Bottom margin
    )
)

# Link x and y axes scales
fig.update_layout(
    yaxis_scaleanchor="x"  # Link the y-axis scale to the x-axis scale
)

# Inject custom CSS to reduce the whitespace between components
st.markdown("""
    <style>
        /* Reduce space between subheader and chart */
        .stSubheader {
            margin-bottom: 0.1rem; /* Adjust this to your desired spacing */
        }
        .stPlotlyChart {
            margin-top: -10px; /* Adjust this to decrease the gap further */
        }
    </style>
""", unsafe_allow_html=True)

config = {'displayModeBar': False}
# Render the Plotly figure in Streamlit
st.subheader('Enclosure Locations')
st.markdown("""Hover over the markers to see the enclosure details.""")
st.plotly_chart(fig, use_container_width=True, config=config)

# --------------------------------------------------------------------------------------
# Create HTML for the DataFrame with smaller font size

html_style = """
<style>
.small-font {
    font-size: 12px; /* Adjust size as needed */
    text-align: left; /* Align column headers to the left */
}
table th {
    text-align: left; /* Align column headers to the left */
}
table td {
    text-align: left; /* Align data cells to the left */
}
table thead th {
    text-align: left; /* Align column headers to the left */
}
</style>
"""
# --------------------------------------------------------------------------------------
for zone in ['Aquatic', 'Big Cats', 'Monkeys']:

    st.subheader(f'{zone} Zone')
    df_Zone = df_Enclosures[df_Enclosures['Zone'] == zone][['Enclosure_ID','Name','Animal','Status','WikiURL']]
    df_Zone["WikiURL"] = df_Zone["WikiURL"].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
    #df_Zone.columns = ['ID','Name','Animal','Status','Naturalist Background']

    html_table = df_Zone.to_html(escape=False, index=False)

    # Combine style and table
    styled_html = f"{html_style}<div class='small-font'>{html_table}</div>"

    # Display the styled DataFrame in Streamlit
    st.markdown(styled_html, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------
