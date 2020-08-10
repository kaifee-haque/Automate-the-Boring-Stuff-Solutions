stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(inventory):
    print("Inventory:")
    total = 0
    for i, j in inventory.items():
        print(j, i)
        total += j
    print(f"Total number of items: {total}")

display_inventory(stuff)
