import streamlit as st


st.set_page_config(page_title="Zoo Structure")

st.markdown("""The Zoo has 3 :red[Zones], 'Aquatic','Big Cats','Monkeys'. """)

st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")

st.markdown("""
Each Zone is composed of a number of Enclosures where the Animals live.

The Aquatic Zone has 6 Enclosures, 3 for various Species of Penguins, 1 for Flamingos, 1 for starfish and stingrays which is closed. 

The Big Cats Zone has 5 Enclosures, 1 each for Lions, Tigers, Jaguars, Lynx and Cheetahs which is closed. 

The Monkey Zone has 5 Enclosures for Gorillas, Chimpanzees, Capuchins, Orangutans, and Golden Snub-Nosed Monkeys. """)

st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")

st.markdown("""
The Attributes of each :red[Enclosure] are - 
- Enclosure_ID (unique identifier in the form xx/xxxx where x is a number) , 
- Name (provide the surname of an naturalist related to the animal), 
- WikiURL (a URL to wikipedia or similar about the naturalist) , 
- Zone, 
- Animal,
- Capacity (number of animals it can hold), 
- Current Number (current number of animals), 
- Diet (typical diet). 
- Status Which is open or Closed, and for Closed a random date in the form YYYY-MM-DD within the last 2 years.""")

# Capacity is -  
#             10 of each type of penguin,   
#             15 Flamingoes,   
#             5 Lions,   
#             3 Tigers,   
#             2 Jaguars,   
#             6 Lynx,   
#             3 Gorillas,   
#             8 chimpanzees,   
#             4 capuchins,   
#             5 Orangutans,   
#             6 Golden Snub Nose Monkeys. 
            
st.markdown("""Currently the Zoo is 80% full with Animals, some Enclosures are 100%.full.""")


st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")

st.markdown("""
The Zoo employs :red[Staff]. Roughly 70% of staff are full time, the rest are part time. Each Zone has a dedicated Vet, a Supervisor, and 6 staff. 

The Attributes of each staff member are

- Staff_ID (In the form of a 16 digit string composed of lower case characters and numbers)
- Enclosure_ID (Enclosure they work in)
- Name 
- Role (One of [Vet, Supervisor, Staff])
- FTE (Full time equivalent, 1 if full time, between 0.5 and 0.8 for part time. Vets and Supervisors are always full time)
- Start_time (Morning, Afternoon)""")

st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")

st.markdown("""
The :red[Animals] in the Zoo all live in their nominated enclosure. Each Animal has an identifying ID. The Zoo records the SubSpecies, Age and Gender of the Animal, the date it arrived at the Zoo and its Health. Big Cats and Monkeys have their own names, but Penguins and Flamingos don’t. 

The Attributes of each Animal are 

- Enclosure_ID (The Enclosure the Animal lives in)
- Animal_ID (Id in the form X-nnnn where X is one of [A,F,J,W] and nnnn is a 4 digit number)
- SubSpecies (A more specific value for Species if relevant)
- Name (might be None for some Species)
- Age (Number of Years)
- Gender (One of [Male,Female])
- Arrival_Date (Date in the form YYYY-MM-DD)
- Health_Status (one of [Healthy, Minor Issues, Under Treatment])""")

st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")

st.markdown("""

The Zoo needs to buy Food for the Animals, and Tea and Coffee for the Staff.  
            
There’s a monthly :red[Budget] for the different types of feed. The supply cost for each feed type varies each month,
so :red[Invoices] might be above or below the budget amount.

The Attributes of the Budget are

- Month (In the form YYYY-MM)
- Order Type (One of [Fish, Fruit, Meat, Plants, Coffee, Tea]
- Budget

The Attributes of the Invoices are 

- Order_ID (In the form Zoo-nnnn where nnnn is a 4 digit number)
- Food (One of [Fish, Fruit, Meat, Plants, Coffee, Tea])
- Purchase_Date (Date in the form YYYY-MM)
- Cost """)

st.markdown(":tiger::monkey::gorilla::orangutan::leopard::flamingo::seal:")

st.markdown("""


The Zoo records :red[Visits] to each Enclosure every day, so if a person visits 3 Enclosures 3 records are generated.

The Zoo is open every day of the year except Christmas Day. Weekends and Bank Holidays are typically the busiest times. School holidays, especially during Summer see a higher volume of visitors.Some visitors are members, and their membership number is recorded for the visit.

""")