# Write a class to hold player information, e.g. what room they are in
# currently.
#figure out a way to establish current room and how to store items from it.
class Player:
    def __init__(self, current_room=None, players_items=[]):
        # self.name = name
        self.current_room = current_room
        self.players_items = None
    
    def __str__(self):
       return f'{self.name} {self.current_room}'

    def adds_item(self):
        return self.players_items.append()

    def removes_item(self):
        return self.players_items.remove()


# #testing
# player = Player('Carlitos', 'Abuelas', 'hammer')
# print(player)