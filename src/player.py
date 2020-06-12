# Write a class to hold player information, e.g. what room they are in
# currently.
#figure out a way to establish current room and how to store items from it.
class Player:
    def __init__(self, current_room=None):
        # self.name = name
        self.current_room = current_room
        #inventory of items collected
        # self.players_stuff = Item([])
    # must add items to a player
        # self.players_stuff.append(item)
    # see how many items a player has. len(items)

    def __str__(self):
       return f'{self.name} {self.current_room}'

# #testing
# player = Player('Carlitos', 'Abuelas', 'hammer')
# print(player)