import streamlit as st
import pandas as pd

# ------------------------------------------------------------------------------------
def glimpse(file_name):

    df = pd.read_csv(f'./data/{file_name}')

    st.markdown(f"### {file_name}")
    st.markdown(f"""
    Rows: {df.shape[0]}, Columns: {df.shape[1]}""")

    n = df.shape[0] if df.shape[0] < 5 else 5
    df_random = df.sample(n=n, random_state=42, replace=False)

    out_string = ''
    for col in df_random.columns:
        padded_string = col.ljust(20).replace(" ", "&nbsp;") 
        out_string += f'{padded_string}: {df_random[col].iloc[:4].tolist()}<br>'

    st.markdown(f"""<p style="font-family: 'Courier', monospace; font-size: 12px;">
                    {out_string}
                    </p>""", unsafe_allow_html=True)

# ------------------------------------------------------------------------------------
st.set_page_config(page_title="CSV Structure")

files = ['Zoo-Zones.csv', 'Zoo-Enclosures.csv', 'Zoo-Animals.csv', 'Zoo-Staff.csv', 
         'Zoo-Budgets.csv', 'Zoo-Invoices.csv',
         'Zoo-Calendar.csv', 'Zoo-Visits.csv',]

for file in files:
    glimpse(file)

