# Functions used in CGI Academy Data Engineering Exercise 1


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

################ORIGINAL DATA IMPORT########################


def extract_data():
    '''
    This function reads in four csvs and one json file, and combines them, replaces blanks with nan, and returns a Pandas DataFrame with all of the ticket data from the Los Angeles open data 
    '''
    df_pandas = pd.DataFrame(
        columns=['Ticket number', 'Issue Date', 'Issue time', 'Meter Id', 'Marked Time',
                 'RP State Plate', 'Plate Expiry Date', 'VIN', 'Make', 'Body Style',
                 'Color', 'Location', 'Route', 'Agency', 'Violation code',
                 'Violation Description', 'Fine amount', 'Latitude', 'Longitude',
                 'Agency Description', 'Color Description', 'Body Style Description'])

    print('Importing csv...')
    # read the shared folder data into spark dataframe
    df0 = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_sample_0.csv')
    df1 = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_sample_1.csv')
    df2 = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_sample_2.csv')
    df3 = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_sample_3.csv')
    df4 = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_sample_4.csv')
    # There is more parking citation data on the github repo, I am going to import and add it too
    df5 = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_sample_5.csv')
    df_csv = pd.concat([df0, df1, df2, df3, df4, df5])
    # Drop the first column, and append it to pandas dataframe
    df_csv = df_csv.iloc[:, 1:]
    df_pandas = df_pandas.append(df_csv)

    # read and append json
    print('Importing json...')

    df_json = pd.read_json(
        'https://raw.githubusercontent.com/matthewbrennerCGI/Project1Data/main/parking_citation_add.json')
    df_json = df_json.iloc[:, 1:]
    df_pandas = df_pandas.append(df_json)

    df = df_pandas.replace('', np.nan)
    df.drop(['Unnamed:_0.1'], axis=1, inplace=True)
    print('Data import complete.')
    print(f'Shape: {str(df_pandas.shape)}')
    return df

####################DATA VALIDATION FUNCTIONS#######################


def has_digit(df, my_col):
    '''
    This function takes a dataframe and column name and employs regular expressions to see if there are any numerical digits in the cell and returns only the rows in the column containing digits.
    '''
    df[my_col] = df[my_col].astype(str)
    return df[df[my_col].str.contains(r'[0-9]') == True]


def only_alpha(df, my_col):
    '''
    This function takes a dataframe and specified columns, check if a column only has alphabetical values and returns rows where this is not true.
    '''
    df[my_col] = df[my_col].astype(str)
    return df[df[my_col].str.contains(r'[^a-zA-Z \/\.\-]') == True]


def only_number(df, my_col):
    '''
    This function takes a dataframe and specified columns, check if a column only has alphabetical values and returns rows where this is not true.
    '''
    df[my_col] = df[my_col].astype(str)
    return df[df[my_col].str.contains(r'^\d+$') == False]

####################### OTHER DATA ENGINEERING FUNCTIONS #######################


def get_distance(lat1, lon1, lat2, lon2):
    '''
    Given the latitude and longitude of two points, compute the hypotenuse distance between them
    '''
    return (((abs(lat1-lat2))**2) + ((abs(lon1-lon2))**2))**(1/2)


def drop_columns(df, threshold):
    '''
    drop columns from a dataframe over a threshold (0-1, percentage) missing data
    '''
    columns = (df.columns[df.isnull().mean() > threshold]).tolist()

    original_dimensions = df.shape
    df.drop(columns, axis=1, inplace=True)
    final_dimensions = df.shape

    print(f'Columns over {threshold} null threshold to drop:  {columns}')
    print(f'Original dimensions: {original_dimensions}')
    print(f'Dimensions after drop: {final_dimensions}')
    print(f'{original_dimensions[1]-final_dimensions[1]} columns dropped.')
    return df


def drop_not_us(df):
    '''
    Takes in a dataframe
    Drops rows of records where RP_State_Plate does not match one of the US 50 states
    Returns dataframe with only us states
    '''
    # Read in state abbreviations
    state = pd.read_csv(
        'https://raw.githubusercontent.com/matthewbrennerCGI/state_abbreviations/main/State_Abbreviations.csv')
    # make a list of state abbreviations
    states = state.Abbreviation.tolist()
    # Dorop rows where records arent in the state list and print details
    original_dimensions = df.shape
    df = df[df['RP_State_Plate'].isin(states)]
    final_dimensions = df.shape
    print('Dropping license plates from outside the 50 US States')
    print(f'Original dimensions: {original_dimensions}')
    print(f'Final dimensions: {final_dimensions}')
    print(f'{original_dimensions[0] - final_dimensions[0]} rows dropped.')
    return df


def address_split(df):
    '''
    Takes in a dataframe and splits the address field from a single string into 7 columns, dividing on a space as a separator
    '''
    location_split = df.Location.str.split(' ', expand=True)
    df['address_0'] = location_split[0]
    df['address_1'] = location_split[1]
    df['address_2'] = location_split[2]
    df['address_3'] = location_split[3]
    df['address_4'] = location_split[4]
    df['address_5'] = location_split[5]
    df['address_6'] = location_split[6]
    df['address_7'] = location_split[7]
    return df
