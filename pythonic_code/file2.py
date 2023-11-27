import pandas as pd

df = pd.read_csv('nbaallelo.csv')

df.info()

mydf = df[df['fran_id'] == 'Lakers']

mydf = mydf[['fran_id', 'team_id']]

mydf['team_id'].unique()  


