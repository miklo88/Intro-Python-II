# Implement a class to hold room information. This should have name and
# description attributes.
class Room:
    def __init__(self, name):
        self.name = name

#another class of room to make sure my class here is working
class Description(Room):
    def __init__(self, name, description):
        super().__init__(name)
        self.description = description

    def __str__(self):
        return f'Uuu I am a {self.description} {self.name}!'

roomtype = Description('Cellar', 'Moldy')
print(roomtype)