import streamlit as st
import time
import numpy as np
import pandas as pd

df_Enclosures = pd.read_csv('./data/Zoo-Enclosures.csv')

st.set_page_config(page_title="Enclosures")

st.subheader('Zone information')
df_Summary = df_Enclosures[df_Enclosures['Status'] == 'Open'].groupby('Zone').agg({
    'Enclosure_ID': 'nunique',
    'Animal': lambda x: ', '.join(x.astype(str)),
    'Current_Number': 'sum'
})
df_Summary.columns = ["Enclosures","Animals","Number"]
st.write(df_Summary)

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
