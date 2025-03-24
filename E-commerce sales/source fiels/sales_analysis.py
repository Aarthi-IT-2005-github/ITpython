import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_sales(data_file):
    df = pd.read_csv(data_file)

    # Seasonal sales distribution
    seasonal_sales = df[["Winter Sales", "Spring Sales", "Summer Sales", "Fall Sales"]].sum()

    # Plot seasonal sales
    plt.figure(figsize=(8, 5))
    sns.barplot(x=seasonal_sales.index, y=seasonal_sales.values, palette="coolwarm")
    plt.title("📊 Seasonal Sales Trend")
    plt.xlabel("Season")
    plt.ylabel("Total Sales")
    plt.show()

    # Top-selling categories
    top_categories = df.groupby("category")["sales_month_1"].sum().sort_values(ascending=False).head(5)
    plt.figure(figsize=(8, 5))
    sns.barplot(x=top_categories.index, y=top_categories.values, palette="viridis")
    plt.title("🔥 Top-Selling Categories")
    plt.xlabel("Category")
    plt.ylabel("Sales")
    plt.show()

    print("✅ Sales Analysis Completed!")

if __name__ == "__main__":
    analyze_sales("D:\data science\E-commerce sales\source fiels\clean-dataset.csv")
