import pandas as pd
import os


def loaddata(path="data/telco_customer_churn.csv"):
    """
    Load data from csv file

    Args
    -------
    path: str
        csv dataset file path
        Defaults to "data/raw/telco_customer_churn.csv"

    Returns
    -------
    DataFrame: DataFrame of csv file
    """
    file_path = os.path.abspath(path)
    if os.path.exists(file_path):
        df = pd.read_csv(file_path, index_col="customerID")
    else:
        raise FileNotFoundError(f"File not found at this path: {file_path}")

    return df


if __name__ == "__main__":
    df = loaddata()
    print(df.head())
