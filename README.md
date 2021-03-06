# CGI ACADEMY PYTHON MINI PROJECT #1

Python mini-project for CGI Data Engineer Academy

[Trello Board](https://trello.com/b/8Nslkzg7/python-project)

## About the Project

In this project you will be expected to extract data, transform and/or clean data, and save it as a new file using Python/Pandas. The output will be used in exercise #2.  

### Instructions

The Parking Citation Dataset is a public dataset containing millions of records of information about parking tickets for a county in California. We will only be using a subset of this data (1 million rows) for this assignment. You can see the [whole dataset here](https://data.lacity.org/Transportation/Parking-Citations/wjz9-h9np/data).

All you need to do is go into your Databricks Community Edition, click on the Workspace menu item, and either in your user’s workspace or in the shared space, right click and select ‘Import’. Once the import menu pops up, change the radio button on the top to ‘URL’ and enter the following URL:  

https://databricks-prod-cloudfront.cloud.databricks.com/public/4027ec902e239c93eaaa8714f173bcfc/599323449357213/1051081740767045/956079641523452/latest.html 

This will import the Databricks archive notebook needed for this exercise into your workspace. If this gives you issues I have also exported the notebook in the 0522 - Data Engineer Training > Cohort 3 - May 2022 > Mini Projects > Mini Project #1 folder and it can be imported similarly but instead of using the URL radio button, you would keep it as is on the import pop up with the ‘File’ radio button selected and navigate to where you downloaded the Databricks archive notebook in your file system to import it.

### Steps

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

## PLAN

- Work on project in Jupyter Notebooks in VSCode and paste into databricks

## Data Preparation

1. Drop `Unnamed:_0.1` column - import artifact.
2. Change `Ticket_number` data type to string.
3. Change `Issue_Date` data type to datetime.
4. Drop data with incomplete location data (lat long like 99999 or NA) 
5. Add `Distance_to_pointA` column with distance in feet to point at (6439997, 1802686).


## Data Dictionary

| Feature                | Datatype       | Definition                              | Description                      |
| :--------------------- | :------------- | :-------------------------------------- | :------------------------------- |
| Ticket_number          | object         | Ticket number                           | Original - converted to string   |
| Issue_Date             | datetime64[ns] | MM/dd/yyyy                              | Original - converted to datetime |
| Issue_time             | *float64*      | 24-hour time  hhmm.0                    | Original                         |
| Meter_Id               | object         |                                         | Original                         |
| Marked_Time            | float64        |                                         | Original                         |
| RP_State_Plate         | object         | Plate state abbreviation                | Original                         |
| Plate_Expiry_Date      | *float64*      | yyyymm.0                                | Original                         |
| VIN                    | object         | Vehicle Identification Number           | Original                         |
| Make                   | object         | Car make abbreviation                   | Original                         |
| Body_Style             | object         | Body style abbreviation                 | Original                         |
| Agency                 | float64        | Integer - PDF with corresponding agency | Original                         |
| Violation_code         | object         |                                         | Original                         |
| Violation_Description  | object         |                                         | Original                         |
| Fine_amount            | float64        |                                         | Original                         |
| Latitude               | float64        |                                         | Original                         |
| Longitude              | float64        |                                         | Original                         |
| Agency_Description     | float64        |                                         | Original                         |
| Color_Description      | float64        |                                         | Original                         |
| Body_Style_Description | float64        |                                         | Original                         |
| Distance_to_pointA     |                | Distance to (6439997, 1802686)          | Engineered                       |
|                        |

## Steps to reproduce

### On Databricks Community

- [x] Read this README.md
- [ ] Env yml file


### On your local machine

- [ ] d
- [ ] 