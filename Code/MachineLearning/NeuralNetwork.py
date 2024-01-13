import pandas as pd
import numpy as np

import tensorflow as tf
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.model_selection import KFold, GridSearchCV, train_test_split
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

def run_neural_network_model(path):

    df = pd.read_csv(path)

    # Step 1: Extract features (X) and target variable (y)
    X = df.drop('Production_Total', axis=1)
    X = X.drop('Crop_Year', axis=1)
    X = X.drop('Yield_Mean', axis=1).values  # Features
    y = df['Yield_Mean'].values  # Target variable

    # Step 2: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Define the base model for KerasClassifier
    def create_model(hidden_units=64, input_dim=8, learning_rate=0.001, optimizer='adam'):
        model = Sequential()
        model.add(Dense(hidden_units, input_dim=input_dim, activation='relu'))
        model.add(Dense(1, activation='linear'))

        # Use specified optimizer and learning rate
        if optimizer == 'adam':
            optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate)
        elif optimizer == 'rmsprop':
            optimizer = tf.keras.optimizers.RMSprop(learning_rate=learning_rate)
        else:
            raise ValueError(f"Unsupported optimizer: {optimizer}")

        model.compile(optimizer=optimizer, loss='mean_squared_error')
        return model

    kfold = KFold(n_splits=2, shuffle=True, random_state=42)

    # Define the hyperparameters to search
    param_grid = {
        'hidden_units': [32, 64],
        'epochs': [25, 50, 100],
        'batch_size': [32, 64],
        'optimizer': ['adam', 'rmsprop'],
        'learning_rate': [0.001, 0.01]
    }

    # Create GridSearchCV
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    model = tf.keras.wrappers.scikit_learn.KerasRegressor(build_fn=create_model, input_dim=X_train.shape[1], verbose=1)
    grid = GridSearchCV(estimator=model, param_grid=param_grid, scoring='neg_mean_squared_error', cv=kfold)
    grid_result = grid.fit(X_train, y_train)

    # Get the best model
    best_model = grid_result.best_estimator_.model

    # Step 7: Evaluate the model
    y_pred = best_model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    best_params = grid_result.best_params_
    print("Best Hyperparameters:", best_params)
    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')