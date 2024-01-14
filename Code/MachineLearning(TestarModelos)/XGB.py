import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV, KFold
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from xgboost import XGBRegressor
import matplotlib.pyplot as plt

def run_XGB_model(path):

    df = pd.read_csv(path)

    X = df.drop('Production_Total', axis=1)
    X = X.drop('Crop_Year', axis=1)
    X = X.drop('Yield_Mean', axis=1) 
    y = df['Yield_Mean']

    poly = PolynomialFeatures(degree=2, include_bias=False)
    poly_features = poly.fit_transform(X)
    X_train, X_test, y_train, y_test = train_test_split(poly_features, y, test_size=0.3, random_state=42)

    param_grid = {
        'objective': ['reg:squarederror'],
        'eval_metric': ['rmse'],
        'max_depth': [3, 6, 9],
        'learning_rate': [0.01, 0.1, 0.2],
        'subsample': [0.8, 0.9, 1.0],
        'colsample_bytree': [0.8, 0.9, 1.0]
    }

    model = XGBRegressor()

    cvk = KFold(n_splits=5, random_state=42, shuffle=True)
   
    grid_search = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=cvk, n_jobs=-1, verbose=2)
    grid_search.fit(X_train, y_train)

    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)

    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')