"""In this module we have replaced the steps with functions. 

* value in doing this
* outcome...

however these functions are only available to you in this script. 
If you want to make these functions available to you as installable modules, 
that is when a package comes into play. 

"""

import os

from my_module import load_data, summarize_data, categorize_snowfall_amount


def main():    """
    Main function to execute the workflow.
    """
    base_path = os.path.join("example-scripts", "data.csv")

    # Load and clean the data
    data = load_data(base_path)
    print(data)

    # Add snowfall category
    data = categorize_snowfall_amount(data)

    # Summarize the data
    summary = summarize_data(data)

    # Print the results
    print("Data with snowfall categories:")
    print(data)
    print("\nSummary of data by snowfall category:")
    print(summary)


if __name__ == "__main__":
    main()
