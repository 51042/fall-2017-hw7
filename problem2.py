import pandas as pd
import numpy as np

def search_by_zip(dataframe):
    """
    This function return a dataframe that contains restaurants that have failed an inspection within the last year within ZIP code 60661

    Args: dataframe - DataFrame containing the original data.
    Return: return a new dataframe which contains all rows from the old dataframe that match the criterion
    """
    emps = pd.read_csv(dataframe)
    emps['Inspection Date'] = emps['Inspection Date'].apply(lambda x: x[6:] + x[0:2] + x[3:5])
    fails = emps[(emps['Facility Type'] == 'Restaurant') & (emps['Inspection Date'] >= '20161101') & (emps['Results'] == 'Fail') & (emps['Zip'] == 60661.0)]
    return fails

def search_by_location(dataframe):
    """
    This function return a dataframe that contains restaurants that have failed an inspection within the last year within 0.5 miles from Professor home.

    Args: dataframe - DataFrame containing the original data.
    Return: return a sorted dataframe which contains all rows from the old dataframe that match the criterion
    """
    romano_latitude, romano_longitude = 41.8873906, -87.6459561
    emps = pd.read_csv(dataframe)
    emps['Inspection Date'] = emps['Inspection Date'].apply(lambda x: x[6:] + x[0:2] + x[3:5])
    emps['Distance'] = ((emps['Latitude'] - romano_latitude) ** 2 + (emps['Longitude'] - romano_longitude) **2).apply(np.sqrt)
    results = emps[(emps['Facility Type'] == 'Restaurant') & (emps['Inspection Date'] >= '20161101') & (emps['Results'] == 'Fail') & (emps['Distance'] <= 0.5)]
    results = results.sort_values('Distance')
    return results



if __name__ == "__main__":
    x = search_by_zip('Food_Inspections.csv')
    y = search_by_location('Food_Inspections.csv')
    print(x)
    print("_" * 100)
    print(y)
