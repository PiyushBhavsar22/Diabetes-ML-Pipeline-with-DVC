import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
import yaml
import os
import mlflow
from urllib.parse import urlparse

os.environ['MLFLOW_TRACKING_URI']="https://dagshub.com/PiyushBhavsar/MachineLearningPipeline.mlflow"
os.environ['MLFLOW_TRACKING_USERNAME']="PiyushBhavsar"
os.environ["MLFLOW_TRACKING_PASSWORD"]="efc90d4643739e2846176d7c919671f169a01449"

## Load parameters from params.yaml
params = yaml.safe_load(open("params.yaml"))["train"]

def evaluate(data_path,model_path):
    data=pd.read_csv(data_path)
    X=data.drop(columns=['Outcome'])
    y=data['Outcome']

    mlflow.set_tracking_uri("https://dagshub.com/PiyushBhavsar/MachineLearningPipeline.mlflow")

    ## Load the model from the disk
    model=pickle.load(open(model_path,'rb'))

    predictions=model.predict(X)
    accuracy=accuracy_score(y,predictions)

    ##Log metrics to MLFlow
    mlflow.log_metric("accuracy",accuracy)
    print("Model accuracy:{accuracy}")

if __name__=="__main__":
    evaluate(params["data"],params["model"])

    