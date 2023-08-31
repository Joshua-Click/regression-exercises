import pandas as pd
import numpy as np
import os
from env import get_db_url


def get_zillow_2017():
    '''This function imports zillow 2017 data from MySql codeup server and creates a csv
    
    argument: df
    
    returns: zillow df'''
    filename = "zillow_2017.csv"
    if os.path.isfile(filename):
        df = pd.read_csv(filename)
    else:
        query = """
        SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt, yearbuilt, taxamount, fips
        FROM properties_2017
        JOIN propertylandusetype
        USING (propertylandusetypeid)
        WHERE propertylandusetypeid like '261';"""
        connection = get_db_url("zillow")
        df = pd.read_sql(query, connection)
        df.to_csv(filename, index=False)
    return df

def wrangle_zillow():
    ''' This function takes the zillow df csv, cleans it, and returns prep'd df'''

    file = 'zillow_2017.csv'

    df = pd.read_csv(file)# reads csv


    df = df.dropna() #drops all NaN values

    # renames columns for ease
    df.rename(columns={df.columns[0]: 'num_bedrooms', df.columns[1]: 'num_bathrooms', df.columns[2]: 'finished_sqft', df.columns[3]: 'tax_value'}, inplace=True)

    make_ints = ['num_bedrooms', 'finished_sqft', 'tax_value', 'yearbuilt']
    for col in make_ints:
        df[col] = df[col].astype(int)

    return df

def check_columns(df):
    """
    This function takes a pandas dataframe as input and returns
    a dataframe with information about each column in the dataframe. For
    each column, it returns the column name, the number of
    unique values in the column, the unique values themselves,
    the number of null values in the column, and the data type of the column.
    The resulting dataframe is sorted by the 'Number of Unique Values' column in ascending order.
​
    Args:
    - df: pandas dataframe
​
    Returns:
    - pandas dataframe
    """
    data = []
    # Loop through each column in the dataframe
    for column in df.columns:
        # Append the column name, number of unique values, unique values, number of null values, and data type to the data list
        data.append(
            [
                column,
                df[column].nunique(),
                df[column].unique(),
                df[column].isna().sum(),
                df[column].dtype
            ]
        )
    # Create a pandas dataframe from the data list, with column names 'Column Name', 'Number of Unique Values', 'Unique Values', 'Number of Null Values', and 'dtype'
    # Sort the resulting dataframe by the 'Number of Unique Values' column in ascending order
    return pd.DataFrame(
        data,
        columns=[
            "Column Name",
            "Number of Unique Values",
            "Unique Values",
            "Number of Null Values",
            "dtype"
        ],
    ).sort_values(by="Number of Unique Values")
















