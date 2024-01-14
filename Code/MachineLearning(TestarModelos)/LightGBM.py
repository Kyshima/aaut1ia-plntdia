import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from lightgbm import LGBMRegressor
from sklearn.model_selection import KFold
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt
from lightgbm.callback import early_stopping

def run_lightgbm_model(path):
    df = pd.read_csv(path)

    X = df.drop('Production_Total', axis=1)
    X = X.drop('Yield_Mean', axis=1)
    X = X.drop('Crop_Year', axis=1)
    y = df['Yield_Mean']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    param_grid = {
        'n_estimators': [100, 200],
        'learning_rate': [0.1],
        'max_depth': [5, 9], 
        'num_leaves': [31, 127],
        'subsample': [0.8],
        'colsample_bytree': [0.8, 1.0],
        'reg_alpha': [0, 0.1, 1.0],
        'reg_lambda': [0, 1.0],
        'min_child_samples': [10, 30],
        'min_child_weight': [1e-2, 1],
        'objective': ['regression'],
    }

    model = LGBMRegressor(random_state=123)

    cvk = KFold(n_splits=5, random_state=42, shuffle=True)

    grid_search = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=cvk, verbose=2, n_jobs=-1)

    grid_search.fit(X_train, y_train, eval_set=[(X_test, y_test)], eval_metric='rmse', callbacks=[early_stopping(stopping_rounds=10, verbose=False)])

    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)

    y_pred = grid_search.best_estimator_.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')

    df.info()