from src.load_data import loaddata
from src.preprocessing import preprocess_data
from src.model_pipe import LogisticRegressionPipeline


def main():
    df = loaddata()
    df = preprocess_data(df)

    ml = LogisticRegressionPipeline(df)
    ml.run_pipeline()
    ml.save_model()


if __name__=="__main__":
    main()