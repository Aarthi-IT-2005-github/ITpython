import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import numpy as np
import warnings

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

if __name__ == "__main__":
    generate_recommendations("D:/data science/E-commerce sales/source fiels/clean-dataset.csv")
a
