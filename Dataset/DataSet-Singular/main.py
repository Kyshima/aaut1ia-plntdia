import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('APY.csv')
df.dropna(inplace=True)

df = df.drop(columns=['District ', 'Season'])

df_group = df.groupby(['State', 'Crop', 'Crop_Year'], as_index=False).agg(Area_Total=('Area', 'sum'),
                                                                          Production_Total=('Production', 'sum'),
                                                                          Yield_Mean=('Yield', 'mean'))

# Sort the DataFrame for efficient searching
df_group.sort_values(['State', 'Crop', 'Crop_Year'], inplace=True)

# Create columns for the previous years
for i in range(1, 4):
    df_group[f'Area_Ant_{i}'] = df_group.groupby(['State', 'Crop'])['Area_Total'].shift(i)
    df_group[f'Production_Ant_{i}'] = df_group.groupby(['State', 'Crop'])['Production_Total'].shift(i)

# Drop NaN rows resulting from shifting
df_group.dropna(subset=[f'Area_Ant_{i}' for i in range(1, 4)], inplace=True)

# Reset the index after sorting and dropping NaN rows
df_group.reset_index(drop=True, inplace=True)

# df_group.dropna(inplace=True)
state_dummies = pd.get_dummies(df_group['State'], prefix='State', dtype=int)
crop_dummies = pd.get_dummies(df_group['Crop'], prefix='Crop', dtype=int)
df_dummies = pd.concat([state_dummies, crop_dummies], axis=1)
df_dummies = pd.concat([df_dummies, df_group], axis=1)
df_dummies = df_dummies.drop(columns=['State', 'Crop'])
df_dummies.info()

df_dummies.to_csv("Dataset_Crop_Singular_3_anos.csv", index=False)