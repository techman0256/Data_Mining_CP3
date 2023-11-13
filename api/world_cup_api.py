import uvicorn
from fastapi import FastAPI,HTTPException
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import joblib
from match_win_parameter import MatchWinParameter

from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Dropout
# from tensorflow.keras.utils import to_categorical

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
    target = data['target']
    
    # load preprocessor
    preprocessor = joblib.load('api/preprocessor.pkl')
    
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
        'winner_runs': [winner_runs],
        'winner_wickets': [winner_wickets],
        'target': [target]
    })

    # apply preprocessing
    df_transformed = preprocessor.transform(df)

    prediction = model.predict(df_transformed)
    print(prediction)

    return {"Winning probability for this team": str(prediction[0][0])}


if __name__== '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



