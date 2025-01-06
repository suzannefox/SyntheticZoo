import streamlit as st
import time
import numpy as np
import pandas as pd

import plotly.graph_objects as go
import base64

st.set_page_config(page_title="Staff")

# ------------------------------------------------------------------------------------

df_Staff = pd.read_csv('./data/Zoo-Staff.csv')
df_Staff['Staff'] = ""

for i, row in df_Staff.iterrows():
    info = f"{row['Name']} ({row['FTE']})"
    df_Staff.loc[i, 'Staff'] = info

df_Central = df_Staff[df_Staff['Enclosure_ID'].isnull()][['Zone','Name','Role']]
df_Central['Staff'] = ""

for i, row in df_Central.iterrows():
    info = f"{row['Name']} ({row['Role']})"
    df_Central.loc[i, 'Staff'] = info

# ---------------------------------------------------------------------------------------

df_Summary = df_Central.groupby(['Zone']).agg({
    'Staff': lambda x: ', '.join(x.astype(str)) })

st.subheader('Vets and Supervisors')
st.write(df_Summary)


df_Summary = df_Staff.groupby(['Enclosure_ID']).agg({
    'FTE': ['sum'], 
    'Staff': lambda x: ', '.join(x.astype(str)) })

st.subheader('Enclosure Staff')
st.write(df_Summary)

