import pandas as pd
import os
import yaml


def loadconfig(path="config/config.yaml") -> dict:
    """
    Load configuration from YAML file.

    Args
    -------
    config_path: str.
        Path to the configuration.<br>
        Defaults to "config/config.yaml"

    Returns
    -------
    dict
        Dictionary with configuration settings
    """
    file_path = os.path.abspath(path)
    
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            config = yaml.safe_load(f)
    else:
        raise FileNotFoundError("Configuration file is missing.")

    return config


def loaddata() -> pd.DataFrame:
    """
    Load data from csv file. File path from configuration.

    Returns
    -------
    DataFrame: DataFrame of csv file
    """
    config = loadconfig()
    try:
        path = os.path.abspath(config["data"]["data_path"])
        indx_col = config["data"]["index_column"]
    except:
        raise ValueError("Invalid data configurations.")

    if not os.path.basename(path).endswith(".csv"):
        raise ValueError(
            f"Invalid file extension. Only .csv files are supported.")
    if os.path.exists(path):
        df = pd.read_csv(path, index_col=indx_col)
    else:
        raise FileNotFoundError("Data file is not found on its path.")
    return df


if __name__ == "__main__":
    df = loaddata()
    print(df.head())
