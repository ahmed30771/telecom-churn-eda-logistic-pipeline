from src.load_data import loaddata
from src.preprocessing import preprocess_data
from src.model_pipe import LogisticRegressionPipeline


def main():
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


if __name__=="__main__":
    main()