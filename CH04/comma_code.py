def comma_string(_list):
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
