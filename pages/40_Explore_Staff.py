import streamlit as st
import time
import numpy as np
import pandas as pd

import plotly.graph_objects as go
import base64

st.set_page_config(page_title="Staff")

# ------------------------------------------------------------------------------------

# get staff
df_Staff = pd.read_csv('./data/Zoo-Staff.csv')
df_Staff['Staff'] = ""

# get enclosures
df_Enclosures = pd.read_csv('./data/Zoo-Enclosures.csv')
df_Enc = df_Enclosures[['Enclosure_ID','Name']]
df_Enc = df_Enc.reset_index()

# make a var for staff and their FTE
for i, row in df_Staff.iterrows():
    info = f"{row['Name']} ({row['FTE']})"
    df_Staff.loc[i, 'Staff'] = info

# ---------------------------------------------------------------------------------------
# Zone Vets and Supervisors

df_Central = df_Staff[df_Staff['Enclosure_ID'].isnull()][['Zone','Name','Role']]
df_Central['Staff'] = ""

for i, row in df_Central.iterrows():
    info = f"{row['Name']} ({row['Role']})"
    df_Central.loc[i, 'Staff'] = info

df_Summary = df_Central.groupby(['Zone']).agg({
    'Staff': lambda x: ', '.join(x.astype(str)) })

st.subheader('Vets and Supervisors')
st.write(df_Summary)

# ---------------------------------------------------------------------------------------
# Enclosure Staff

df_Summary = df_Staff.groupby(['Enclosure_ID']).agg(
    Total_FTE = ('FTE', 'sum'), 
    Staff_List=('Staff', lambda x: ', '.join(x.astype(str))))

df_Display = pd.merge(df_Summary, df_Enc, on='Enclosure_ID', how='left')

df_Display['Enclosure'] = ''
for i, row in df_Display.iterrows():
    info = f"{row['Enclosure_ID']} ({row['Name']})"
    df_Display.loc[i, 'Enclosure'] = info

df_Display = df_Display[['Enclosure','Total_FTE','Staff_List']]
df_Display = df_Display.reset_index(drop=True)

st.subheader('Enclosure Staff')
# st.dataframe(df_Display.style.hide(axis="index"))
st.write(df_Display.to_html(index=False), unsafe_allow_html=True)

# ---------------------------------------------------------------------------------------

# Compute 'Text' column using lambda and apply
y = df_Enclosures[['Enclosure_ID','Zone','Name']]
y.columns = ['Enclosure_ID','Zoney','Namey']
df_Staff = pd.merge(df_Staff, y, on='Enclosure_ID', how='outer')

df_Staff['myZone'] = df_Staff.apply(lambda row: row['Zone'] if pd.isna(row['Enclosure_ID']) else row['Zoney'], axis=1)
df_Staff['Text'] = df_Staff.apply(lambda row: f"{row['Name']} ({row['Role']}) in the {row['myZone']} Zone", axis=1)

df_StaffList = df_Staff[['Staff_ID','FTE','Start_time','Text']]

st.subheader('All Staff List')
# st.dataframe(df_Display.style.hide(axis="index"))
st.write(df_StaffList.to_html(index=False), unsafe_allow_html=True)
