from venv import create
import pandas as pd
import random
import string
import datetime
from datetime import timedelta
import holidays

def find_duplicates(df, column_name):
    """
    Finds duplicate entries in a specific column of a DataFrame.
    
    Parameters:
        df (pd.DataFrame): The input DataFrame.
        column_name (str): The name of the column to check for duplicates.
    
    Returns:
        pd.DataFrame: A DataFrame containing the duplicate entries and their counts.
    """
    duplicates = df[column_name].value_counts()
    duplicates = duplicates[duplicates > 1].reset_index()
    duplicates.columns = [column_name, 'Count']
    return duplicates

# ----------------------------------------------------------------------------------------
# Function to generate a random Staff_ID
def generate_staff_id():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=16))

# Function to determine FTE based on role
def generate_fte(role):
    if role in ["Vet", "Supervisor"]:
        return 1
    
    rand_dist = round(random.uniform(1, 3), 0)
    if rand_dist < 3:
        return 1
    else:
        return round(random.uniform(0.5, 0.8), 1)

def generate_names():
    # List of synthetic first and last names
    first_names = ["Alex", "Ed", "Sarah", "Louise", "Pearl", "Morgan", "Ellen", "Rosa", "Hunter", "Dakota","Fred","Jo","Chris","Dan"]
    last_names = ["Smith", "Johnson", "Brown", "Taylor", "Anderson", "Thomas", 
                    "Jackson", "White", "Harris", "Martin","Martin","Fletcher","Thatcher","Jones",
                    "Wolfe","Brownlee","Archer","Smythe"]
        
    list_names = []
    for first in first_names:
        for last in last_names:
            list_names.append(f'{first} {last}')

    list_used = [1 for i in range(0,len(list_names))]
    return(list_names, list_used)

def weighted_choice(values, selection_probability, verbose = False):
    filtered_values = [value for value, occ in zip(values, selection_probability) if occ == 1]
    chosen = random.choices(filtered_values)[0]
    index = values.index(chosen)
    selection_probability[index] -= 0.2

    if verbose:
        print(len(list_names))
        print(filtered_values)
        print(len(filtered_values))
        print(chosen, index)
        
    return(chosen)

def generate_animal_id():
    return f"{random.choice(['A','F','J','W'])}-{random.randint(1000, 9999)}"

def generate_animal_name(species):
    # List of possible names for animals
    animal_names = ["Kiki", "Bongo", "Milo", "Bella", "Charlie", "Lola", "Max"]

    if species in ['Penguins','Flamingos']:
        return('None')
    elif species in ['Lions','Lynx','Tigers','Jaguars']:
        animal_names = ["Simba", "Nala", "Scar", "Orion","Tyson","Apollo","Kiara","Leo","Zeus","Fang","Samson","King","Prince","Duke"]
    
    return(random.choice(animal_names))

# Function to generate a random date within the last 10 years
def generate_random_date(age):
    # Calculate the earliest allowable date
    min_date = datetime.datetime.now() - timedelta(days=age * 365)
    # Generate a random date between min_date and today
    start_date = min_date
    end_date = datetime.datetime.now()
    return (start_date + (end_date - start_date) * random.random()).strftime("%Y-%m-%d")

def generate_food():

    items = ['Fish','Fruit','Meat','Plants','Coffee','Tea']
    itembudget = [2300, 750, 3600, 600, 100, 76]

    month = []

    for x in range(1,13):
        month.append(f'2024-{x:02}')

    return(items, itembudget, month)

def is_school_holiday(date):

    # Define school holiday periods
    school_holidays = [
        (datetime.date(2024, 1, 1), datetime.date(2024, 1, 7)), 
        (datetime.date(2024, 3, 29), datetime.date(2024, 4, 12)), 
        (datetime.date(2024, 7, 25), datetime.date(2024, 9, 2)),   
        (datetime.date(2024, 12, 19), datetime.date(2024, 12, 31)),  
    ]

    return any(start <= date <= end for start, end in school_holidays)

def generate_visit_count(current_date, is_weekend, is_bankholiday, is_schoolholiday):

    if current_date == datetime.date(2024, 12, 25):
        return(0)

    # Parameters
    base_weekday_visits = 450  # Base visit rate for a weekday
    weekend_multiplier = 1.85  if is_school_holiday == False else 1.22 # Ensures weekends account for ~70% of visits
    bank_holiday_multiplier = 2.5  # Double visits on bank holidays
    school_holiday_multiplier = 1.4
    summer_multiplier = 1.7  # Double visits during summer
    if current_date.month == 6: summer_multiplier *= 0.65
    if current_date.month == 7: summer_multiplier *= 0.85

    # Determine base rate
    if is_weekend:  # Weekend
        base_rate = base_weekday_visits * weekend_multiplier
    else:  # Weekday
        base_rate = base_weekday_visits
    
    if is_school_holiday:
        base_rate = base_rate * school_holiday_multiplier

    # Adjust for bank holidays
    if is_bankholiday:
        base_rate *= bank_holiday_multiplier
    
    # Adjust for summer
    if current_date.month in [6,7,8]:
        base_rate *= summer_multiplier
    
    # Simulate the number of visits for the day
    daily_visits = int(random.gauss(base_rate, base_rate * 0.1))  # Add some randomness
    return(round(daily_visits,0))

def generate_members():
    memberids = []

    for x in range(0,2246):

        while True:
            memid = 'CL-' + ''.join(random.choices(string.digits, k=8))
            ago = random.uniform(1,3650)
            joined = datetime.datetime.now() - timedelta(ago)
            joined = joined.strftime('%Y-%m-%d')

            if not memid in memberids:
                member = {"Member_ID": memid, "join_date": joined}
                memberids.append(member)
                break
    
    return memberids

def generate_visit_targets():

    visit_Targets = [{'Enclosure_ID':'01/0001','Visits':19000,'MemberVisits':2000},
                    {'Enclosure_ID':'01/0002','Visits':23458,'MemberVisits':2000},
                    {'Enclosure_ID':'01/0003','Visits':21474,'MemberVisits':2000},
                    {'Enclosure_ID':'01/0004','Visits':7500,'MemberVisits':1250},
                    {'Enclosure_ID':'01/0005','Visits':0,'MemberVisits':0},
                    {'Enclosure_ID':'02/0006','Visits':15750,'MemberVisits':1750},
                    {'Enclosure_ID':'02/0007','Visits':19500,'MemberVisits':1875},
                    {'Enclosure_ID':'02/0008','Visits':19250,'MemberVisits':1900},
                    {'Enclosure_ID':'02/0009','Visits':21225,'MemberVisits':2000},
                    {'Enclosure_ID':'02/0010','Visits':0,'MemberVisits':0},
                    {'Enclosure_ID':'03/0011','Visits':9200,'MemberVisits':2100},
                    {'Enclosure_ID':'03/0012','Visits':14000,'MemberVisits':1925},
                    {'Enclosure_ID':'03/0013','Visits':21250,'MemberVisits':1980},
                    {'Enclosure_ID':'03/0014','Visits':14560,'MemberVisits':1280},
                    {'Enclosure_ID':'03/0015','Visits':25500,'MemberVisits':2500}]
    
    return visit_Targets

def generate_static_calendar():
    days_2024 = [
        {'day_of_year': 1, 'date': '2024-01-01', 'day_of_week': 'Monday', 'type': "New Year's Day", 'weekend': False, 'bank_holiday': True, 'school_holiday': True, 'visits': 1566} ,
        {'day_of_year': 2, 'date': '2024-01-02', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 668} ,
        {'day_of_year': 3, 'date': '2024-01-03', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 684} ,
        {'day_of_year': 4, 'date': '2024-01-04', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 582} ,
        {'day_of_year': 5, 'date': '2024-01-05', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 569} ,
        {'day_of_year': 6, 'date': '2024-01-06', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 850} ,
        {'day_of_year': 7, 'date': '2024-01-07', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 709} ,
        {'day_of_year': 8, 'date': '2024-01-08', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 693} ,
        {'day_of_year': 9, 'date': '2024-01-09', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 530} ,
        {'day_of_year': 10, 'date': '2024-01-10', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 573} ,
        {'day_of_year': 11, 'date': '2024-01-11', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 593} ,
        {'day_of_year': 12, 'date': '2024-01-12', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 612} ,
        {'day_of_year': 13, 'date': '2024-01-13', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 831} ,
        {'day_of_year': 14, 'date': '2024-01-14', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 673} ,
        {'day_of_year': 15, 'date': '2024-01-15', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 563} ,
        {'day_of_year': 16, 'date': '2024-01-16', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 623} ,
        {'day_of_year': 17, 'date': '2024-01-17', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 591} ,
        {'day_of_year': 18, 'date': '2024-01-18', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 574} ,
        {'day_of_year': 19, 'date': '2024-01-19', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 608} ,
        {'day_of_year': 20, 'date': '2024-01-20', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 590} ,
        {'day_of_year': 21, 'date': '2024-01-21', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 829} ,
        {'day_of_year': 22, 'date': '2024-01-22', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 706} ,
        {'day_of_year': 23, 'date': '2024-01-23', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 628} ,
        {'day_of_year': 24, 'date': '2024-01-24', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 690} ,
        {'day_of_year': 25, 'date': '2024-01-25', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 596} ,
        {'day_of_year': 26, 'date': '2024-01-26', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 546} ,
        {'day_of_year': 27, 'date': '2024-01-27', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 687} ,
        {'day_of_year': 28, 'date': '2024-01-28', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 769} ,
        {'day_of_year': 29, 'date': '2024-01-29', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 661} ,
        {'day_of_year': 30, 'date': '2024-01-30', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 586} ,
        {'day_of_year': 31, 'date': '2024-01-31', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 623} ,
        {'day_of_year': 32, 'date': '2024-02-01', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 715} ,
        {'day_of_year': 33, 'date': '2024-02-02', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 626} ,
        {'day_of_year': 34, 'date': '2024-02-03', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 736} ,
        {'day_of_year': 35, 'date': '2024-02-04', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 717} ,
        {'day_of_year': 36, 'date': '2024-02-05', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 718} ,
        {'day_of_year': 37, 'date': '2024-02-06', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 705} ,
        {'day_of_year': 38, 'date': '2024-02-07', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 685} ,
        {'day_of_year': 39, 'date': '2024-02-08', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 605} ,
        {'day_of_year': 40, 'date': '2024-02-09', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 738} ,
        {'day_of_year': 41, 'date': '2024-02-10', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 862} ,
        {'day_of_year': 42, 'date': '2024-02-11', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 723} ,
        {'day_of_year': 43, 'date': '2024-02-12', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 668} ,
        {'day_of_year': 44, 'date': '2024-02-13', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 624} ,
        {'day_of_year': 45, 'date': '2024-02-14', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 561} ,
        {'day_of_year': 46, 'date': '2024-02-15', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 669} ,
        {'day_of_year': 47, 'date': '2024-02-16', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 664} ,
        {'day_of_year': 48, 'date': '2024-02-17', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 700} ,
        {'day_of_year': 49, 'date': '2024-02-18', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 686} ,
        {'day_of_year': 50, 'date': '2024-02-19', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 523} ,
        {'day_of_year': 51, 'date': '2024-02-20', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 630} ,
        {'day_of_year': 52, 'date': '2024-02-21', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 767} ,
        {'day_of_year': 53, 'date': '2024-02-22', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 570} ,
        {'day_of_year': 54, 'date': '2024-02-23', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 643} ,
        {'day_of_year': 55, 'date': '2024-02-24', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 748} ,
        {'day_of_year': 56, 'date': '2024-02-25', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 723} ,
        {'day_of_year': 57, 'date': '2024-02-26', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 514} ,
        {'day_of_year': 58, 'date': '2024-02-27', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 647} ,
        {'day_of_year': 59, 'date': '2024-02-28', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 624} ,
        {'day_of_year': 60, 'date': '2024-02-29', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 687} ,
        {'day_of_year': 61, 'date': '2024-03-01', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 546} ,
        {'day_of_year': 62, 'date': '2024-03-02', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 669} ,
        {'day_of_year': 63, 'date': '2024-03-03', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 654} ,
        {'day_of_year': 64, 'date': '2024-03-04', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 649} ,
        {'day_of_year': 65, 'date': '2024-03-05', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 760} ,
        {'day_of_year': 66, 'date': '2024-03-06', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 597} ,
        {'day_of_year': 67, 'date': '2024-03-07', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 523} ,
        {'day_of_year': 68, 'date': '2024-03-08', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 499} ,
        {'day_of_year': 69, 'date': '2024-03-09', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 769} ,
        {'day_of_year': 70, 'date': '2024-03-10', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 735} ,
        {'day_of_year': 71, 'date': '2024-03-11', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 612} ,
        {'day_of_year': 72, 'date': '2024-03-12', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 643} ,
        {'day_of_year': 73, 'date': '2024-03-13', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 686} ,
        {'day_of_year': 74, 'date': '2024-03-14', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 615} ,
        {'day_of_year': 75, 'date': '2024-03-15', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 636} ,
        {'day_of_year': 76, 'date': '2024-03-16', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 645} ,
        {'day_of_year': 77, 'date': '2024-03-17', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 735} ,
        {'day_of_year': 78, 'date': '2024-03-18', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 641} ,
        {'day_of_year': 79, 'date': '2024-03-19', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 570} ,
        {'day_of_year': 80, 'date': '2024-03-20', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 531} ,
        {'day_of_year': 81, 'date': '2024-03-21', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 703} ,
        {'day_of_year': 82, 'date': '2024-03-22', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 613} ,
        {'day_of_year': 83, 'date': '2024-03-23', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 812} ,
        {'day_of_year': 84, 'date': '2024-03-24', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 756} ,
        {'day_of_year': 85, 'date': '2024-03-25', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 635} ,
        {'day_of_year': 86, 'date': '2024-03-26', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 554} ,
        {'day_of_year': 87, 'date': '2024-03-27', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 641} ,
        {'day_of_year': 88, 'date': '2024-03-28', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 578} ,
        {'day_of_year': 89, 'date': '2024-03-29', 'day_of_week': 'Friday', 'type': 'Good Friday', 'weekend': False, 'bank_holiday': True, 'school_holiday': True, 'visits': 1509} ,
        {'day_of_year': 90, 'date': '2024-03-30', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 874} ,
        {'day_of_year': 91, 'date': '2024-03-31', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 734} ,
        {'day_of_year': 92, 'date': '2024-04-01', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 572} ,
        {'day_of_year': 93, 'date': '2024-04-02', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 614} ,
        {'day_of_year': 94, 'date': '2024-04-03', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 623} ,
        {'day_of_year': 95, 'date': '2024-04-04', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 590} ,
        {'day_of_year': 96, 'date': '2024-04-05', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 650} ,
        {'day_of_year': 97, 'date': '2024-04-06', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 587} ,
        {'day_of_year': 98, 'date': '2024-04-07', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 751} ,
        {'day_of_year': 99, 'date': '2024-04-08', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 595} ,
        {'day_of_year': 100, 'date': '2024-04-09', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 579} ,
        {'day_of_year': 101, 'date': '2024-04-10', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 477} ,
        {'day_of_year': 102, 'date': '2024-04-11', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 740} ,
        {'day_of_year': 103, 'date': '2024-04-12', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 530} ,
        {'day_of_year': 104, 'date': '2024-04-13', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 800} ,
        {'day_of_year': 105, 'date': '2024-04-14', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 705} ,
        {'day_of_year': 106, 'date': '2024-04-15', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 565} ,
        {'day_of_year': 107, 'date': '2024-04-16', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 587} ,
        {'day_of_year': 108, 'date': '2024-04-17', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 740} ,
        {'day_of_year': 109, 'date': '2024-04-18', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 715} ,
        {'day_of_year': 110, 'date': '2024-04-19', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 540} ,
        {'day_of_year': 111, 'date': '2024-04-20', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 773} ,
        {'day_of_year': 112, 'date': '2024-04-21', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 803} ,
        {'day_of_year': 113, 'date': '2024-04-22', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 570} ,
        {'day_of_year': 114, 'date': '2024-04-23', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 635} ,
        {'day_of_year': 115, 'date': '2024-04-24', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 608} ,
        {'day_of_year': 116, 'date': '2024-04-25', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 478} ,
        {'day_of_year': 117, 'date': '2024-04-26', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 724} ,
        {'day_of_year': 118, 'date': '2024-04-27', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 913} ,
        {'day_of_year': 119, 'date': '2024-04-28', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 745} ,
        {'day_of_year': 120, 'date': '2024-04-29', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 546} ,
        {'day_of_year': 121, 'date': '2024-04-30', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 680} ,
        {'day_of_year': 122, 'date': '2024-05-01', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 716} ,
        {'day_of_year': 123, 'date': '2024-05-02', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 598} ,
        {'day_of_year': 124, 'date': '2024-05-03', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 585} ,
        {'day_of_year': 125, 'date': '2024-05-04', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 727} ,
        {'day_of_year': 126, 'date': '2024-05-05', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 731} ,
        {'day_of_year': 127, 'date': '2024-05-06', 'day_of_week': 'Monday', 'type': 'May Day', 'weekend': False, 'bank_holiday': True, 'school_holiday': False, 'visits': 1561} ,
        {'day_of_year': 128, 'date': '2024-05-07', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 675} ,
        {'day_of_year': 129, 'date': '2024-05-08', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 734} ,
        {'day_of_year': 130, 'date': '2024-05-09', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 605} ,
        {'day_of_year': 131, 'date': '2024-05-10', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 736} ,
        {'day_of_year': 132, 'date': '2024-05-11', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 836} ,
        {'day_of_year': 133, 'date': '2024-05-12', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 670} ,
        {'day_of_year': 134, 'date': '2024-05-13', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 661} ,
        {'day_of_year': 135, 'date': '2024-05-14', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 534} ,
        {'day_of_year': 136, 'date': '2024-05-15', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 646} ,
        {'day_of_year': 137, 'date': '2024-05-16', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 610} ,
        {'day_of_year': 138, 'date': '2024-05-17', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 607} ,
        {'day_of_year': 139, 'date': '2024-05-18', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 953} ,
        {'day_of_year': 140, 'date': '2024-05-19', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 813} ,
        {'day_of_year': 141, 'date': '2024-05-20', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 694} ,
        {'day_of_year': 142, 'date': '2024-05-21', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 689} ,
        {'day_of_year': 143, 'date': '2024-05-22', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 562} ,
        {'day_of_year': 144, 'date': '2024-05-23', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 639} ,
        {'day_of_year': 145, 'date': '2024-05-24', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 647} ,
        {'day_of_year': 146, 'date': '2024-05-25', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 879} ,
        {'day_of_year': 147, 'date': '2024-05-26', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 760} ,
        {'day_of_year': 148, 'date': '2024-05-27', 'day_of_week': 'Monday', 'type': 'Spring Bank Holiday', 'weekend': False, 'bank_holiday': True, 'school_holiday': False, 'visits': 1407} ,
        {'day_of_year': 149, 'date': '2024-05-28', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 692} ,
        {'day_of_year': 150, 'date': '2024-05-29', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 712} ,
        {'day_of_year': 151, 'date': '2024-05-30', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 663} ,
        {'day_of_year': 152, 'date': '2024-05-31', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 660} ,
        {'day_of_year': 153, 'date': '2024-06-01', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 787} ,
        {'day_of_year': 154, 'date': '2024-06-02', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 826} ,
        {'day_of_year': 155, 'date': '2024-06-03', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 758} ,
        {'day_of_year': 156, 'date': '2024-06-04', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 765} ,
        {'day_of_year': 157, 'date': '2024-06-05', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 757} ,
        {'day_of_year': 158, 'date': '2024-06-06', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 628} ,
        {'day_of_year': 159, 'date': '2024-06-07', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 631} ,
        {'day_of_year': 160, 'date': '2024-06-08', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 793} ,
        {'day_of_year': 161, 'date': '2024-06-09', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 780} ,
        {'day_of_year': 162, 'date': '2024-06-10', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 675} ,
        {'day_of_year': 163, 'date': '2024-06-11', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 697} ,
        {'day_of_year': 164, 'date': '2024-06-12', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 606} ,
        {'day_of_year': 165, 'date': '2024-06-13', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 719} ,
        {'day_of_year': 166, 'date': '2024-06-14', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 820} ,
        {'day_of_year': 167, 'date': '2024-06-15', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 882} ,
        {'day_of_year': 168, 'date': '2024-06-16', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 931} ,
        {'day_of_year': 169, 'date': '2024-06-17', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 728} ,
        {'day_of_year': 170, 'date': '2024-06-18', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 722} ,
        {'day_of_year': 171, 'date': '2024-06-19', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 689} ,
        {'day_of_year': 172, 'date': '2024-06-20', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 692} ,
        {'day_of_year': 173, 'date': '2024-06-21', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 797} ,
        {'day_of_year': 174, 'date': '2024-06-22', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 990} ,
        {'day_of_year': 175, 'date': '2024-06-23', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 747} ,
        {'day_of_year': 176, 'date': '2024-06-24', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 680} ,
        {'day_of_year': 177, 'date': '2024-06-25', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 702} ,
        {'day_of_year': 178, 'date': '2024-06-26', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 580} ,
        {'day_of_year': 179, 'date': '2024-06-27', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 666} ,
        {'day_of_year': 180, 'date': '2024-06-28', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 738} ,
        {'day_of_year': 181, 'date': '2024-06-29', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 1007} ,
        {'day_of_year': 182, 'date': '2024-06-30', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 804} ,
        {'day_of_year': 183, 'date': '2024-07-01', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 1075} ,
        {'day_of_year': 184, 'date': '2024-07-02', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 875} ,
        {'day_of_year': 185, 'date': '2024-07-03', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 852} ,
        {'day_of_year': 186, 'date': '2024-07-04', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 828} ,
        {'day_of_year': 187, 'date': '2024-07-05', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 829} ,
        {'day_of_year': 188, 'date': '2024-07-06', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 1203} ,
        {'day_of_year': 189, 'date': '2024-07-07', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 1251} ,
        {'day_of_year': 190, 'date': '2024-07-08', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 1065} ,
        {'day_of_year': 191, 'date': '2024-07-09', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 959} ,
        {'day_of_year': 192, 'date': '2024-07-10', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 1007} ,
        {'day_of_year': 193, 'date': '2024-07-11', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 978} ,
        {'day_of_year': 194, 'date': '2024-07-12', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 941} ,
        {'day_of_year': 195, 'date': '2024-07-13', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 1075} ,
        {'day_of_year': 196, 'date': '2024-07-14', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 1186} ,
        {'day_of_year': 197, 'date': '2024-07-15', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 929} ,
        {'day_of_year': 198, 'date': '2024-07-16', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 1002} ,
        {'day_of_year': 199, 'date': '2024-07-17', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 926} ,
        {'day_of_year': 200, 'date': '2024-07-18', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 874} ,
        {'day_of_year': 201, 'date': '2024-07-19', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 837} ,
        {'day_of_year': 202, 'date': '2024-07-20', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 994} ,
        {'day_of_year': 203, 'date': '2024-07-21', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 1281} ,
        {'day_of_year': 204, 'date': '2024-07-22', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 969} ,
        {'day_of_year': 205, 'date': '2024-07-23', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 993} ,
        {'day_of_year': 206, 'date': '2024-07-24', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 860} ,
        {'day_of_year': 207, 'date': '2024-07-25', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 979} ,
        {'day_of_year': 208, 'date': '2024-07-26', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 868} ,
        {'day_of_year': 209, 'date': '2024-07-27', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 923} ,
        {'day_of_year': 210, 'date': '2024-07-28', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1199} ,
        {'day_of_year': 211, 'date': '2024-07-29', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 980} ,
        {'day_of_year': 212, 'date': '2024-07-30', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 908} ,
        {'day_of_year': 213, 'date': '2024-07-31', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 927} ,
        {'day_of_year': 214, 'date': '2024-08-01', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 945} ,
        {'day_of_year': 215, 'date': '2024-08-02', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1099} ,
        {'day_of_year': 216, 'date': '2024-08-03', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 997} ,
        {'day_of_year': 217, 'date': '2024-08-04', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1429} ,
        {'day_of_year': 218, 'date': '2024-08-05', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1205} ,
        {'day_of_year': 219, 'date': '2024-08-06', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1052} ,
        {'day_of_year': 220, 'date': '2024-08-07', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1066} ,
        {'day_of_year': 221, 'date': '2024-08-08', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 992} ,
        {'day_of_year': 222, 'date': '2024-08-09', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1156} ,
        {'day_of_year': 223, 'date': '2024-08-10', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1291} ,
        {'day_of_year': 224, 'date': '2024-08-11', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1249} ,
        {'day_of_year': 225, 'date': '2024-08-12', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1188} ,
        {'day_of_year': 226, 'date': '2024-08-13', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 960} ,
        {'day_of_year': 227, 'date': '2024-08-14', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1006} ,
        {'day_of_year': 228, 'date': '2024-08-15', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1091} ,
        {'day_of_year': 229, 'date': '2024-08-16', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1102} ,
        {'day_of_year': 230, 'date': '2024-08-17', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1525} ,
        {'day_of_year': 231, 'date': '2024-08-18', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1444} ,
        {'day_of_year': 232, 'date': '2024-08-19', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1083} ,
        {'day_of_year': 233, 'date': '2024-08-20', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1042} ,
        {'day_of_year': 234, 'date': '2024-08-21', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 933} ,
        {'day_of_year': 235, 'date': '2024-08-22', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1196} ,
        {'day_of_year': 236, 'date': '2024-08-23', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 998} ,
        {'day_of_year': 237, 'date': '2024-08-24', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1432} ,
        {'day_of_year': 238, 'date': '2024-08-25', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1284} ,
        {'day_of_year': 239, 'date': '2024-08-26', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 990} ,
        {'day_of_year': 240, 'date': '2024-08-27', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1122} ,
        {'day_of_year': 241, 'date': '2024-08-28', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1249} ,
        {'day_of_year': 242, 'date': '2024-08-29', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 1101} ,
        {'day_of_year': 243, 'date': '2024-08-30', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 941} ,
        {'day_of_year': 244, 'date': '2024-08-31', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 1380} ,
        {'day_of_year': 245, 'date': '2024-09-01', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 689} ,
        {'day_of_year': 246, 'date': '2024-09-02', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 557} ,
        {'day_of_year': 247, 'date': '2024-09-03', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 611} ,
        {'day_of_year': 248, 'date': '2024-09-04', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 698} ,
        {'day_of_year': 249, 'date': '2024-09-05', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 695} ,
        {'day_of_year': 250, 'date': '2024-09-06', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 480} ,
        {'day_of_year': 251, 'date': '2024-09-07', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 867} ,
        {'day_of_year': 252, 'date': '2024-09-08', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 798} ,
        {'day_of_year': 253, 'date': '2024-09-09', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 623} ,
        {'day_of_year': 254, 'date': '2024-09-10', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 618} ,
        {'day_of_year': 255, 'date': '2024-09-11', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 609} ,
        {'day_of_year': 256, 'date': '2024-09-12', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 642} ,
        {'day_of_year': 257, 'date': '2024-09-13', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 551} ,
        {'day_of_year': 258, 'date': '2024-09-14', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 736} ,
        {'day_of_year': 259, 'date': '2024-09-15', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 705} ,
        {'day_of_year': 260, 'date': '2024-09-16', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 631} ,
        {'day_of_year': 261, 'date': '2024-09-17', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 490} ,
        {'day_of_year': 262, 'date': '2024-09-18', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 645} ,
        {'day_of_year': 263, 'date': '2024-09-19', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 679} ,
        {'day_of_year': 264, 'date': '2024-09-20', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 659} ,
        {'day_of_year': 265, 'date': '2024-09-21', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 721} ,
        {'day_of_year': 266, 'date': '2024-09-22', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 791} ,
        {'day_of_year': 267, 'date': '2024-09-23', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 658} ,
        {'day_of_year': 268, 'date': '2024-09-24', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 607} ,
        {'day_of_year': 269, 'date': '2024-09-25', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 628} ,
        {'day_of_year': 270, 'date': '2024-09-26', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 622} ,
        {'day_of_year': 271, 'date': '2024-09-27', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 556} ,
        {'day_of_year': 272, 'date': '2024-09-28', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 715} ,
        {'day_of_year': 273, 'date': '2024-09-29', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 792} ,
        {'day_of_year': 274, 'date': '2024-09-30', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 654} ,
        {'day_of_year': 275, 'date': '2024-10-01', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 671} ,
        {'day_of_year': 276, 'date': '2024-10-02', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 564} ,
        {'day_of_year': 277, 'date': '2024-10-03', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 669} ,
        {'day_of_year': 278, 'date': '2024-10-04', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 584} ,
        {'day_of_year': 279, 'date': '2024-10-05', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 841} ,
        {'day_of_year': 280, 'date': '2024-10-06', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 760} ,
        {'day_of_year': 281, 'date': '2024-10-07', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 707} ,
        {'day_of_year': 282, 'date': '2024-10-08', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 617} ,
        {'day_of_year': 283, 'date': '2024-10-09', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 645} ,
        {'day_of_year': 284, 'date': '2024-10-10', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 667} ,
        {'day_of_year': 285, 'date': '2024-10-11', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 512} ,
        {'day_of_year': 286, 'date': '2024-10-12', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 735} ,
        {'day_of_year': 287, 'date': '2024-10-13', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 761} ,
        {'day_of_year': 288, 'date': '2024-10-14', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 809} ,
        {'day_of_year': 289, 'date': '2024-10-15', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 661} ,
        {'day_of_year': 290, 'date': '2024-10-16', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 653} ,
        {'day_of_year': 291, 'date': '2024-10-17', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 538} ,
        {'day_of_year': 292, 'date': '2024-10-18', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 649} ,
        {'day_of_year': 293, 'date': '2024-10-19', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 839} ,
        {'day_of_year': 294, 'date': '2024-10-20', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 860} ,
        {'day_of_year': 295, 'date': '2024-10-21', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 722} ,
        {'day_of_year': 296, 'date': '2024-10-22', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 456} ,
        {'day_of_year': 297, 'date': '2024-10-23', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 689} ,
        {'day_of_year': 298, 'date': '2024-10-24', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 564} ,
        {'day_of_year': 299, 'date': '2024-10-25', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 631} ,
        {'day_of_year': 300, 'date': '2024-10-26', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 745} ,
        {'day_of_year': 301, 'date': '2024-10-27', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 896} ,
        {'day_of_year': 302, 'date': '2024-10-28', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 549} ,
        {'day_of_year': 303, 'date': '2024-10-29', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 551} ,
        {'day_of_year': 304, 'date': '2024-10-30', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 655} ,
        {'day_of_year': 305, 'date': '2024-10-31', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 653} ,
        {'day_of_year': 306, 'date': '2024-11-01', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 552} ,
        {'day_of_year': 307, 'date': '2024-11-02', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 766} ,
        {'day_of_year': 308, 'date': '2024-11-03', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 715} ,
        {'day_of_year': 309, 'date': '2024-11-04', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 666} ,
        {'day_of_year': 310, 'date': '2024-11-05', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 635} ,
        {'day_of_year': 311, 'date': '2024-11-06', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 645} ,
        {'day_of_year': 312, 'date': '2024-11-07', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 669} ,
        {'day_of_year': 313, 'date': '2024-11-08', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 548} ,
        {'day_of_year': 314, 'date': '2024-11-09', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 899} ,
        {'day_of_year': 315, 'date': '2024-11-10', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 855} ,
        {'day_of_year': 316, 'date': '2024-11-11', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 569} ,
        {'day_of_year': 317, 'date': '2024-11-12', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 655} ,
        {'day_of_year': 318, 'date': '2024-11-13', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 621} ,
        {'day_of_year': 319, 'date': '2024-11-14', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 712} ,
        {'day_of_year': 320, 'date': '2024-11-15', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 652} ,
        {'day_of_year': 321, 'date': '2024-11-16', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 825} ,
        {'day_of_year': 322, 'date': '2024-11-17', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 823} ,
        {'day_of_year': 323, 'date': '2024-11-18', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 567} ,
        {'day_of_year': 324, 'date': '2024-11-19', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 722} ,
        {'day_of_year': 325, 'date': '2024-11-20', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 571} ,
        {'day_of_year': 326, 'date': '2024-11-21', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 607} ,
        {'day_of_year': 327, 'date': '2024-11-22', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 610} ,
        {'day_of_year': 328, 'date': '2024-11-23', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 692} ,
        {'day_of_year': 329, 'date': '2024-11-24', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 729} ,
        {'day_of_year': 330, 'date': '2024-11-25', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 605} ,
        {'day_of_year': 331, 'date': '2024-11-26', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 677} ,
        {'day_of_year': 332, 'date': '2024-11-27', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 651} ,
        {'day_of_year': 333, 'date': '2024-11-28', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 521} ,
        {'day_of_year': 334, 'date': '2024-11-29', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 600} ,
        {'day_of_year': 335, 'date': '2024-11-30', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 897} ,
        {'day_of_year': 336, 'date': '2024-12-01', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 798} ,
        {'day_of_year': 337, 'date': '2024-12-02', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 661} ,
        {'day_of_year': 338, 'date': '2024-12-03', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 717} ,
        {'day_of_year': 339, 'date': '2024-12-04', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 652} ,
        {'day_of_year': 340, 'date': '2024-12-05', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 637} ,
        {'day_of_year': 341, 'date': '2024-12-06', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 614} ,
        {'day_of_year': 342, 'date': '2024-12-07', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 832} ,
        {'day_of_year': 343, 'date': '2024-12-08', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 737} ,
        {'day_of_year': 344, 'date': '2024-12-09', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 652} ,
        {'day_of_year': 345, 'date': '2024-12-10', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 684} ,
        {'day_of_year': 346, 'date': '2024-12-11', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 640} ,
        {'day_of_year': 347, 'date': '2024-12-12', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 603} ,
        {'day_of_year': 348, 'date': '2024-12-13', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 676} ,
        {'day_of_year': 349, 'date': '2024-12-14', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 687} ,
        {'day_of_year': 350, 'date': '2024-12-15', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': False, 'visits': 892} ,
        {'day_of_year': 351, 'date': '2024-12-16', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 604} ,
        {'day_of_year': 352, 'date': '2024-12-17', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 675} ,
        {'day_of_year': 353, 'date': '2024-12-18', 'day_of_week': 'Wednesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': False, 'visits': 578} ,
        {'day_of_year': 354, 'date': '2024-12-19', 'day_of_week': 'Thursday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 606} ,
        {'day_of_year': 355, 'date': '2024-12-20', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 709} ,
        {'day_of_year': 356, 'date': '2024-12-21', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 688} ,
        {'day_of_year': 357, 'date': '2024-12-22', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 705} ,
        {'day_of_year': 358, 'date': '2024-12-23', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 649} ,
        {'day_of_year': 359, 'date': '2024-12-24', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 714} ,
        {'day_of_year': 360, 'date': '2024-12-25', 'day_of_week': 'Wednesday', 'type': 'Christmas Day', 'weekend': False, 'bank_holiday': True, 'school_holiday': True, 'visits': 0} ,
        {'day_of_year': 361, 'date': '2024-12-26', 'day_of_week': 'Thursday', 'type': 'Boxing Day', 'weekend': False, 'bank_holiday': True, 'school_holiday': True, 'visits': 1658} ,
        {'day_of_year': 362, 'date': '2024-12-27', 'day_of_week': 'Friday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 633} ,
        {'day_of_year': 363, 'date': '2024-12-28', 'day_of_week': 'Saturday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 686} ,
        {'day_of_year': 364, 'date': '2024-12-29', 'day_of_week': 'Sunday', 'type': 'Normal Day', 'weekend': True, 'bank_holiday': False, 'school_holiday': True, 'visits': 768} ,
        {'day_of_year': 365, 'date': '2024-12-30', 'day_of_week': 'Monday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 714} ,
        {'day_of_year': 366, 'date': '2024-12-31', 'day_of_week': 'Tuesday', 'type': 'Normal Day', 'weekend': False, 'bank_holiday': False, 'school_holiday': True, 'visits': 630} 
    ]
    return(days_2024)

# ----------------------------------------------------------------------------------------

def define_entityZones():
    zones = [
        {"Zone_ID": "01", "Zone" :"Aquatic"},
        {"Zone_ID": "02", "Zone" :"Big Cats"},
        {"Zone_ID": "03", "Zone" :"Monkeys"}
    ]

    return(zones)
def define_entityEnclosures():

    zones = define_entityZones()

    # Enclosures, generate a dummy id which will be updated later
    enclosures = [
        # Aquatic Zone
        {"Enclosure_ID": "01/0001", "Name": "Darwin", "WikiURL": "https://en.wikipedia.org/wiki/Charles_Darwin", "Zone": "Aquatic", "Animal": "Penguins", "Capacity": 10, "Current_Number": 10, "Diet": "Fish", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "01/0002", "Name": "Wallace", "WikiURL": "https://en.wikipedia.org/wiki/Alfred_Russel_Wallace", "Zone": "Aquatic", "Animal": "Penguins", "Capacity": 10, "Current_Number": 8, "Diet": "Fish", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "01/0003", "Name": "Huxley", "WikiURL": "https://en.wikipedia.org/wiki/Thomas_Henry_Huxley", "Zone": "Aquatic", "Animal": "Penguins", "Capacity": 10, "Current_Number": 6, "Diet": "Fish", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "01/0004", "Name": "Audubon", "WikiURL": "https://en.wikipedia.org/wiki/John_James_Audubon", "Zone": "Aquatic", "Animal": "Flamingos", "Capacity": 15, "Current_Number": 15, "Diet": "Plants", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "01/0005", "Name": "Cousteau", "WikiURL": "https://en.wikipedia.org/wiki/Jacques_Cousteau", "Zone": "Aquatic", "Animal": "Starfish and Stingrays", "Capacity": 0, "Current_Number": 0, "Diet": "Various", "Status": "Closed", "Closed_Date": "2023-12-21"},
        
        # Big Cats Zone
        {"Enclosure_ID": "02/0001", "Name": "Livingstone", "WikiURL": "https://en.wikipedia.org/wiki/David_Livingstone", "Zone": "Big Cats", "Animal": "Lions", "Capacity": 5, "Current_Number": 5, "Diet": "Meat", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "02/0002", "Name": "Bates", "WikiURL": "https://en.wikipedia.org/wiki/Henry_Walter_Bates", "Zone": "Big Cats", "Animal": "Tigers", "Capacity": 3, "Current_Number": 2, "Diet": "Meat", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "02/0003", "Name": "Humboldt", "WikiURL": "https://en.wikipedia.org/wiki/Alexander_von_Humboldt", "Zone": "Big Cats", "Animal": "Jaguars", "Capacity": 2, "Current_Number": 2, "Diet": "Meat", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "02/0004", "Name": "VonFrisch", "WikiURL": "https://en.wikipedia.org/wiki/Karl_von_Frisch", "Zone": "Big Cats", "Animal": "Lynx", "Capacity": 6, "Current_Number": 6, "Diet": "Meat", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "02/0005", "Name": "Cougar", "WikiURL": "https://en.wikipedia.org/wiki/Cougar", "Zone": "Big Cats", "Animal": "Cheetahs", "Capacity": 0, "Current_Number": 0, "Diet": "Meat", "Status": "Closed", "Closed_Date": "2024-03-26"},
        
        # Monkey Zone
        {"Enclosure_ID": "03/0001", "Name": "Leakey", "WikiURL": "https://en.wikipedia.org/wiki/Louis_Leakey", "Zone": "Monkeys", "Animal": "Gorillas", "Capacity": 3, "Current_Number": 3, "Diet": "Plants", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "03/0002", "Name": "Goodall", "WikiURL": "https://en.wikipedia.org/wiki/Jane_Goodall", "Zone": "Monkeys", "Animal": "Chimpanzees", "Capacity": 8, "Current_Number": 7, "Diet": "Plants", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "03/0003", "Name": "Fossey", "WikiURL": "https://en.wikipedia.org/wiki/Dian_Fossey", "Zone": "Monkeys", "Animal": "Capuchins", "Capacity": 4, "Current_Number": 4, "Diet": "Fruits", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "03/0004", "Name": "Koehler", "WikiURL": "https://en.wikipedia.org/wiki/Wolfgang_Köhler", "Zone": "Monkeys", "Animal": "Orangutans", "Capacity": 5, "Current_Number": 5, "Diet": "Fruits", "Status": "Open", "Closed_Date": None},
        {"Enclosure_ID": "03/0005", "Name": "Zhou", "WikiURL": "https://en.wikipedia.org/wiki/Zhou_Cheng", "Zone": "Monkeys", "Animal": "Golden Snub-Nosed Monkeys", "Capacity": 6, "Current_Number": 6, "Diet": "Plants", "Status": "Open", "Closed_Date": None},
    ]

    # update the enclosures id based on the Zone
    for i, enc in enumerate(enclosures):
        # get the Zone type from the Enclosure
        myZone = enc['Zone']
        # get the Zone_Id from the zones dictionary
        id = next((d["Zone_ID"] for d in zones if d["Zone"] == myZone), None)
        # generate an enclosure id
        myId = f'{id}/{i+1:04}'
        enc['Enclosure_ID'] = myId

    return(enclosures)
def define_entityStaff():

    # zones dictionary
    zones = define_entityZones()
    # enclosures dictionary
    enclosures = define_entityEnclosures()
    # names
    list_names, list_probability = generate_names()
    # Staff roles and start times
    start_times = ["Morning", "Morning","Morning","Afternoon"]

    # List to hold all staff members
    staff = []
    names = []

    # Generate 2 Zone level staff 
    for zone in zones:
        # Add Vet and Supervisor for the zone
        for role in ["Vet", "Supervisor"]:
            staff.append({
                "Staff_ID": generate_staff_id(),
                "Zone": zone['Zone'],
                "Enclosure_ID": 'None',
                "Name": f"{weighted_choice(list_names, list_probability)}",
                "Role": role,
                "FTE": generate_fte(role),
                "Start_time": random.choice(start_times),
            })

    # Add 6 staff members for each enclosure
    list_enclosures = [elem["Enclosure_ID"] for elem in enclosures]
    for enclosure in list_enclosures:
        for _ in range(6):
            staff.append({
                "Staff_ID": generate_staff_id(),
                "Zone":"From Enclosure Id",
                "Enclosure_ID": enclosure,
                "Name": f"{weighted_choice(list_names, list_probability)}",
                "Role": "Staff",
                "FTE": generate_fte("Staff"),
                "Start_time": random.choice(start_times),
            })

    return(staff)
def define_entityAnimals():

    # get the enclosures dictionary
    enclosures = define_entityEnclosures()

    animals = []

    for enc in enclosures:
        enclosure_id = enc['Enclosure_ID']
        num = enc['Current_Number']

        species = enc['Animal']
        if species == 'Penguins':
            if enclosure_id == '01/0001':
                species = 'Emperor Penguin'
            elif enclosure_id == '01/0002':
                species = 'Gentoo Penguin'
            else:
                species = 'Humbolt Penguin'

        for _ in range(num):
            age = random.randint(1, 25)
            animals.append({
                "Enclosure_ID": enclosure_id,
                "Animal_ID": generate_animal_id(),
                "SubSpecies": species,
                "Name": generate_animal_name(enc['Animal']),
                "Age": age,  # Age between 1 and 20 years
                "Gender": random.choice(["Male", "Female"]),
                "Arrival_Date": generate_random_date(age),
                "Health_Status": random.choice(["Healthy", "Minor Issues", "Under Treatment"]),
            })

    return(animals)
def define_entityInvoices():

    items, budgets, month = generate_food()
    food_invoices = []

    inv = 0
    random.seed(1234)
    for m in month:
        inv +=1
        for i, item in enumerate(items):
            inv +=1

            budget = budgets[i]
            wt = random.uniform(0.8, 1.3)
            if item == 'Meat':
                wt = random.uniform(0.9,1.5)

            x = {'Invoice_ID': f'Zoo-{inv:04}',
                'Month': m,
                'Order Type': item,
                'Cost':round(budget * wt, 2)}
            
            food_invoices.append(x)

    return(food_invoices)
def define_entityBudgets():

    items, budgets, month = generate_food()
    
    # This is how each type of food is allocated between Enclosures
    allocate_fish = [{'01/0001': .33}, {"01/0002": .33}, {"01/0003": .34}]
    allocate_fruit = [{'03/0013': .2}, {"03/0014":.8}]
    allocate_meat = [{"02/0006": .4}, {"02/0007":.15},{"02/0008":.15},{"02/0009":.3}]
    allocate_plant = [{"01/0004": .3}, {"03/0011":.5}, {"03/0012":.1}, {"03/0015":.1}]
    allocate_central = [{"Staff": 1}]

    random.seed(1234)
    food_budgets = []
    for m in month:
        for i, item in enumerate(items):

            budget = budgets[i]

            if item == 'Fish':
                allocation = allocate_fish
            elif item == "Fruit":
                allocation = allocate_fruit
            elif item == "Meat":
                allocation = allocate_meat
            elif item == "Plants":
                allocation = allocate_plant
            else:
                allocation = allocate_central
            
            for enc in allocation:
                for key, value in enc.items():
                    # Optionally store them in variables
                    extracted_key = key
                    extracted_value = value

                    y = {'Month': m,
                        'Order Type': item,
                        'Enclosure': key,
                        'Budget': budget * value}
        
                    food_budgets.append(y)
            
    return(food_budgets)
def define_entityCalendar(mode = 'static'):
    
    # pre defined calendar
    if mode == "static":
        return(generate_static_calendar())

    # Generate a new calendar from scratch     
    # Define UK bank holidays
    uk_holidays = holidays.UK(years=2024)

    # Generate the list of dictionaries
    days_2024 = []
    start_date = datetime.date(2024, 1, 1)
    end_date = datetime.date(2024, 12, 31)

    current_date = start_date
    doy = 0
    while current_date <= end_date:
        doy +=1 
        dow = current_date.strftime("%A")

        is_bankholiday = True if current_date in uk_holidays else False
        is_schoolholiday = True if is_school_holiday(current_date) else False
        is_weekend = True if dow in ['Saturday','Sunday'] else False

        day_entry = {
            "day_of_year": doy,
            "date": current_date.strftime("%Y-%m-%d"),
            "day_of_week": dow,
            "type": "Normal Day" if not current_date in uk_holidays else uk_holidays[current_date],
            "weekend": is_weekend,
            "bank_holiday": is_bankholiday,
            "school_holiday": is_schoolholiday,
            "visits":generate_visit_count(current_date, is_weekend, is_bankholiday, is_schoolholiday)
        }
        days_2024.append(day_entry)
        current_date += datetime.timedelta(days=1)

        # define visits to match this calender
        #df_Calendar = pd.DataFrame(days_2024)
        #dict_visits = define_entityVisits(df_Calendar)

    return(days_2024)
def define_entityVisits(verbose = False):
    # generate the targets and calculate the proportion for each
    # enclosure, and the split between ad-hoc visits and member visits
    dict_Calendar = generate_static_calendar()
    df_Calendar = pd.DataFrame(dict_Calendar)
    if verbose:
        print(f'df_Calendar is {df_Calendar.shape}')

    dict_Targets = generate_visit_targets()
    df_Targets = pd.DataFrame(dict_Targets)
    if verbose:
        print(f'df_Targets is {df_Targets.shape}')

    df_Targets['Total'] = df_Targets['Visits'] + df_Targets['MemberVisits']

    df_Targets["prop"] = df_Targets['Total'] / df_Targets['Total'].sum()
    df_Targets['r1'] = df_Targets["Visits"] / df_Targets['Total']
    df_Targets['r2'] = df_Targets["MemberVisits"] / df_Targets['Total']

    # get the member_ids
    dict_Members = generate_members()

    # List to return
    visits =[]

    # for each day in the calender
    for i, row in df_Calendar.iterrows():
        date = row['date']
        total_today = row['visits']
        total_visits_created = 0
        if verbose:
            print(date)

        # for each enclosure target
        for j, row_targ in df_Targets.iterrows():
            enc = row_targ['Enclosure_ID']
            prop = row_targ['prop']
            if prop == 0: continue
            t1 = row_targ["r1"]
            t2 = row_targ["r2"]

            # visits for the enclosure
            total_enclosure = round(total_today * prop, 0)
            v1 = round(total_enclosure * t1) # non-members
            v2 = round(total_enclosure * t2) # members

            # ad-hoc visits
            for visit in range(0,v1):
                visit_nm = {"Date": date, 
                            "Enclosure_ID": enc,
                            "Member_ID":'None'}
                visits.append(visit_nm)

            # member visits
            for visit in range(0,v2):
                mem_id = random.choice(dict_Members)
                mem_id = mem_id['Member_ID']
                visit_mem = {"Date": date, 
                            "Enclosure_ID": enc,
                            "Member_ID":mem_id}
                visits.append(visit_mem)
                
    return(visits)

# ----------------------------------------------------------------------------------------------------
def createEntity(entityName, verbose = False):

    validList = ['Zones', 'Enclosures', 'Staff', 'Animals','Invoices','Budgets','Calendar','Visits']

    if not entityName in validList:
        print(f' ... Invalid Entity {entityName}')
        return()
    else:
        print(f' ... Creating df for {entityName}')

    if entityName == 'Zones':
        data = define_entityZones()
        df = pd.DataFrame(data)

    elif entityName == 'Enclosures':
        data = define_entityEnclosures()
        df = pd.DataFrame(data)

    elif entityName == 'Staff':
        data = define_entityStaff()
        df = pd.DataFrame(data)

    elif entityName == 'Animals':
        data = define_entityAnimals()
        df = pd.DataFrame(data)

    elif entityName == 'Invoices':
        data = define_entityInvoices()
        df = pd.DataFrame(data)

    elif entityName == 'Budgets':
        data = define_entityBudgets()
        df = pd.DataFrame(data)

    elif entityName == 'Calendar':
        data = define_entityCalendar()
        df = pd.DataFrame(data)

    elif entityName == 'Visits':
        data = define_entityVisits()
        df = pd.DataFrame(data)

    if verbose:
        print(f' ... Created df for {entityName} with {df.shape[0]} rows and {df.shape[1]} cols, columns are {df.columns}')
    
    return(df)

def createZoo(verbose = True):

    out_dir = './data'
    validList = ['Zones', 'Enclosures', 'Staff', 'Animals','Invoices','Budgets','Calendar','Visits']

    for entity in validList:
        out_name = f'{out_dir}/Zoo-{entity}.csv'
        print(f'{datetime.datetime.now().strftime('%H:%M:%S')} {'-' * 40}')
        print(f' ... Creating {out_name}')
        df_Entity = createEntity(entity, verbose = True)
        df_Entity.to_csv(out_name, index = None)


def main():
    createZoo()

if __name__=="__main__":
    main()