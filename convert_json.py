import pandas as pd

data = pd.read_csv('./data/nba_3pt_data.csv')

print(data.to_dict('records')[0])