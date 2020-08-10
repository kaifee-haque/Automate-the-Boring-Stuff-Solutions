stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for i, j in inventory.items():
        print(j, i)
        total += j
    print(f"Total number of items: {total}")

def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory.setdefault(item, 0)
        inventory[item] += 1

display_inventory(stuff)
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
add_to_inventory(stuff, dragon_loot)
display_inventory(stuff)
