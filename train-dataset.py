import argparse
from azureml.data.dataset_factory import TabularDatasetFactory
import pandas as pd
from sklearn.linear_model import LogisticRegression
from azureml.core.run import Run
import joblib
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
from azureml.core import Dataset
from azureml.core import Model
from azureml.core import Workspace
import numpy as np

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--C', type=float, default=1.0, help="")
    parser.add_argument('--max_iter',type=int, default=100, help="")

    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))


    df = pd.read_csv("cleandata.csv")
    df['Avg_Sleepiness'] = df['Avg_Sleepiness'].apply(lambda x: float(x.strip('%')))
    df['Percent_Morning_Crashes'] = df['Percent_Morning_Crashes'].apply(lambda x: float(x.strip('%')))
    df['Percent_Evening_Crashes'] = df['Percent_Evening_Crashes'].apply(lambda x: float(x.strip('%')))


    x_col = ['Avg_Sleepiness', 'People_Queried_About_Sleep', 'raw_Crashes_per_Year','Avg_Crash_Severity','Percent_Morning_Crashes','Percent_Evening_Crashes','Crashes_per_Year']
    y_col = ['State']
    x_df = df.loc[:, x_col]
    y_df = df.loc[:, y_col]

    x_train, x_test = train_test_split(x_df, shuffle=False)
    y_train, y_test = train_test_split(y_df, shuffle=False)

    model = LogisticRegression(C=args.C,max_iter=args.max_iter).fit(x_train,y_train)

    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))

if __name__ == '__main__':
    main()