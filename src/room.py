# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    #room description
    def __str__(self):
        return f'{self.name} {self.description}'

# #another class of room to make sure my class here is working
# class Description(Room):
#     def __init__(self, name, description):
#         super().__init__(name)
#         self.description = description

#     def __str__(self):
#         return f'Uuu I am a {self.description} {self.name}!'

# room = Room('Cellar', 'stinky smelly Moldy')
# print(room)