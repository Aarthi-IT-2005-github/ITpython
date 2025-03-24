import pandas as pd

def preprocess_data(input_file, output_file):
    df = pd.read_csv(input_file)

    # Check for missing values
    df.fillna(0, inplace=True)

    # Create seasonal sales columns
    df["Winter Sales"] = df["sales_month_12"] + df["sales_month_1"] + df["sales_month_2"]
    df["Spring Sales"] = df["sales_month_3"] + df["sales_month_4"] + df["sales_month_5"]
    df["Summer Sales"] = df["sales_month_6"] + df["sales_month_7"] + df["sales_month_8"]
    df["Fall Sales"] = df["sales_month_9"] + df["sales_month_10"] + df["sales_month_11"]

    # Save cleaned data
    df.to_csv(output_file, index=False)
    print("✅ Data Preprocessing Completed!")

if __name__ == "__main__":
    preprocess_data(r"D:\data science\E-commerce sales\source fiels\dataset-sales.csv", 
                    r"D:\data science\E-commerce sales\source fiels\clean-dataset.csv")
