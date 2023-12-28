import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

# Assuming you have a pandas DataFrame named 'df' with your dataset
df = pd.read_csv('Dataset_Crop_Multiple_3.csv')

# Step 1: Extract features (X) and target variable (y)
X = df.drop('Production_Total', axis=1)
X = X.drop('Yield_Mean', axis=1)  # Replace 'target_variable_column_name' with your actual target variable column name
y = df['Yield_Mean']

# Step 2: Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Step 3: Create a linear regression model
model = LinearRegression()

# Step 4: Fit the model to the training data
model.fit(X_train, y_train)

# Step 5: Make predictions on the test data
y_pred = model.predict(X_test)

# Step 6: Evaluate the model
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


df.info()


#import numpy as np
#import pandas as pd
#from sklearn.model_selection import train_test_split
#from sklearn.preprocessing import StandardScaler
#from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
#import tensorflow as tf
#from tensorflow.keras.models import Sequential
#from tensorflow.keras.layers import Dense
#
## Assuming you have a pandas DataFrame named 'df' with your dataset
#df = pd.read_csv('Dataset_Crop_Multiple_3.csv')
##
### Step 1: Extract features (X) and target variable (y)
#X = df.drop('Production_Total', axis=1)
#X = X.drop('Yield_Mean', axis=1).values  # Features
#y = df['Yield_Mean'].values  # Target variable
#
## Step 2: Split the data into training and testing sets
#X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
#
## Step 3: Standardize the data (optional but often beneficial for neural networks)
#scaler = StandardScaler()
#X_train = scaler.fit_transform(X_train)
#X_test = scaler.transform(X_test)
#
## Step 4: Build the neural network model
#model = Sequential()
#model.add(Dense(64, activation='relu', input_shape=(X_train.shape[1],)))
#model.add(Dense(32, activation='relu'))
#model.add(Dense(1, activation='linear'))  # Linear activation for regression
#
## Step 5: Compile the model
#model.compile(optimizer='adam', loss='mean_squared_error')
#
## Step 6: Train the model
#model.fit(X_train, y_train, epochs=50, batch_size=32, validation_split=0.2, verbose=1)
#
## Step 7: Evaluate the model
#y_pred = model.predict(X_test)
#
#mse = mean_squared_error(y_test, y_pred)
#mae = mean_absolute_error(y_test, y_pred)
#r2 = r2_score(y_test, y_pred)
#
#print(f'Mean Squared Error: {mse}')
#print(f'Mean Absolute Error: {mae}')
#print(f'R-squared: {r2}')
