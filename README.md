# Data Mining CP3

# World Cup 2023 Cricket Match Prediction API by Group Deep Miners

## Overview

Welcome to the World Cup 2023 Cricket Match Prediction API! This API is designed to predict the winning probability for a cricket team based on various parameters. The model used in this API has been trained on historical data and is capable of providing predictions for World Cup 2023 cricket matches.

## Installation

To use this API, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/techman0256/Data_Mining_CP3

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt


## Running the API locally

To run the API locally, execute the following command:

   ```bash
   python world_cup_api.py
   ```

The API will be accessible at 'http://127.0.0.1:8000'

## Task 1

### Run Prediction
The script predicts scores for the 10th and 11th matches of the input player using the trained models and calculates the root mean squared error (RMSE) for evaluation.

- URL : **/predict_runs**
- Method: POST
- Provide the input parameters as the name of the player.
   
   ```json
   {
     "Player": "string"
   }
   ```

- Response : The API will return the winning probability for the specified team in the form of a JSON response.

   ```Json
   {
     "Predicted Runs for Match 10 ": "Run1",
     "Predicted Runs for Match 11 ": "Run2"
   }
   ```

### Top number of Centuries Scored by any Player
The script calculates the number of centuries scored by each player based on their match scores. And outputs the highest century-scoring player.

- URL : **/get_most_centuries_scoring_player**
- Method: POST
- Needs no input parameter.
- Response : The API will return the highest century scoring player

   ```Json
   {
     "Most Centuries Scoring Player": "['Player 1' No. of centuries]['Player 2' No. of centuries]....."
   }
   ```


### Top 10 Players to score Highest Rus
The script calculates players scoring highest runs overall in the tournament. And outputs the list of players (top 10).

- URL : **/get_top_10_most_runs_player**
- Method: POST
- Needs no input parameter.
- Response : The API will return the highest century scoring player

   ```Json
   {
     "1st": "['Player' runs]",
     "3rd": "['Player' runs]",
     "2nd": "['Player' runs]",
     "4th": "['Player' runs]",
     "5th": "['Player' runs]",
     "6th": "['Player' runs]",
     "7th": "['Player' runs]",
     "8th": "['Player' runs]",
     "9th": "['Player' runs]"
   }
   ```



## Task 2
Predicting the Finalist Teams and Players

### Match Outcomes
The script builds a deep learning model using TensorFlow and Keras to predict match outcomes.

- URL : **/predict_match_win**
- Method: POST
- Provide the input parameters for match prediction using the MatchWinParameter class.

   
   ```json
   {
      "venue": "Stadium Name",
      "batting_team": "Team A",
      "bowling_team": "Team B",
      "ball": 10,
      "innings_total": 150,
      "run_rate": 7.5,
      "required_run_rate": 8.0,
      "ball_left": 30,
      "runs_needed": 50,
      "target": 200
   }
   ```

- Response : The API will return the winning probability for the specified team in the form of a JSON response.

   ```Json
   {
      "Winning probability for this team": "0.75"
   }
   ```

So to make this work for task 2, you need to input 2 teams at a time (semi-finals) and the model will predict the winning probability of the teams. By this you will get the 2 teams that will play the finals. 

__Note: The model need data for the 2nd innings of each match__




## Task 3
Predict the Winner of ICC Cricket World Cup 2023

### Match Outcomes
The script builds a deep learning model using TensorFlow and Keras to predict match outcomes.

- URL : **/predict_match_win**
- Method: POST
- Provide the input parameters for match prediction using the MatchWinParameter class.

   
   ```json
   {
      "venue": "Stadium Name",
      "batting_team": "Team A",
      "bowling_team": "Team B",
      "ball": 10,
      "innings_total": 150,
      "run_rate": 7.5,
      "required_run_rate": 8.0,
      "ball_left": 30,
      "runs_needed": 50,
      "target": 200
   }
   ```

- Response : The API will return the winning probability for the specified team in the form of a JSON response.

   ```Json
   {
      "Winning probability for this team": "0.75"
   }
   ```

So to make this work for task 3, you need to input 2 teams playing finals (from output of task2) and the model will predict the winning probability of the teams. By this you will get the team that will win finals. 

__Note: The model need data for the 2nd innings of each match__


## Contribution of Each Member
- Dhruv Shah, Pranav Patel and Sumukh Patel - Developed the core logic behind the models to be used for Task1, Task2 and Task3. Implemented the model using Python and required libraries.

- Akshat Prasad, Arsh Jindal and Chinmay Vaishnav - Worked on the API Development part. Deployed the ML Models built for Task1, Task2 and Task3 successfully. Also worked on structuring the repository and updating the Readme.md file.
  


