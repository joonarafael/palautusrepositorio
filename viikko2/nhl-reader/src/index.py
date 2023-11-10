import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        self.content = requests.get(url).json()
        self.players = [Player(player) for player in self.content]

class PlayerStats:
    def __init__(self, record):
        self.players = record.players
    
    def top_scorers_by_nationality(self, nationality):
        players_in_nationality = [player for player in self.players if player.nationality == nationality]

        return sorted(players_in_nationality, key=lambda player: player.assists + player.goals, reverse=True)

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2022-23/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    for player in players:
        print(player)

if __name__ == "__main__":
    main()