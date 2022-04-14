stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    print("Inventory:")
    for item in stuff:
        print(stuff[item], item)
    print(f"Total number of items: {sum(stuff.values())}")


#displayInventory(stuff)