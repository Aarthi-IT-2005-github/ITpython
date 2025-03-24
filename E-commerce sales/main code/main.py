import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.frequent_patterns import apriori, association_rules
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error
import numpy as np
import warnings

# 1. Data Preprocessing
def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Handle missing values
    df.fillna(0, inplace=True)

    # Create seasonal sales columns
    df["Winter Sales"] = df["sales_month_12"] + df["sales_month_1"] + df["sales_month_2"]
    df["Spring Sales"] = df["sales_month_3"] + df["sales_month_4"] + df["sales_month_5"]
    df["Summer Sales"] = df["sales_month_6"] + df["sales_month_7"] + df["sales_month_8"]
    df["Fall Sales"] = df["sales_month_9"] + df["sales_month_10"] + df["sales_month_11"]

    # Save the preprocessed data
    df.to_csv(output_file, index=False)
    print("✅ Data Preprocessing Completed!")

# 2. Data Analysis and Visualization
def analyze_sales(data_file):
    df = pd.read_csv(data_file)

    # Seasonal sales distribution
    seasonal_sales = df[["Winter Sales", "Spring Sales", "Summer Sales", "Fall Sales"]].sum()

    # Plot seasonal sales (Fixed palette warning)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=seasonal_sales.index, y=seasonal_sales.values, hue=seasonal_sales.index, palette="coolwarm", legend=False)
    plt.title("Seasonal Sales Trend")  # Removed the emoji to avoid Tkinter warning
    plt.xlabel("Season")
    plt.ylabel("Total Sales")
    plt.show()

    # Top-selling categories
    top_categories = df.groupby("category")["sales_month_1"].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_categories.index, y=top_categories.values, palette="viridis")
    plt.title("Top-Selling Categories")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.show()

    print("✅ Sales Analysis Completed!")

# 3. Recommendation System using Association Rule Mining (Apriori)
def generate_recommendations(data_file):
    df = pd.read_csv(data_file)

    # Convert sales data into a transaction format
    basket = df.groupby(["product_id", "product_name"])[["sales_month_1", "sales_month_2", "sales_month_3"]].sum()

    # Convert sales values to boolean (True if sales > 0, False if sales == 0)
    basket = basket.apply(lambda col: col > 0)

    # Apply Apriori algorithm
    frequent_items = apriori(basket, min_support=0.01, use_colnames=True)
    
    # Suppress the specific warning about invalid value encountered in division
    warnings.filterwarnings("ignore", category=RuntimeWarning, message="invalid value encountered in divide")
    
    # Generate association rules
    rules = association_rules(frequent_items, metric="lift", min_threshold=1)

    # Handle NaN or infinite values in the result (e.g., lift calculation)
    rules = rules.replace([np.inf, -np.inf], np.nan)  # Replace inf values with NaN
    rules = rules.fillna(0)  # Replace NaNs with 0

    # Print top 5 recommendations by lift
    print(rules.sort_values(by="lift", ascending=False).head(5))
    print("✅ Recommendation System Completed!")

# 4. Predictive Model for Seasonal Products and Trends
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

    # Visualization: Predicted vs Actual values
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x=y_test, y=y_pred, color='blue', edgecolor='black')
    plt.title('Predicted vs Actual Sales for Month 12')
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')
    plt.show()

    # Residuals (Error distribution)
    residuals = y_test - y_pred
    plt.figure(figsize=(10, 6))
    sns.histplot(residuals, kde=True, color='red', bins=30)
    plt.title('Distribution of Residuals (Prediction Errors)')
    plt.xlabel('Residuals (Errors)')
    plt.ylabel('Frequency')
    plt.show()

    # Feature Importance: Coefficients of the Linear Model
    feature_names = X.columns
    feature_importance = model.coef_

    plt.figure(figsize=(10, 6))
    sns.barplot(x=feature_names, y=feature_importance, palette='viridis')
    plt.title('Feature Importance: Coefficients of the Linear Model')
    plt.xlabel('Features')
    plt.ylabel('Coefficient Value')
    plt.show()

# Main Program to Execute All Steps
def main():
    input_file = "D:/data science/E-commerce sales/source fiels/dataset-sales.csv"
    output_file = "D:/data science/E-commerce sales/source fiels/clean-dataset.csv"
    
    # Step 1: Data Preprocessing
    preprocess_data(input_file, output_file)

    # Step 2: Data Analysis and Visualization
    analyze_sales(output_file)

    # Step 3: Generate Recommendations
    generate_recommendations(output_file)

    # Step 4: Predictive Model Training for Seasonal Products
    train_sales_model(output_file)

if __name__ == "__main__":
    main()
