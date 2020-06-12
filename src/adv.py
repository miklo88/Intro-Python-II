from room import Room
from player import Player
from item import Item
#All the items
items = {
    'candybar': Item("snickers", "might as well eat it so you dont get hangry."),
}
    # 'notebook': Item("notebook", "spillin the tea."),
    # 'vase': Item("vase", "there seems to be a map drawn on this this vase."),
    # 'staff': Item("staff", "enable gandalf mode."),
    # 'candlestick': Item("candlestick", "save for the darkest of times."),
# print(items['candybar'])
# Declare all the rooms
#room dictionary with attributes/properites of name and description.
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),
    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}
# print(room['outside']['candybar'])
# #room variables #add items to rooms
# outside = Room("Outside Cave Entrance",
# "North of you, the cave mount beckons")

# foyer = Room("Foyer", """Dim light filters in from the south. Dusty
# passages run north and east.""")

# overlook = Room("Grand Overlook", """A steep cliff appears before you, falling
# into the darkness. Ahead to the north, a light flickers in
# the distance, but there is no way across the chasm.""")

# narrow = Room("Narrow Passage", """The narrow passage bends here from west
# to north. The smell of gold permeates the air.""")

# treasure = Room("Treasure Chamber", """You've found the long-lost treasure
# chamber! Sadly, it has already been completely emptied by
# earlier adventurers. The only exit is to the south.""")

#welcome instructions
instructions = """Welcome to find the treasure! As a player you will navigate multiple rooms using the cardinal
directions n for north, s for south, e for east, w for west to find the treasure!"""
print(instructions)
#cardinal direction choice
#Read the user input (The python commmands)
# direction_choice = input(f'Begin your quest now: ')
#Evaluate your code (to work out what I mean)
# chosen_path = 
#Print any results (so you can see the comps response)
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['overlook'].s_to = room['foyer']
room['foyer'].e_to = room['narrow']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
# outside.n_to = foyer
# foyer.s_to = outside
# foyer.n_to = overlook
# overlook.s_to = foyer
# foyer.e_to = narrow
# narrow.w_to = foyer
# narrow.n_to = treasure
# treasure.s_to = narrow
#
# Main
#
# # making a items object

# Make a new player object that is currently in the 'outside' room.
player = Player()
player.current_room = room['outside']
# item = Room()
room['outside'].items.append(items['candybar'])
# Write a loop that:
while True:
    # * Prints the current room name
    print(player.current_room.name)
    # print(item.current_room.item_name)
    # * Prints the current description (the textwrap module might be useful here).
    print(f'The room is {player.current_room.description}')
    # * Waits for user input and decides what to do.
    input_var = input("Where will you go? (n,s,e,w)?: " )
    # If the user enters a cardinal direction, attempt to move to the room there.
    # If the user enters "q", quit the game.
    if input_var == 'n':
        # check if the current room has a n_to attribute
        if player.current_room.n_to is not None:
            # move the player to that room
            player.current_room = player.current_room.n_to 

    elif input_var == 's':
        if player.current_room.s_to is not None:
            #move the player to that room
            player.current_room = player.current_room.s_to

    elif input_var == 'e':
        if player.current_room.e_to is not None:
            #move the player to that room
            player.current_room = player.current_room.e_to

    elif input_var == 'w':
        if player.current_room.w_to is not None:
            #move the player to that room
            player.current_room = player.current_room.w_to
#to break out of the game
    elif input_var == 'q':
        print(f'The quest has ended.') 
        break
        # Print an error message if the movement isn't allowed.
# for any wrong input 
    else:
        print('Wrong command, try again')
