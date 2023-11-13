import uvicorn
from fastapi import FastAPI,HTTPException
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np

from match_win_parameter import MatchWinParameter

from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.utils import to_categorical

app = FastAPI()
#load h5 model form tensorflow
model = tf.keras.models.load_model('api/model.h5')



@app.get("/")
def read_root():
    return {"Hello": "Welcome to World Cup 2023 Match Prediction API"}

@app.post("/predict_match_win")
def match_win(data: MatchWinParameter):
    data= data.model_dump()
    venue = data['venue']
    batting_team = data['batting_team']
    bowling_team = data['bowling_team']
    ball = data['ball']
    innings_total = data['innings_total']
    run_rate = data['run_rate']
    required_run_rate = data['required_run_rate']
    ball_left = data['ball_left']
    runs_needed = data['runs_needed']
    winner_runs = data['winner_runs']
    winner_wickets = data['winner_wickets']
    
    #preprocessing data
    categorical_cols = ["venue", "batting_team", "bowling_team"]
    numeric_cols = ['runs_needed','winner_wickets','winner_runs','required_run_rate','ball','innings_total','target','ball_left',
                    'run_rate']

    numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])
    categorical_transformer = Pipeline(steps=[
        ("label_encoder", OneHotEncoder(handle_unknown='ignore'))
    ])

    # Combine transformers
    preprocessor = ColumnTransformer(
        transformers=[
            ("num", numeric_transformer, numeric_cols),
            ("cat", categorical_transformer, categorical_cols)
        ]
    )

    # Preprocessing the data
    X = preprocessor.fit_transform(data)








# if __name__== '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)



