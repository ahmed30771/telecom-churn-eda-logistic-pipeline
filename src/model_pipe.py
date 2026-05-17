
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd
import os
try:
    from load_data import loadconfig
except:
    from src.load_data import loadconfig



class LogisticRegressionPipeline:
    def __init__(self, df):
        """
        Initialize the Pipepline

        Args
        -------
        df: pd.DataFrame
            pd.DataFrame for the Pipeline
        """
        self.config = loadconfig()
        self.df = df
        self.pipeline = None
        self.grid_search = None
        self.label_encoder = LabelEncoder()

    def encode_target(self):
        # extracting required cofigurations
        try:
            target_col = self.config["target"]["column"]
        except:
            raise ValueError("Invalid target column configuration.")

        if not target_col in self.df.columns:
            raise ValueError("Invalid target column in configuration.")

        self.df[target_col] = self.label_encoder.fit_transform(
            self.df[target_col])

    def split_data(self):
        # extracting required cofigurations
        try:
            target_col = self.config["target"]["column"]
            test_size = self.config["split"]["test_size"]
            random_state = self.config["split"]["random_state"]
            stratify = self.config["split"]["stratify_target"]
        except:
            raise ValueError("Invalid split data configuration.")

        if not target_col in self.df.columns:
            raise ValueError("Invalid target column in configuration.")

        # features
        X = self.df.drop(columns=[target_col])
        # target
        y = self.df[target_col]
        if stratify:
            stratify = y
        else:
            stratify = None

        # train test split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X,
            y,
            test_size=test_size,
            random_state=random_state,
            stratify=stratify
        )
        return self.X_train, self.X_test, self.y_train, self.y_test

    def create_column_transformer(self):
        # extracting required cofigurations
        try:
            numeric = self.config["column_transformer"]["numeric"]
            nominal = self.config["column_transformer"]["nominal"]
            ordinal = self.config["column_transformer"]["ordinal"]
            numeric_features = numeric["features"]
            nominal_features = nominal["features"]
            ordinal_dict = ordinal["features"]
        except:
            raise ValueError("Invalid column transformer configurations.")

        # Remaining Columns
        used_columns = numeric_features + \
            nominal_features + list(ordinal_dict.keys())
        remaining_columns = [
            col for col in self.X_train.columns if col not in used_columns]

        # Numeric Pipeline
        numeric_pipeline = Pipeline([
            ("imputer", SimpleImputer(
                strategy=numeric["SimpleImputer"]["strategy"])),
            ("scaler", StandardScaler())
        ])

        # Nominal Pipeline
        nominal_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(
                handle_unknown=nominal["OneHotEncoder"]["handle_unknown"], drop=nominal["OneHotEncoder"]["drop"]))
        ])

        # Ordinal Pipeline
        ordinal_pipeline = Pipeline([
            ("imputer", SimpleImputer(
                strategy=ordinal["SimpleImputer"]["strategy"])),
            ("ordinal", OrdinalEncoder(categories=list(ordinal_dict.values())))
        ])

        # Remaining Columns Pipeline
        remaining_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent"))
        ])

        # Column Transformer
        self.column_transformer = ColumnTransformer([
            ("num", numeric_pipeline, numeric_features),
            ("nominal", nominal_pipeline, nominal_features),
            ("ordinal", ordinal_pipeline, list(ordinal_dict.keys())),
            ("remaining", remaining_pipeline, remaining_columns)
        ])

    def create_pipeline(self):
        # extracting required cofigurations
        try:
            rand_state = self.config["model"]["logistic_regression"]["random_state"]
        except:
            raise ValueError("Invalid Logistic Regression Configuration.")

        self.logPipeline = Pipeline([
            ("preprocessor", self.column_transformer),
            ("model", LogisticRegression(random_state=rand_state))
        ])
    

    def apply_gridsearch(self):
        # extracting required cofigurations
        try:
            cv = self.config["grid_search"]["cv"]
            scoring = self.config["grid_search"]["scoring"]
            n_jobs = self.config["grid_search"]["n_jobs"]
            verbose = self.config["grid_search"]["verbose"]
            param_grid = self.config["grid_search"]["param_grid"]
        except:
            raise ValueError('Invalid grid search configurations.')

        self.grid_search = GridSearchCV(
            estimator=self.logPipeline,
            param_grid=param_grid,
            cv=cv,
            scoring=scoring,
            verbose=verbose,
            n_jobs=n_jobs
        )

    def train_model(self):
        self.grid_search.fit(self.X_train, self.y_train)

    def evaluate_model(self):

        print("\nBest Parameters:")
        print(self.grid_search.best_params_)

        print("\nBest CV Score:")
        print(self.grid_search.best_score_)

        test_score = self.grid_search.score(self.X_test, self.y_test)

        print("\nTest Accuracy:")
        print(test_score)

    def save_model(self):
        # extracting required cofigurations
        try:
            path = os.path.abspath(self.config["model"]["logistic_regression"]["save_path"])
        except:
            raise ValueError("Invalid Logistic Regression path Configuration.")

        # Best trained model save
        with open(path, "wb") as f:
            pickle.dump(self.grid_search.best_estimator_, f)
        print(f"Model saved at: {path}")

    def load_model(self):
        # extracting required cofigurations
        try:
            path = os.path.abspath(self.config["model"]["logistic_regression"]["save_path"])
        except:
            raise ValueError("Invalid Logistic Regression path Configuration.")
        
        # Load model
        with open(path, "rb") as f:
            self.loaded_model = pickle.load(f)
        print("Model loaded successfully")

    def predict(self, X_new):
        return self.loaded_model.predict(X_new)

    def save_cv_report(self):
        # extracting required cofigurations
        try:
            path = os.path.abspath(self.config["report"]["cv_report_path"])
        except:
            raise ValueError("Invalid CV Report Path Configuration.")

        # Cross-validation results
        results = pd.DataFrame(self.grid_search.cv_results_)

        # Important columns select
        report = results[[
            "params",
            "mean_test_score",
            "std_test_score",
            "rank_test_score"
        ]].copy()

        # Sorting best to worst
        report = report.sort_values(by="rank_test_score")

        # Save to CSV
        report.to_csv(path, index=False)
        print(f"\nCV report saved at: {path}")

    def run_pipeline(self):
        # 1. encode target
        self.encode_target()

        # 2. split
        self.split_data()

        # 3. preprocess
        self.create_column_transformer()

        # 4. model pipeline
        self.create_pipeline()

        # 5. grid
        self.apply_gridsearch()

        # 6. train
        self.train_model()

        # 7. evaluate
        self.evaluate_model()

        # 8. Cross-validation Report
        self.save_cv_report()


if __name__ == "__main__":
    from load_data import loaddata
    from preprocessing import preprocess_data
    df = loaddata()
    df = preprocess_data(df)
    ml = LogisticRegressionPipeline(df)
    ml.run_pipeline()
    ml.save_model()
