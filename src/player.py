# Write a class to hold player information, e.g. what room they are in
# currently.
#figure out a way to establish current room and how to store that state.
class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    
# figure out a way to add and subract hp from player object for my own stretch goal purposes.
class Attributes(Player):
    def __init__(self, name, hp, current_room):
        super().__init__(current_room)
        self.name = name
        self.hp = hp

    def __str__(self):
        return f'Hola mis amigos! My name is {self.name}. Seems like this {self.current_room} is kind of spooky.'

player1 = Attributes('Carlitos', 100, 'Main Room')
print(player1)
# print(player1.name)
print(player1.hp)