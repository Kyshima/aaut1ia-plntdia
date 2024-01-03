import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import layers
from kerastuner.tuners import RandomSearch

def run_neural_network_model(path):

    df = pd.read_csv(path)

    best_hps = {
        'units_input': 128,
        'activation_input': 'sigmoid',
        'num_layers': 1,
        'units_0': 192,
        'activation_0': 'relu',
        'dropout_0': 0.3,
        'units_1': 256,
        'activation_1': 'sigmoid',
        'dropout_1': 0.2,
        'learning_rate': 0.0083605,
        'units_2': 160,
        'activation_2': 'relu',
        'dropout_2': 0.2
    }

    # Step 1: Extract features (X) and target variable (y)
    X = df.drop('Production_Total', axis=1)
    X = X.drop('Yield_Mean', axis=1).values  # Features
    y = df['Yield_Mean'].values  # Target variable

    # Step 2: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Step 3: Standardize the data (optional but often beneficial for neural networks)
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Step 4: Build the neural network model
    model = Sequential()
    model.add(Dense(best_hps['units_input'], activation=best_hps['activation_input'], input_shape=(X_train.shape[1],)))

    for i in range(best_hps['num_layers']):
        model.add(Dense(best_hps[f'units_{i}'], activation=best_hps[f'activation_{i}']))
        model.add(layers.Dropout(best_hps[f'dropout_{i}']))

    model.add(Dense(1, activation='linear'))  # Linear activation for regression

    # Step 5: Compile the model
    optimizer = tf.keras.optimizers.Adam(learning_rate=best_hps['learning_rate'])
    model.compile(optimizer=optimizer, loss='mean_squared_error')

    # Step 6: Train the model
    model.fit(X_train, y_train, epochs=100)

    # Step 7: Evaluate the model
    y_pred = model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')