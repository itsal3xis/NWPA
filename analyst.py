import requests
import json

def standings():
    url = 'https://api-web.nhle.com/v1/standings/now'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        equipes_stats = []

        for record in data.get('standings', []):
            equipe_info = {
                "team": record['teamName']['default'],
                "conference": record['conferenceName'],
                "division": record['divisionName'],
                "points": record['points'],
                "gamesPlayed": record['gamesPlayed'],
                "wins": record['wins'],
                "homeWins:": record['homeWins'],
                "roadWins": record['roadWins'],
                "loses": record['losses'],
                "homeLoses": record['homeLosses'],
                "roadLoses": record['roadLosses'],
                "OtWins": record['otLosses'],
                
            }
            equipes_stats.append(equipe_info)
        
        # Sauvegarde dans un fichier JSON
        with open("teamsStats.json", "w", encoding="utf-8") as f:
            json.dump(equipes_stats, f, ensure_ascii=False, indent=4)
        
    
    else:
        print(f"Error: {response.status_code}")
print(standings())


    