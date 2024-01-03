import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

def run_random_forest_model(path):

    df = pd.read_csv(path)

    # Step 1: Extract features (X) and target variable (y)
    X = df.drop('Production_Total', axis=1)
    X = X.drop('Yield_Mean', axis=1)
    X = X.drop('Crop_Year', axis=1)
    y = df['Yield_Mean']

    # Step 2: Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Step 3: Define the hyperparameter grid for GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 4]
    }

    # Step 4: Create a RandomForestRegressor
    model = RandomForestRegressor(random_state=123)

    # Step 5: Create GridSearchCV object
    grid_search = GridSearchCV(model, param_grid, scoring='neg_mean_squared_error', cv=5)

    # Step 6: Fit the model to the training data with hyperparameter tuning
    grid_search.fit(X_train, y_train)

    # Step 7: Get the best hyperparameters
    best_params = grid_search.best_params_
    print("Best Hyperparameters:", best_params)

    # Step 8: Make predictions on the test data using the best model
    y_pred = grid_search.best_estimator_.predict(X_test)

    # Step 9: Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    print(f'Mean Squared Error: {mse}')
    print(f'Mean Absolute Error: {mae}')
    print(f'R-squared: {r2}')

    # Step 10: Visualize the results (optional)
    plt.scatter(y_test, y_pred)
    plt.xlabel('Actual values')
    plt.ylabel('Predicted values')
    plt.title('Actual vs Predicted values')
    plt.show()

    df.info()
