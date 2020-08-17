#! python3

def validator(c_dict):
    """Takes a chess board configuration and determines whether or not
    it is valid.

    Args:
        c_dict: A dictionary representing a chess board configuration.

    Returns:
        A boolean indicating whether or not the configuration is valid.
    """
    
    white_types = ["wking", "wqueen", "wbishop", "wknight", "wrook", "wpawn"]
    black_types = ["bking", "bqueen", "bbishop", "bknight", "brook", "bpawn"]

    if len(c_dict) > 32:
        return False

    for key in c_dict:
        if (not 1 <= int(key[0]) <= 8) and (not "a" <= key[1] <= "h"):
            return False

    white_count = dict.fromkeys(white_types, 0)
    black_count = dict.fromkeys(black_types, 0)
    
    for value in c_dict.values():
        if value not in white_types and value not in black_types:
            return False
        if value[0] == "w":
            white_count[value] += 1
        if value[0] == "b":
            black_count[value] += 1

    if white_count["wking"] > 1 or black_count["bking"] > 1:
        return False
    if white_count["wpawn"] > 8 or black_count["bpawn"] > 8:
        return False
    
    w_sum = 0
    b_sum = 0
    for value in white_count.values():
        w_sum += value
    for value in black_count.values():
        b_sum += value
    if w_sum > 16 or b_sum > 16:
        return False

    return True
print(validator({'1h': 'bking', '6c': 'bking', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}))
