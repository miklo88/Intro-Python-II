# Write a class to hold player information, e.g. what room they are in
# currently.
#figure out a way to establish current room and how to store items from it.
class Player:
    def __init__(self, name, current_room=None):
        self.name = name
        self.current_room = current_room
    # must add items to a player
        # self.items.append(item)

    def __str__(self):
       return f'{self.name} {self.current_room}'

#testing
# player = Player('Carlitos', 'Abuelas')
# print(player)