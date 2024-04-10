import argparse
import os
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from azureml.core.run import Run
from azureml.data.dataset_factory import TabularDatasetFactory
import joblib

def clean_data(data):
    x_df = data.to_pandas_dataframe()
    x_df = x_df.drop(columns=['matchup_home','season_type','team_name_home','team_name_away'])
    x_df[['wl_home','wl_away']] = x_df[['wl_home','wl_away']].replace(['W','L'],[1,0])
    y_df = x_df.pop("highest_3pp_wl").apply(lambda s: 1 if s == "W" else 0)

    return x_df, y_df

def main():
    # argparse setup
    parser = argparse.ArgumentParser()
    parser.add_argument('--C', type=float, default=1.0, help="Inverse of regularization strength. Smaller values cause stronger regularization")
    parser.add_argument('--max_iter', type=int, default=100, help="Maximum number of iterations to converge")
    args = parser.parse_args()

    run = Run.get_context()

    run.log("Regularization Strength:", np.float(args.C))
    run.log("Max iterations:", np.int(args.max_iter))

    # getting data
    url_path = 'https://raw.githubusercontent.com/mattwatson50/udacity_azure_ml_final/main/data/nba_3pt_data.csv'
    ds = TabularDatasetFactory.from_delimited_files(path=url_path)

    x, y = clean_data(ds)
    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        random_state=104,
        test_size=0.25,
        shuffle=True
        )

    # train model
    model = LogisticRegression(C=args.C, max_iter=args.max_iter).fit(x_train, y_train)

    # evaluate model
    accuracy = model.score(x_test, y_test)
    run.log("Accuracy", np.float(accuracy))
    
    # save model
    os.makedirs('outputs', exist_ok=True)
    joblib.dump(value=model, filename='outputs/model.joblib')

if __name__ == '__main__':
    main()
