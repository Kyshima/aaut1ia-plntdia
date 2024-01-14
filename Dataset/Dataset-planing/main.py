import json

import numpy as np
import pandas as pd

df = pd.read_csv('D:/Faculdade/mestrado/projeto2semestre/aaut1ia-plntdia/Dataset/Dataset-planing/APY.csv')
df.dropna(inplace=True)

df = df.drop(columns=['District ', 'Season'])

df_group = df.groupby(['State', 'Crop', 'Crop_Year'], as_index=False).agg(Area_Total=('Area', 'sum'),
                                                                          Production_Total=('Production', 'sum'),
                                                                          Yield_Mean=('Yield', 'mean'))
df_temp = []

for year in range(4, 22):
    if year < 9:
        f = open('D:/Faculdade/mestrado/projeto2semestre/aaut1ia-plntdia/DataSet/Dataset-planing/DataSet/200' + str(year) + '-0' + str(year + 1) + '.json')
    elif year == 9:
        f = open('D:/Faculdade/mestrado/projeto2semestre/aaut1ia-plntdia/DataSet/Dataset-planing/DataSet/200' + str(year) + '-' + str(year + 1) + '.json')
    else:
        f = open('D:/Faculdade/mestrado/projeto2semestre/aaut1ia-plntdia/DataSet/Dataset-planing/DataSet/20' + str(year) + '-' + str(year + 1) + '.json')

    data = json.load(f)
    for crop in data:
        if "Coconut" not in crop:
            for state in data[crop]["Total Cost"]:
                if "NaN" not in state:
                    if year < 10:
                        temp_data = {
                            'Crop_Year': 2000 + year,
                            'State': state,
                            'Crop': crop,
                            'Total Cost': data[crop]["Total Cost"][state],
                            'ProdCost': data[crop]["ProdCost"][state],
                            'CultCost': data[crop]["CultCost"][state],
                            'OperCost': data[crop]["OperCost"][state],
                            'FixedCost': data[crop]["FixedCost"][state]
                        }
                    else:
                        temp_data = {
                            'Crop_Year': 2000 + year,
                            'State': state,
                            'Crop': crop,
                            'Total Cost': data[crop]["Total Cost"][state],
                            'ProdCost': data[crop]["ProdCost"][state],
                            'CultCost': data[crop]["CultCost"][state],
                            'OperCost': data[crop]["OperCost"][state],
                            'FixedCost': data[crop]["FixedCost"][state]
                        }
                    df_temp.append(pd.DataFrame(temp_data, index=[0]))

df_temp = pd.concat(df_temp, axis=0, ignore_index=True)

df_temp['State'] = np.where(df_temp['State'] == "Chhatisgarh", "Chhattisgarh", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "Pnnjab", "Punjab", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "Orissa", "Odisha", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "A.P.", "Andhra Pradesh", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "Maharastra", "Maharashtra", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "Jharkhand ", "Jharkhand", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "Kerala ", "Kerala", df_temp['State'])
df_temp['State'] = np.where(df_temp['State'] == "Gujatat", "Gujarat", df_temp['State'])

df_temp['Crop'] = np.where(df_temp['Crop'] == "R&M", "Rapeseed &Mustard", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Cotton", "Cotton(lint)", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Lentil", "Masoor", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Nigerseed", "Niger seed", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "VFCTobacco", "Tobacco", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Arhar", "Arhar/Tur", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Peas", "Peas & beans (Pulses)", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Saffflower ", "Safflower", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Paddy", "Rice", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "R & M", "Rapeseed &Mustard", df_temp['Crop'])
df_temp['Crop'] = np.where(df_temp['Crop'] == "Moong", "Moong(Green Gram)", df_temp['Crop'])



df_merge = df_temp.merge(df_group, how='left', on=['State','Crop_Year', 'Crop'])
df_merge.dropna(inplace=True)
print(df_merge)

print(df_merge['State'].unique())


df_merge.to_csv("Dataset_Planning.csv", index=False)

