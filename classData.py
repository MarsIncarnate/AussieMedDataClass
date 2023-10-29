import os
import pandas as pd

# Directory where the prescription data files are located
data_directory = './'

# List of years of data
years = ['2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021']

# Load the categorized medication data
categorized_medication_data_file = 'categorized_medication_data.xlsx'
categorized_df = pd.read_excel(categorized_medication_data_file, sheet_name=None)

# Iterate through each prescription data file for each year
for year in years:
    prescription_data_file = f'prescription_data_{year}.xlsx'
    if not os.path.isfile(prescription_data_file):
        print(f"Prescription data file for {year} not found.")
        continue

    # Load the prescription data for the current year
    year_data = pd.read_excel(prescription_data_file)

    # Iterate through each sheet in categorized_medication_data
    for sheet_name, sheet_df in categorized_df.items():
        # Merge the prescription data with categorized medication data based on medication name and form strength
        merged_data = pd.merge(sheet_df, year_data, left_on=['MEDICATION', 'FORM STRENGTH'], right_on=['GENERIC', 'FORM STRENGTH'], how='left')

        # Extract the prescription data column for the current year
        prescription_column = merged_data['Total']

        # Fill missing prescription data with 0
        prescription_column = prescription_column.fillna(0)

        # Update the corresponding column in the categorized_medication_data DataFrame
        categorized_df[sheet_name][year] = prescription_column

# Save the updated categorized_medication_data DataFrame back to the Excel file
with pd.ExcelWriter(categorized_medication_data_file, engine='openpyxl') as writer:
    for sheet_name, sheet_df in categorized_df.items():
        sheet_df.to_excel(writer, sheet_name=sheet_name, index=False)

print("Data population completed.")
