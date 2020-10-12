#! python3
"""Functions for displaying and adding to a dictionary containing items
in a fantasy game."""


def display_inventory(inventory):
    """Displays a given dictionary of fantasy game items as a series of strings.

    Args: inventory: The dictionary representing the inventory of game items.
    """
    
    print("Inventory:")
    total = 0
    for i, j in inventory.items():
        print(j, i)
        total += j
    print(f"Total number of items: {total}")


def add_to_inventory(inventory, added_items):
    """Adds game items to the inventory.
    Args:
        inventory: The dictionary representing the inventory of game items.
        added_items: A list of strings representing the items to be added.
    """
    
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

        
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
