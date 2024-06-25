"""In this module we have replaced the steps with functions. 

* value in doing this
* outcome...

however these functions are only available to you in this script. 
If you want to make these functions available to you as installable modules, 
that is when a package comes into play. 

"""

import pandas as pd
import os


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


def categorize_snow(x):
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


def add_snowfall_category(data):
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


def main():
    """
    Main function to execute the workflow.
    """
    base_path = os.path.join("example-scripts", "data.csv")

    # Load and clean the data
    data = load_data(base_path)
    print(data)

    # Add snowfall category
    data = add_snowfall_category(data)

    # Summarize the data
    summary = summarize_data(data)

    # Print the results
    print("Data with snowfall categories:")
    print(data)
    print("\nSummary of data by snowfall category:")
    print(summary)


if __name__ == "__main__":
    main()
