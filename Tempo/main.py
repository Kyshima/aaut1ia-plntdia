import numpy as np
import pandas as pd

df = pd.read_csv('APY.csv')

df.dropna(inplace=True)

seasons_array = {
    'Kharif': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
    'Rabi': [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1],
    'Autumn': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0],
    'Summer': [0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0],
    'Whole_year': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'Winter': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1]
}

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November','December']
df[months] = None

condition = (df['Season'] == 'Kharif')
df.loc[(df['Season'] == 'Kharif'), months] = np.array(seasons_array['Kharif'])
df.loc[(df['Season'] == 'Rabi'), months] = np.array(seasons_array['Rabi'])
df.loc[(df['Season'] == 'Autumn'), months] = np.array(seasons_array['Autumn'])
df.loc[(df['Season'] == 'Summer'), months] = np.array(seasons_array['Summer'])
df.loc[(df['Season'] == 'Whole_year'), months] = np.array(seasons_array['Whole_year'])
df.loc[(df['Season'] == 'Winter'), months] = np.array(seasons_array['Winter'])

print(df)
