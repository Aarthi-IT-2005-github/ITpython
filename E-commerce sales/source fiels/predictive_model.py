import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import matplotlib.pyplot as plt
import seaborn as sns

def train_sales_model(data_file):
    df = pd.read_csv(data_file)

    # Features and Target
    X = df[["price", "review_score", "sales_month_1", "sales_month_2", "sales_month_3"]]
    y = df["sales_month_12"]  # Predicting future sales

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict and evaluate
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    print(f"📉 Mean Absolute Error: {mae}")
    print("✅ Predictive Model Training Completed!")

    # Visualization 1: Predicted vs Actual values
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, color='blue', edgecolor='black')
    plt.title('Predicted vs Actual Sales for Month 12')
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.show()

    # Visualization 2: Residuals (Error distribution)
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True, color='red', bins=30)
    plt.title('Distribution of Residuals (Prediction Errors)')
    plt.xlabel('Residuals (Errors)')
    plt.ylabel('Frequency')
    plt.show()

    # Visualization 3: Feature Importance (Coefficients of the Linear Model)
    feature_names = X.columns
    feature_importance = model.coef_

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_names, y=feature_importance, palette='viridis')
    plt.title('Feature Importance: Coefficients of the Linear Model')
    plt.xlabel('Features')
    plt.ylabel('Coefficient Value')
    plt.show()

if __name__ == "__main__":
    train_sales_model("D:/data science/E-commerce sales/source fiels/clean-dataset.csv")
