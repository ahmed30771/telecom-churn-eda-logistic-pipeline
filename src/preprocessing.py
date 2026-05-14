import pandas as pd
import numpy as np

class DataPreprocessor:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the DataPreprocessor

        Args
        -------
        df: pd.DataFrame
            pd.DataFrame for the preprocessing
        """
        self.df = df.copy()

    def remove_duplicate_rows(self) -> pd.DataFrame:
        """
        Remove duplicated rows from DataFrame.

        Returns
        -------
        pd.DataFrame
            DataFrame with duplicated rows removed.
        """
        self.df = self.df.drop_duplicates(keep='last')
        return self.df
    
    def prepare_dtypes(self) -> pd.DataFrame:
        """
        Replace the empty string with nan and change dtypes for only numeric data in string.

        Returns
        -------
        pd.DataFrame
            DataFrame with replaced blank strings with nan and change dtypes of numeric strings.
        """
        self.df = self.df.replace(r'^\s*$', np.nan, regex=True)
        for col in self.df.columns:
            converted = pd.to_numeric(self.df[col], errors='coerce')
            numeric_ratio = converted.notna().mean()
            if numeric_ratio > 0.9:
                self.df[col] = converted
        return self.df
    
    def clip_outliers_iqr(self, columns, threshold=3):

        
        for col in columns:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            lower_bound = Q1 - threshold * IQR
            upper_bound = Q3 + threshold * IQR
            
            self.df[col] = self.df[col].clip(lower=lower_bound, upper=upper_bound)
        
        return self.df

def preprocess_data(df) -> pd.DataFrame:
    """
    Convenience function to data preprocessing.

    Args
    -------
    df: pd.DataFrame
        DataFrame of dataset.

    Returns
    -------
    pd.DataFrame
        DataFrame with dataset.
    """
    preprocessor = DataPreprocessor(df)
    preprocessor.remove_duplicate_rows()
    preprocessor.prepare_dtypes()
    df_new = preprocessor.clip_outliers_iqr(columns=['tenure', 'MonthlyCharges', 'TotalCharges'])
    return df_new




if __name__=="__main__":
    from load_data import loaddata
    df = loaddata()
    df = preprocess_data(df)
    print(df.head())
    print("-"*50)
    print("Dtypes:\n", df.dtypes)
    print("-"*50)
    print("Total Nan", df.isna().sum().sum())
    print("Total Duplicated:", df.duplicated().sum())
