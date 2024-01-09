'''import pandas as pd
import xgboost as xgb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

def run_XGB_model(path):

    df = pd.read_csv(path)

    # Step 1: Extract features (X) and target variable (y)
    X = df.drop('Production_Total', axis=1)
    X = X.drop('Crop_Year', axis=1)
    X = X.drop('Yield_Mean', axis=1)  # Replace 'target_variable_column_name' with your actual target variable column name
    y = df['Yield_Mean']

    # Step 2: Split the data into training and testing sets
    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_features = poly.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)

    dtrain = xgb.DMatrix(X_train, label=y_train)
    dtest = xgb.DMatrix(X_test, label=y_test)

    # Set XGBoost parameters
    params = {
        'objective': 'reg:squarederror',  # for regression tasks
        'max_depth': 9,
        'learning_rate': 0.1,
        'subsample': 0.8,
        'colsample_bytree': 0.8,
        'eval_metric': 'rmse'  # root mean squared error
    }

    # Step 3: Create a linear regression model
    num_round = 100  # Number of boosting rounds
    model = xgb.train(params, dtrain, num_round)

    # Step 4: Fit the model to the training data
    model = xgb.train(params, dtrain, num_round)

    # Step 5: Make predictions on the test data
    y_pred = model.predict(dtest)

    # Step 6: Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')

    # Step 7: Visualize the results (optional)
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual values')
    plt.ylabel('Predicted values')
    plt.title('Actual vs Predicted values')
    plt.show()


    df.info()'''

import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

def run_XGB_model(path):

    df = pd.read_csv(path)

    # Step 1: Extract features (X) and target variable (y)
    X = df.drop('Production_Total', axis=1)
    X = X.drop('Crop_Year', axis=1)
    X = X.drop('Yield_Mean', axis=1)  # Replace 'target_variable_column_name' with your actual target variable column name
    y = df['Yield_Mean']

    # Step 2: Split the data into training and testing sets
    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_features = poly.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)

    param_grid = {
        'objective': ['reg:squarederror'],  # for regression tasks
        'eval_metric': ['rmse'],  # root mean squared error
        'max_depth': [3, 6, 9],
        'learning_rate': [0.01, 0.1, 0.2],
        'subsample': [0.8, 0.9, 1.0],
        'colsample_bytree': [0.8, 0.9, 1.0]
    }


    # Create a base XGBRegressor model
    model = XGBRegressor()

    cvk = KFold(n_splits=5, random_state=42, shuffle=True)

    # Create a parameter grid for GridSearchCV
   
    # Step 4: Apply GridSearchCV
    grid_search = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=cvk, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    # Step 5: Get the best hyperparameters
    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)

    # Step 6: Make predictions on the test data using the best model
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    # Step 7: Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')

    # Step 8: Visualize the results (optional)
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual values')
    plt.ylabel('Predicted values')
    plt.title('Actual vs Predicted values')
    plt.show()

    # Additional info (optional)
    df.info()