#! python3

def comma_string(_list):
    """Takes a list of items and formats it into a string, separated by
    commas like plain English.

    Args:
        _list: The list of items.

    Returns:
        result: The string of list items separated by commas."""
    
    result = ""
    for i, character in enumerate(_list):
        if i == len(_list) - 1:
            result += "and "
        result += str(character)
        if i < len(_list) - 1:
            result += "," + " "
    return(result)

crew = ["Holden", "Nagata", "Kamal", "Burton", "Miller"]
print(comma_string(crew))
