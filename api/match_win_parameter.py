from pydantic import BaseModel

class MatchWinParameter(BaseModel):
    venue: object
    batting_team: object
    bowling_team: object
    ball: float
    innings_total: int
    run_rate: float
    required_run_rate: float
    ball_left: int
    runs_needed : float
    winner_runs : float
    winner_wickets: float
