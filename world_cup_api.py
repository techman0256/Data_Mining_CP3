import uvicorn
from fastapi import FastAPI,HTTPException
import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import joblib
from match_win_parameter import MatchWinParameter
from run_pred_parameter import RunPredParameter

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
        'target': [target]
    })

    # apply preprocessing
    df_transformed = preprocessor.transform(df)

    prediction = model.predict(df_transformed)
    print(prediction)

    return {"Winning probability for this team": str(prediction[0][0])}


@app.post("/predict_runs")
def predict_run(data: RunPredParameter):
    data= data.model_dump()
    Player = data['Player']
    #search Player in 1st column of dataset predicted_scores.csv

    df= pd.read_csv('datasets/predicted_scores.csv')

    df = df[df['Player']==Player]

    m10 = int(df['M10'].values[0])
    m11 = int(df['M11'].values[0])

    return {"Predicted Runs for Match 10 ": str(m10),
            "Predicted Runs for Match 11 ": str(m11)}


@app.post("/get_top_10_most_runs_player")
def top_10_batsman():
    df= pd.read_csv('datasets/predicted_scores.csv')
    df = df.sort_values(by=['Total'], ascending=False)
    df = df.head(10)
    df= df[['Player','Total']]
    df['Total'] = df['Total'].astype(int)
    #return jason format
    return {"1st": str(df.iloc[0].values),
            "3rd": str(df.iloc[2].values),
            "2nd": str(df.iloc[1].values),
            "4th": str(df.iloc[3].values),
            "5th": str(df.iloc[4].values),
            "6th": str(df.iloc[5].values),
            "7th": str(df.iloc[6].values),
            "8th": str(df.iloc[7].values),
            "9th": str(df.iloc[8].values)}


@app.post("/get_most_centuries_scoring_player")
def top_century():
    df= pd.read_csv('datasets/predicted_scores.csv')
    df = df.sort_values(by=['Centuries'], ascending=False)
    #df = df.head()
    df= df[['Player','Centuries']]
    df['Centuries'] = df['Centuries'].astype(int)
    #return jason format
    return {"Most Centuries Scoring Player": str(df.iloc[0].values) + str(df.iloc[1].values)}   

if __name__== '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)



