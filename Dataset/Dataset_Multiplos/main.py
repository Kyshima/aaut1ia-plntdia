import numpy as np
import pandas as pd

df = pd.read_csv('APY.csv')
df.dropna(inplace=True)

df = df.drop(columns=['District ', 'Season'])

df_group = df.groupby(['State', 'Crop', 'Crop_Year'], as_index=False).agg(Area_Total=('Area', 'sum'),
                                                                          Production_Total=('Production', 'sum'),
                                                                          Yield_Mean=('Yield', 'mean'))
df_temp = []

for (state, year), group in df_group.groupby(['State', 'Crop_Year']):
        temp_data = {'State': state, 'Crop_Year': year}

        st = df_group[(df_group['State'] == state)]
        for i in range(1, 4):
            st_yr = st[(st['Crop_Year'] == year - i)]
            for crop in st_yr['Crop'].unique():

                ano_ant = st_yr[st_yr['Crop'] == crop]

                if not ano_ant.empty:
                    temp_data.update({
                        f'{crop}_Area_Ant_{i}': ano_ant['Area_Total'].iloc[0],
                        f'{crop}_Production_Ant_{i}': ano_ant['Production_Total'].iloc[0],
                    })
        df_temp.append(pd.DataFrame(temp_data, index=[0]))

df_temp = pd.concat(df_temp, axis=0, ignore_index=True)
df_temp.fillna(0, inplace=True)
print(df_temp)

df_merge = df_group.merge(df_temp, how='left', on=['State','Crop_Year'])


state_dummies = pd.get_dummies(df_merge['State'], prefix='State', dtype=int)
crop_dummies = pd.get_dummies(df_merge['Crop'], prefix='Crop', dtype=int)
df_dummies = pd.concat([state_dummies, crop_dummies], axis=1)
df_dummies = pd.concat([df_dummies, df_merge], axis=1)
df_dummies = df_dummies.drop(columns=['State', 'Crop'])
df_dummies.info()

df_dummies.to_csv("Dataset_Crop_Multiple_3.csv", index=False)

