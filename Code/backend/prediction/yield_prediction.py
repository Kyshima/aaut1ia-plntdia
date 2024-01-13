import pandas as pd
import joblib

#model = loaded_rf = joblib.load("best_random_forest_model.joblib")
model = loaded_rf = joblib.load('C:/Users/Diana/Documents/GitHub/aaut1ia-plntdia/Code/backend/prediction/best_random_forest_model.joblib')

def predict(State, Crop, Area, prodAnt1, areaAnt1, prodAnt2, areaAnt2, prodAnt3, areaAnt3):
    columns = [
        'State_Andaman and Nicobar Island', 'State_Andhra Pradesh', 'State_Arunachal Pradesh', 'State_Assam',
        'State_Bihar',
        'State_CHANDIGARH', 'State_Chhattisgarh', 'State_Dadra and Nagar Haveli', 'State_Daman and Diu', 'State_Delhi',
        'State_Goa', 'State_Gujarat', 'State_Haryana', 'State_Himachal Pradesh', 'State_Jammu and Kashmir',
        'State_Jharkhand',
        'State_Karnataka', 'State_Kerala', 'State_Laddak', 'State_Madhya Pradesh', 'State_Maharashtra', 'State_Manipur',
        'State_Meghalaya', 'State_Mizoram', 'State_Nagaland', 'State_Odisha', 'State_Puducherry', 'State_Punjab',
        'State_Rajasthan', 'State_Sikkim', 'State_THE DADRA AND NAGAR HAVELI', 'State_Tamil Nadu', 'State_Telangana',
        'State_Tripura', 'State_Uttar Pradesh', 'State_Uttarakhand', 'State_West Bengal', 'Crop_Arecanut',
        'Crop_Arhar/Tur',
        'Crop_Bajra', 'Crop_Banana', 'Crop_Barley', 'Crop_Black pepper', 'Crop_Cardamom', 'Crop_Cashewnut',
        'Crop_Castor seed',
        'Crop_Coconut ', 'Crop_Coriander', 'Crop_Cotton(lint)', 'Crop_Cowpea(Lobia)', 'Crop_Dry chillies',
        'Crop_Garlic',
        'Crop_Ginger', 'Crop_Gram', 'Crop_Groundnut', 'Crop_Guar seed', 'Crop_Horse-gram', 'Crop_Jowar', 'Crop_Jute',
        'Crop_Khesari', 'Crop_Linseed', 'Crop_Maize', 'Crop_Masoor', 'Crop_Mesta', 'Crop_Moong(Green Gram)',
        'Crop_Moth',
        'Crop_Niger seed', 'Crop_Oilseeds total', 'Crop_Onion', 'Crop_Other  Rabi pulses', 'Crop_Other Cereals',
        'Crop_Other Kharif pulses', 'Crop_Other Summer Pulses', 'Crop_Peas & beans (Pulses)', 'Crop_Potato',
        'Crop_Ragi',
        'Crop_Rapeseed &Mustard', 'Crop_Rice', 'Crop_Safflower', 'Crop_Sannhamp', 'Crop_Sesamum', 'Crop_Small millets',
        'Crop_Soyabean', 'Crop_Sugarcane', 'Crop_Sunflower', 'Crop_Sweet potato', 'Crop_Tapioca', 'Crop_Tobacco',
        'Crop_Turmeric', 'Crop_Urad', 'Crop_Wheat', 'Crop_other oilseeds', 'Area_Total', 'Area_Ant_1',
        'Production_Ant_1',
        'Area_Ant_2', 'Production_Ant_2', 'Area_Ant_3', 'Production_Ant_3'
    ]

    df = pd.DataFrame(columns=columns)
    df.loc[0] = 0

    columns_to_update = ['State_' + State, 'Crop_' + Crop, 'Area_Total',
                                'Area_Ant_1', 'Production_Ant_1', 'Area_Ant_2',
                         'Production_Ant_2', 'Area_Ant_3',
                         'Production_Ant_3']

    df.loc[0, columns_to_update] = [1, 1, Area, areaAnt1, prodAnt1,
                                    areaAnt2, prodAnt2,
                                    areaAnt3, prodAnt3]

    predictions = model.predict(df)
    return predictions[0]