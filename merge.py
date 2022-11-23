import pandas as pd

dfManU = pd.read_csv('Tweets_ManUtd.csv')
dfLiv = pd.read_csv('Tweets_LFC.csv')
dfArsenal = pd.read_csv('Tweets_Arsenal.csv')
dfChelsea = pd.read_csv('Tweets_ChelseaFC.csv')
dfManCity = pd.read_csv('Tweets_ManCity.csv')
dfSpurs = pd.read_csv('Tweets_SpursOfficial.csv')

df = pd.concat([dfManU, dfLiv, dfArsenal, dfChelsea, dfManCity, dfSpurs])
df.to_csv('Tweets_Overall.csv', index=False)
print(df.sample(n=20))
print(df.shape)
print(df['club'].value_counts())
print(df.dtypes)
print(df.sample(n=20))