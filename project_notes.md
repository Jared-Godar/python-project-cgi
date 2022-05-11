# PYTHON MINI-PROJECT #1

In this project you will be expected to extract data, transform and/or clean data, and save it as a new file using Python/Pandas. The output will be used in exercise #2.  

## Instructions

The Parking Citation Dataset is a public dataset containing millions of records of information about parking tickets for a county in California. We will only be using a subset of this data (1 million rows) for this assignment. You can see the [whole dataset here](https://data.lacity.org/Transportation/Parking-Citations/wjz9-h9np/data).

All you need to do is go into your Databricks Community Edition, click on the Workspace menu item, and either in your user’s workspace or in the shared space, right click and select ‘Import’. Once the import menu pops up, change the radio button on the top to ‘URL’ and enter the following URL:  

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/599323449357213/1051081740767045/956079641523452/latest.html 

This will import the Databricks archive notebook needed for this exercise into your workspace. If this gives you issues I have also exported the notebook in the 0522 - Data Engineer Training > Cohort 3 - May 2022 > Mini Projects > Mini Project #1 folder and it can be imported similarly but instead of using the URL radio button, you would keep it as is on the import pop up with the ‘File’ radio button selected and navigate to where you downloaded the Databricks archive notebook in your file system to import it.

- [ ] Extract CSV and JSON files and append these files into a Pandas DataFrame. (If you have a problem reading json file, it is ok to skip reading Json file and continue with only records in csv file.)
- [ ] Remove the spaces from column headers
- [ ] Change data types
- [ ] Check if a column has any digits in its values
- [ ] Write a function to check if a column only has "Alphabet" values
- [ ] Write a function to check if a column only has "Numeric" values
- [ ] Add a column "Distance_to_pointA", calculating the distance between each point and point A
- [ ] Handle duplicates
- [ ] Drop columns with 70% missing values
- [ ] Remove a few records based on a condition
- [ ] Fill missing values for a column
- [ ] Split a column into several columns
- [ ] Save the final modified dataframe into a partitioned parquet file! (If you are not able to save it as a parquet file, go ahead and save it as a csv file without any partitioning!)

## Deliverables

- [ ] Save the dataframe as Parquet files partitioned by the “Issue_year” column (or only ONE csv file).
- [ ] Export the notebook as an `.html` file with following naming convention `“FNameLName_DE1”` to C`ohort 3 - May 2022 > Mini Projects > Completed Assignments > Mini Project #1`. We will be reviewing outputs and providing feedback, as necessary.
