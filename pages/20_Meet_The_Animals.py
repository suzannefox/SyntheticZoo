import streamlit as st
import pandas as pd

st.set_page_config(page_title="Meet The Animals")

st.markdown("""The Zoo has 3 :red[Zones], 'Aquatic','Big Cats','Monkeys'. """)
st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")
st.markdown("""
Each Zone is composed of a number of Enclosures where the Animals live.
The Aquatic Zone has 6 Enclosures, 3 for various Species of Penguins, 1 for Flamingos, 1 for starfish and stingrays which is closed. 
The Big Cats Zone has 5 Enclosures, 1 each for Lions, Tigers, Jaguars, Lynx and Cheetahs which is closed. 
The Monkey Zone has 5 Enclosures for Gorillas, Chimpanzees, Capuchins, Orangutans, and Golden Snub-Nosed Monkeys. """)

# DataFrame.applymap has been deprecated. Use DataFrame.map instead.