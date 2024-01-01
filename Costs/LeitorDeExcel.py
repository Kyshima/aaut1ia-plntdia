import pandas as pd
import json
import os

excel_file_path = r'C:/Users/Diana/Desktop/Faculdade/2018-19.xlsx'

excel_file_name = os.path.splitext(os.path.basename(excel_file_path))[0]

xl = pd.ExcelFile(excel_file_path, engine='openpyxl')

result_dict = {}

for sheet_name in xl.sheet_names:

    # Read the sheet into a DataFrame
    df = xl.parse(sheet_name, header=None)

    # Extract crop name, states, and costs
    crop_name = sheet_name
    states = df.iloc[3, 3:].tolist()
    costs = df.iloc[-1, 3:].tolist()

    # Create a dictionary for the current crop
    crop_dict = dict(zip(states, costs))

    # Add the crop dictionary to the result dictionary
    result_dict[crop_name] = crop_dict

json_result = json.dumps(result_dict, indent=2)

with open(excel_file_name +'.json', 'w') as json_file:
    json_file.write(json_result)

print("JSON file has been created successfully.")