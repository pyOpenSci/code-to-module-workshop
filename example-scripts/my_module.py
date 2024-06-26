"""This modules contains functions that help a user open and process snowfall 
data.  

Because this is only a python module (a .py file), it can only be imported
into Python if it is in the same directory as your code.

This approach is useful to organize your code for a single analysis where you 
just want to store functions (or classes) in a separate place.However, if 
you want to be able to install this code into an environment so you can 
import functions (or classes) from anywhere that can access that environment,
then you will want to create a package.


"""

import pandas as pd


def load_data(filepath):
    """
    Load data from a CSV file and clean it.

    Parameters
    ----------
    filepath : str
        Path to the CSV file.

    Returns
    -------
    pd.DataFrame
        Loaded and cleaned data as a DataFrame.
    """

    print(filepath)
    # Load the data and replace -999 with NaN
    return pd.read_csv(filepath, na_values=-999)


def define_snow_categories(x):
    """
    Categorize snowfall amount.

    Parameters
    ----------
    x : float
        Snowfall amount.

    Returns
    -------
    str
        Category of snowfall (High, Medium, Low).
    """
    if x > 15:
        return "High"
    elif x < 5:
        return "Low"
    else:
        return "Medium"


def categorize_snowfall_amount(data):
    """
    Add a column categorizing the snowfall amount.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing snowfall data.

    Returns
    -------
    pd.DataFrame
        DataFrame with an added column for snowfall category.
    """
    data["snowfall_category"] = data["average_snowfall"].apply(categorize_snow)
    return data


def summarize_data(data):
    """
    Summarize the data based on snowfall category.

    Parameters
    ----------
    data : pd.DataFrame
        DataFrame containing categorized snowfall data.

    Returns
    -------
    pd.DataFrame
        Summary DataFrame with average snowfall, average temperature, and site count.
    """
    summary = data.groupby("snowfall_category").agg(
        avg_snowfall=("average_snowfall", "mean"),
        avg_temperature=("average_temperature", "mean"),
        site_count=("site", "count"),
    )
    return summary
