# Data Engineering Exercise 1
# Jared Godar

import pandas as pd
import numpy as np

from prepare import extract_data
from prepare import get_distance
from prepare import drop_columns
from prepare import drop_not_us
from prepare import address_split


# Extract data
df = extract_data()
# remove spaces in columns name and replace with an undersocore
df.columns = df.columns.str.replace(' ', '_')
# Convert Ticket number to string, Issue date to date, and display datatypes to confirm changes
df['Ticket_number'] = df['Ticket_number'].astype(str)
df['Issue_Date'] = pd.to_datetime(df['Issue_Date'])
# Drop LAT/LON == 9999
df = df[(df.Latitude != 99999) | (df.Longitude != 99999)]
# Define point A
lat2 = 6439997
lon2 = 1802686
# Create column calculating distance to above point
df['Distance_to_pointA'] = round(get_distance(
    df['Latitude'], df['Longitude'], lat2, lon2), 2)
# Drop 2 duplicated records
df.drop_duplicates(inplace=True)
# Drop columns with over 70% missing records
df = drop_columns(df, 0.7)
# Drop records with plates from outside US
df = drop_not_us(df)
# split address
df = address_split(df)
# Make issue year column out of the datetime object issue date
df['Issue_year'] = df['Issue_Date'].dt.year
