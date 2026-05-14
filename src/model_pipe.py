
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.pipeline import Pipeline
import pickle
import pandas as pd


class LogisticRegressionPipeline:
    def __init__(self, df):
        """
        Initialize the Pipepline

        Args
        -------
        df: pd.DataFrame
            pd.DataFrame for the Pipeline
        """
        self.df = df
        self.pipeline = None
        self.grid_search = None
        self.label_encoder = LabelEncoder()


    def encode_target(self, target_col="Churn"):
        self.df[target_col] = self.label_encoder.fit_transform(
            self.df[target_col]
        )


    def split_data(self, target_col="Churn"):
        # features
        X = self.df.drop(columns=[target_col])
        # target
        y = self.df[target_col]

        # train test split
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(
            X,
            y,
            test_size=0.2,
            stratify=y,
            random_state=42,
        )
        return self.X_train, self.X_test, self.y_train, self.y_test


    def create_column_transformer(
        self,
        numeric_features,
        nominal_features,
        ordinal_features,
        ordinal_categories
        ):
        # Remaining Columns
        used_columns = numeric_features + nominal_features + ordinal_features
        remaining_columns = [col for col in self.X_train.columns if col not in used_columns]
        
        # Numeric Pipeline
        numeric_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="median")),
            ("scaler", StandardScaler())
        ])
        
        # Nominal Pipeline
        nominal_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("onehot", OneHotEncoder(handle_unknown="ignore", drop="first"))
        ])

        # Ordinal Pipeline
        ordinal_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent")),
            ("ordinal", OrdinalEncoder(categories=ordinal_categories))
        ])
        
        # Remaining Columns Pipeline
        remaining_pipeline = Pipeline([
            ("imputer", SimpleImputer(strategy="most_frequent"))
        ])

        # Column Transformer
        self.column_transformer = ColumnTransformer([
            ("num", numeric_pipeline, numeric_features),
            ("nominal", nominal_pipeline, nominal_features),
            ("ordinal", ordinal_pipeline, ordinal_features),
            ("remaining", remaining_pipeline, remaining_columns)
        ])


    def create_pipeline(self):
        self.logPipeline = Pipeline([
            ("preprocessor", self.column_transformer),
            ("model", LogisticRegression())
        ])



    def apply_gridsearch(self):
        param_grid = {
            "model__C": [0.01, 0.1, 1, 10],
            "model__solver": ["lbfgs", "liblinear"],
            "model__max_iter": [100, 200, 500, 5000]
        }

        self.grid_search = GridSearchCV(
            estimator=self.logPipeline,
            param_grid=param_grid,
            cv=5,
            scoring="accuracy",
            n_jobs=-1
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


    def save_model(self, filepath="model/churn_model.pkl"):
        # Best trained model save
        with open(filepath, "wb") as f:
            pickle.dump(self.grid_search.best_estimator_, f)
        print(f"Model saved at: {filepath}")


    def load_model(self, filepath="model/churn_model.pkl"):
        with open(filepath, "rb") as f:
            self.loaded_model = pickle.load(f)
        print("Model loaded successfully")


    def predict(self, X_new):
        return self.loaded_model.predict(X_new)


    def save_cv_report(self, filepath="cv_report.csv"):
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
        report.to_csv(filepath, index=False)
        print(f"CV report saved at: {filepath}")


    def run_pipeline(self, target_column:str, numeric_features:list, nominal_features:list, ordinal_dict:dict):
        # 1. encode target
        self.encode_target(target_column)
        
        # 2. split
        self.split_data()
        
        # 3. preprocess
        self.create_column_transformer(
            numeric_features=numeric_features,
            nominal_features=nominal_features,
            ordinal_features=list(ordinal_dict.keys()),
            ordinal_categories=list(ordinal_dict.values())
        )
        
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
    ml.run_pipeline(
        target_column="Churn",
        numeric_features=['tenure', 'TotalCharges', 'MonthlyCharges'],
        nominal_features=[
            'MultipleLines', 'InternetService',
            'OnlineSecurity', 'OnlineBackup',
            'DeviceProtection', 'TechSupport',
            'StreamingTV', 'StreamingMovies',
            'PaymentMethod'],
        ordinal_dict={
            'Contract': ['Month-to-month', 'One year', 'Two year'],
            'gender': ['Female', 'Male'],
            'Partner': ['No', 'Yes'],
            'Dependents': ['No', 'Yes'],
            'PhoneService': ['No', 'Yes'],
            'PaperlessBilling': ['No', 'Yes']}
        )
    ml.save_model(filepath="model/churn_model.pkl")