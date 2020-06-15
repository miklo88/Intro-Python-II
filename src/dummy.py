new_player1 = { 'firstName': 'LaMarcus', 'lastName': 'Aldridge', 'jersey': '12', 'heightMeters': '2.11', 'nbaDebutYear': '2006', 'weightKilograms': '117.9'}
new_player2 = { 'firstName': 'LeBron', 'lastName': 'James', 'jersey': '2', 'heightMeters': '2.03', 'nbaDebutYear': '2003', 'weightKilograms': '113.4' }
new_player3 = { 'firstName': 'Kawhi', 'lastName': 'Leonard', 'jersey': '2', 'heightMeters': '2.01', 'nbaDebutYear': '2011', 'weightKilograms': '104.3' }  
new_player4 = { 'firstName': 'Dirk', 'lastName': 'Nowitzki', 'jersey': '40', 'heightMeters': '2.15', 'nbaDebutYear': '2011', 'weightKilograms': '107.3' }  
  

class Players:
    def __init__(self, firstname = str, lastname = str, jersey = int, heightMeters = float, nbaDebutYear = int, weightKilograms = float, nba_players = []):
        self.firstname = firstname
        self.lastname = lastname
        self.jersey = jersey
        self.heightMeters = heightMeters
        self.nbaDebutYear = nbaDebutYear
        self.nba_players = nba_players

    def add_player(self):
        return self.append()

    def __str__(self):
        return f'{self.firstname}, {self.lastname}, {self.jersey}, {self.heightMeters}, {self.nbaDebutYear}'

# nba_players = []
# nba_players = Players('carlitos', 'redding', 22, 1.5, 1988)
nba_players = Players()
# nba_players.append(new_player1) #perfect example of a class list being created and passedf to the append.
print(nba_players)