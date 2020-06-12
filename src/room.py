# room blueprint - a room name, the description. extra sugar, add items into this class.
# a category to choose a room by is a cardinal direction.
# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description, items=None):
        self.name = name
        self.description = description
        self.items = []
        self.n_to = None
        self.s_to = None
        self.e_to = None 
        self.w_to = None
    #room name and description from obj to str func also added items concatentation
    def __str__(self):
        output = f'{self.name}: {self.description}: {self.items} \n'
        if self.n_to:
            output += 'To the north is: ' + self.n_to.name + '\n' 
        if self.s_to:
            output += 'To the south is: ' + self.s_to.name + '\n'
            # + 'Hey look!: ' + self.items
        if self.e_to:
            output += 'To the east is: ' + self.e_to.name + '\n'
            # + 'Hey look!: ' + self.items
        if self.w_to:
            output += 'To the west is: ' + self.w_to.name + '\n'
            # + 'Hey look!: ' + self.items

        return output

# # #test
# room = Room('Abuelas', 'jamon the best smell in the world', '!mirame croquetas!')
# print(room)
