class Player:
    def __init__(self,player_id,name,games_played=0,total_points=0,wins=0,average_score=0):
        self.player_id = player_id
        self.name = name
        self.games_played = games_played
        self.total_points = total_points
        self.wins = wins
        self.average_score = average_score
        
    def record_game(self,score,won):
        if score < 0:
            raise ValueError("Score cannot be negative")
        self.games_played += 1
        self.total_points += score
        if won is True:
            self.wins += 1
        
        self.average_score = self.total_points / self.games_played
        
        
player1 = Player("P001", "Micah")

player1.record_game(100, True)

try:
    player1.record_game(-50, False)
except ValueError as error:
    print(error)

print("Games Played:", player1.games_played)
print("Total Points:", player1.total_points)
print("Wins:", player1.wins)
