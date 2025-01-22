import streamlit as st
import pandas as pd

st.set_page_config(page_title="Coffee Break :coffee:")

# ------------------------------------------------------------------------------------
data = [{'Description':"Simon & Garfunkel - It's all happening at the Zoo",'Link':'https://www.youtube.com/watch?v=6xKLBne1CoI'},
        {'Description':'Edinburgh Zoo Penguin inspects the Norweigian Army','Link':'https://www.youtube.com/watch?v=Hq-6wUWffkA'},
        {'Description': 'Golden Snub Nose Monkeys eating bananas','Link':'https://www.youtube.com/watch?v=8FaB1gohPZI'},
        {'Description':'Orangutans at Paignton Zoo','Link':'https://www.youtube.com/watch?v=Q0LNWU5T4Os'},
        {'Description':'BBC and Open University - Ethics of Zoos','Link':'https://www.youtube.com/watch?v=aQDYxTCIVRE'}]

df_videos = pd.DataFrame(data)

df_videos["Link"] = df_videos["Link"].apply(lambda x: f'<a href="{x}" target="_blank">{x}</a>')
html_table = df_videos.to_html(escape=False, index=False)

# Combine style and table
# styled_html = f"{html_style}<div class='small-font'>{html_table}</div>"

# Display the styled DataFrame in Streamlit

st.subheader('Some light relief :coffee: :tea: :cookie:')

st.markdown(html_table, unsafe_allow_html=True)
