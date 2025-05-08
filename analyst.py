import json
import collector

with open("teamsStats.json", "r", encoding="utf-8") as f:
    data = json.load(f)

with open("todayGames.json", "r", encoding="utf-8") as f:
    todaysGames = json.load(f)

def winPourcentage(abbr):
    for team in data:
        if team.get("abrev") == abbr:
            wins = team.get("wins", 0)
            games_played = team.get("gamesPlayed", 1)  # avoid division by zero
            win_pct = (wins / games_played) * 100
            return round(win_pct, 2)
    
    return f"Team '{abbr}' not found."

def winPctAtHome(abbr):
    for team in data:
        if team.get("abrev") == abbr:
            
            homewins = team.get("homeWins", 0)
            homelosses = team.get("homeLoses", 0)

            total_home_games = homewins + homelosses
            if total_home_games == 0:
                return "No home games played."

            homewin_pct = (homewins / total_home_games) * 100
            return round(homewin_pct, 2)

    return f"Team '{abbr}' not found."


def winPctOnRoad(abbr):
    for team in data:
        if team.get("abrev") == abbr:
            
            roadwins = team.get("roadWins", 0)
            roadlosses = team.get("roadLoses", 0)

            total_road_games = roadwins + roadlosses
            if total_road_games == 0:
                return "No road games played."

            roadwinswin_pct = (roadwins / total_road_games) * 100
            return round(roadwinswin_pct, 2)

    return f"Team '{abbr}' not found."

def lossesPctAtHome(abbr):
    for team in data:
        if team.get("abrev") == abbr:
            
            homewins = team.get("homeWins", 0)
            homelosses = team.get("homeLoses", 0)

            total_home_games = homewins + homelosses
            if total_home_games == 0:
                return "No home games played."

            homelosses_pct = (homelosses / total_home_games) * 100
            return round(homelosses_pct, 2)

    return f"Team '{abbr}' not found."

def lossesPctOnRoad(abbr):
    for team in data:
        if team.get("abrev") == abbr:
            
            roadwins = team.get("roadWins", 0)
            roadlosses = team.get("roadLoses", 0)

            total_road_games = roadwins + roadlosses
            if total_road_games == 0:
                return "No road games played."

            roadlosseswin_pct = (roadlosses / total_road_games) * 100
            return round(roadlosseswin_pct, 2)

    return f"Team '{abbr}' not found."


def getHomeTeam(abbr):
    for game in todaysGames:
        if game["homeTeam"]["abbrev"] == abbr:
            return game["homeTeam"]["name"]
    return False



def rapid_analyst(team1_abbr, team2_abbr):
    homeTeam = getHomeTeam(team1_abbr)
    awayTeam = team2_abbr
    if homeTeam == False:
        homeTeam = team2_abbr
        awayTeam = team1_abbr
    
    homeTeamWinPct = winPourcentage(homeTeam)
    awayTeamWinPct = winPourcentage(awayTeam)
    
    homeTeamWinPctAtHome = winPctAtHome(homeTeam)
    awayTeamWinPctOnRoad = winPctOnRoad(awayTeam)
    homeTeamLossPctAtHome = lossesPctAtHome(homeTeam)
    awayTeamLossPctOnRoad = lossesPctOnRoad(awayTeam)

    homeTeamPlayer = collector.team_players(homeTeam)
    awayTeamPlayer = collector.team_players(awayTeam)

    
    
    
    

rapid_analyst("WSH", "CAR")
    

    





    