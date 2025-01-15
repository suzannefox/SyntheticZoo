import streamlit as st
# import streamlit.components.v1 as components
import plotly.graph_objects as go
import base64

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
        x=[1.0, 2.5, 3.0, 6.0, 8.0],
        y=[9.0, 8.5, 7.5, 9.0, 7.5],
        mode='markers',  # Include text in the mode
        text=["Darwin Enclosure, Penguins",
              "Penguins",
              "Penguins",
              "Starfish (Closed)",
              "Flamingoes"],  # Custom text for each point
        textposition="top center",  # Position of the text relative to the marker
        hoverinfo="text",  # Only show the custom text in the hover tooltip
        marker=dict(size=10, 
                    color=["blue", "blue", "blue", "red", "blue"]
        )
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
        opacity=0.7,       # Semi-transparent
        layer="below"      # Background image
    )
)

fig.update_layout(
    xaxis=dict(
        range=[0, 10],
        title="",
        #showgrid=False,       # Remove grid lines
        zeroline=False,       # Remove zero line
        showticklabels=False, # Remove tick labels
        ticks='',             # Remove tick marks
    ),
    yaxis=dict(
        range=[0, 10],
        title="",
        #showgrid=False,       # Remove grid lines
        zeroline=False,       # Remove zero line
        showticklabels=False, # Remove tick labels
        ticks='',             # Remove tick marks
    ),
    height=700,  # Height of the graph
    width=700,   # Width of the graph (equal to height for square)
    title="Zoo Enclosures"
)

# Link x and y axes scales
fig.update_layout(
    yaxis_scaleanchor="x"  # Link the y-axis scale to the x-axis scale
)

# Render the Plotly figure in Streamlit
st.plotly_chart(fig, use_container_width=True)
