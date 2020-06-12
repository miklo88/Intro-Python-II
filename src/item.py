class Item:
    def __init__(self, item_name, item_description):
        self.item_name = item_name
        self.item_description = item_description
    
    def __str__(self):
        #need to figure how to add the item and know which player has item.
       return f'Uuuu {self.item_name}: {self.item_description}'
        





# newitem = Inventory('hammer', 'really old', 1, 'current player')
# print(newitem)
