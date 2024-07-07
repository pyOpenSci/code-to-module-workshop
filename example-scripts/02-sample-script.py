"""In this module we have replaced the steps with functions. 

* This makes your code more concise 
* It also reduces the number of variables stored in your environment 
    * Variables within a function are contained in the unique namespace of that function

To run this script at the command line you can use. 

    python example-scripts/02-sample-script.py

However these functions are only available to you in this script. 
If you want to make these functions available to you as installable modules, 
that is when a package comes into play. 

"""

import pandas as pd


def load_data(filepath):

    print(filepath)
    # Load the data and replace -999 with NaN
    return pd.read_csv(filepath, na_values=-999)


def categorize_snow(x):
    if x > 15:
        return "High"
    elif x < 5:
        return "Low"
    else:
        return "Medium"


def add_snowfall_category(data):
    data["snowfall_category"] = data["average_snowfall"].apply(categorize_snow)
    return data


def summarize_data(data):
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
    data_path = "https://raw.githubusercontent.com/pyOpenSci/code-to-module-workshop/main/example-scripts/data.csv"

    # Load and clean the data
    data = load_data(data_path)
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
