import html
import streamlit as st
import pandas as pd

df_Enclosures = pd.read_csv('./data/Zoo-Enclosures.csv')
df_Animals = pd.read_csv('./data/Zoo-Animals.csv')

df_enc = df_Enclosures[['Enclosure_ID', 'Name', 'Zone', 'Animal']]
df_enc.columns = ['Enclosure_ID', 'Enclosure_Name', 'Zone', 'Animal']
df_animals = pd.merge(df_enc, df_Animals,  on='Enclosure_ID', how='outer').reset_index(drop=True)
df_animals['Enclosure'] = df_animals.apply(lambda row: f"{row['Enclosure_ID']} ({row['Enclosure_Name']})", axis=1)

list_images = [{'Enclosure_ID': '01/0001', 'pic':'./images/Penguin_Emperor.jpg'},
               {'Enclosure_ID': '01/0002', 'pic':'./images/Penguin_Gentoo.jpg'},
               {'Enclosure_ID': '01/0003', 'pic':'./images/Penguin_Humbolt.jpg'},
               {'Enclosure_ID': '01/0004', 'pic':'./images/Flamingo.jpg'},
               {'Enclosure_ID': '02/0006', 'pic':'./images/Lions.jpg'},
               {'Enclosure_ID': '02/0007', 'pic':'./images/Tigers.jpg'},
               {'Enclosure_ID': '02/0008', 'pic':'./images/Jaguar.jpg'},
               {'Enclosure_ID': '02/0009', 'pic':'./images/Lynx.jpg'},
               {'Enclosure_ID': '03/0011', 'pic':'./images/Gorillas.jpg'},
               {'Enclosure_ID': '03/0012', 'pic':'./images/Chimpanzee.jpg'},
               {'Enclosure_ID': '03/0013', 'pic':'./images/Capuchin.jpg'},
               {'Enclosure_ID': '03/0014', 'pic':'./images/Orangutan.jpg'},
               {'Enclosure_ID': '03/0015', 'pic':'./images/Golden.jpg'},]

df_images = pd.DataFrame(list_images)
df_animals = pd.merge(df_animals, df_images, on='Enclosure_ID', how='left')

df_summary = df_animals.groupby(['Enclosure','pic' ,'Animal', 'SubSpecies']).agg(
    Number = ('Enclosure', 'size'),
    # Names=('Name', lambda x: [v for v in x if pd.notna(v)])
    Names=('Name', lambda x: ', '.join(str(v) for v in x if pd.notna(v)))
).reset_index()

# ------------------------------------------------------------------------------------
st.set_page_config(page_title="Meet The Animals")
st.subheader('These are the Animals living in each Enclosure')
st.markdown("""Penguins and Flamingos don't have their own names
               There's a lot of confusion caused by other animals often having the same names""")

def render_dataframe_with_images(df):
    col1, col2, col3 = st.columns([1, 1, 1])
    for _, row in df.iterrows():
        if _ in [0, 3, 6, 9,12,15]: colx = col1
        if _ in [1, 4, 7,10,13,16]: colx = col2
        if _ in [2, 5, 8,11,14,17]: colx = col3

        with colx:
            st.image(row["pic"], width=100)
            text = ''

            if row['Animal'] == 'Penguins':
                text = f'{row["Enclosure"]} is home to {row["Number"]} {row["SubSpecies"]}s, '
            else:
                text = f'{row["Enclosure"]} is home to {row["Number"]} {row["Animal"]}, '

            if row['Animal'] == 'Penguins':
                text += "the penguins don't have names."
            elif row['Animal'] == 'Flamingos':
                text += "the flamingoes don't have names."
            else:
                text += f"Their names are {row['Names']}."
            st.write(text)

render_dataframe_with_images(df_summary)

#html_summary = df_summary.to_html(index=False, escape=False)
#st.markdown(html_summary, unsafe_allow_html=True)

# ------------------------------------------------------------------------------------
st.subheader('Animal List')
df_Animals['Name'] = df_Animals['Name'].apply(lambda x: '' if pd.isna(x) else x)
html_animals = df_Animals.to_html(index=False, escape=False)
st.markdown(html_animals, unsafe_allow_html=True)
