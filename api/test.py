import uvicorn
from fastapi import FastAPI,HTTPException
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

from match_win_parameter import MatchWinParameter

# from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
# from sklearn.compose import ColumnTransformer
# from sklearn.pipeline import Pipeline


model = tf.keras.models.load_model('api/model.h5')

import joblib
preprocessor = joblib.load('api/preprocessor.pkl')

venue = "Some Venue"
batting_team = "Team A"
bowling_team = "Team B"
ball = 30
innings_total = 150
run_rate = 7.5
required_run_rate = 6.8
ball_left = 90
runs_needed = 40
target = 200



df = pd.DataFrame({
        'venue': [venue],
        'batting_team': [batting_team],
        'bowling_team': [bowling_team],
        'ball': [ball],
        'innings_total': [innings_total],
        'run_rate': [run_rate],
        'required_run_rate': [required_run_rate],
        'ball_left': [ball_left],
        'runs_needed': [runs_needed],
        'target': [target]
})


    # apply preprocessing
df_transformed = preprocessor.transform(df)

print(df_transformed.shape)

prediction = model.predict(df_transformed)
print(prediction[0][0])

Player = "V Kohli"

df= pd.read_csv('datasets/predicted_scores.csv')

df = df[df['Player']==Player]

print(df)

m10 = df['M10'].values
m11 = df['M11'].values

print(m10,m11)


df= pd.read_csv('datasets/predicted_scores.csv')
df = df.sort_values(by=['Total'], ascending=False)
df = df.head(10)
df= df[['Player','Total']]

#print the 3rd row of df as a numpy array

print(df.iloc[2].values)