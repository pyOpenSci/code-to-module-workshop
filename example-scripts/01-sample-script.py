"""Module 1 - 

* What challenges do you see in this code? 
* How could we make it more concise? 
* How could we make it less - copy pasta and more reusable? 
* What would happen if you needed to process multiple csv files? 
* Is this code easily shareable?
"""

import pandas as pd

# Load the data -- this requires an internet connection
data_path = "https://raw.githubusercontent.com/pyOpenSci/code-to-module-workshop/main/example-scripts/data.csv"
data = pd.read_csv(data_path)
data.columns

print(data.head())

# Filter rows where the value in 'column1' is greater than 10
sites_more_snow = data[data["average_snowfall"] > 10]

print(f"Sites with more than 15 inches of snow: \n{sites_more_snow}")

avg_temp_more_snow = sites_more_snow["average_temperature"].mean()
print(f"The mean temp for sites with more snow is {avg_temp_more_snow}")

# Sites with less snow - calc average temp
sites_less_snow = data[data["average_snowfall"] < 5]
avg_temp_less_snow = sites_less_snow["average_temperature"].mean()

print(f"The mean temp for sites with less snow is {avg_temp_less_snow}")


# Filter rows where the average snowfall is between 5 and 15 inches
sites_medium_snow = data[
    (data["average_snowfall"] >= 5) & (data["average_snowfall"] <= 15)
]

print(f"Sites with snowfall between 5 and 15 inches:\n{sites_medium_snow}")

# Calculate the mean temperature for sites with medium snow
avg_temp_medium_snow = sites_medium_snow["average_temperature"].mean()
print(
    f"The mean temperature for sites with medium snow is {avg_temp_medium_snow}"
)
