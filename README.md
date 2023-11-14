# Data_Mining_CP3

# World Cup 2023 Cricket Match Prediction API by Group Deep Miners

## Overview

Welcome to the World Cup 2023 Cricket Match Prediction API! This API is designed to predict the winning probability for a cricket team based on various parameters. The model used in this API has been trained on historical data and is capable of providing predictions for World Cup 2023 cricket matches.

## Installation

To use this API, follow the steps below:

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/WorldCup2023PredictionAPI.git
   cd WorldCup2023PredictionAPI

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt


## Usage

### Running the API locally

To run the API locally, execute the following command:

   ```bash
   python world_cup_api.py
   ```

The API will be accessible at 'http://127.0.0.1:8000'

### Endpoint: '/predict_match_win'

- Method: POST
- Description: Predicts the winning probability for a cricket team based on input parameters.
  
Request Body
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

### Response 
The API will return the winning probability for the specified team in the form of a JSON response.

   ```Json
   {
      "Winning probability for this team": "0.75"
   }
   ```



