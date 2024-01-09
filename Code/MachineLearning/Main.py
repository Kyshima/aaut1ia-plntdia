def main():

    path_singular = 'C:/Users/Diana/Documents/GitHub/aaut1ia-plntdia/Code/MachineLearning/Dataset_Crop_Singular_3_anos.csv'
    path_multiple = 'C:/Users/Diana/Documents/GitHub/aaut1ia-plntdia/Code/MachineLearning/Dataset_Crop_Multiple_3.csv'
    path = 0

    print("Choose a model:")
    print("1. Linear Regression")
    print("2. Neural Network")
    print("3. Random Forest")
    print("4. XBG")
    print("5. LightGBM")
    print("6. Polynomial Regression")

    choice = input("Enter the number of the model you want to run: ")

    print("Choose a path:")
    print("1. Singular")
    print("2. Multiple")

    path_choice = input("Enter the number of the path you want to use: ")

    if path_choice == "1":
        path = path_singular
    
    elif path_choice == "2":
        path = path_multiple

    else:
         print("Invalid choice. Please enter a number between 1 and 2.")

    if choice == "1":
        from LinearRegression import run_linear_regression_model
        run_linear_regression_model(path)

    elif choice == "2":
        from NeuralNetwork import run_neural_network_model
        run_neural_network_model(path)

    elif choice == "3":
        from RandomForest import run_random_forest_model
        run_random_forest_model(path)
    
    elif choice == "4":
        from XGB import run_XGB_model
        run_XGB_model(path)

    elif choice == "5":
        from LightGBM import run_lightgbm_model
        run_lightgbm_model(path)

    elif choice == "6":
        from PolynomialRegression import run_polynomial_regression_model
        run_polynomial_regression_model(path)
        
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()