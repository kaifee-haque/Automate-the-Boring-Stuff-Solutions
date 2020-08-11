#! python3

table_data = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]

def print_table(table):
    
    max_length = []
    for category in table:
        length = 0
        for item in category:
            if len(item) > length:
                length = len(item)
        max_length.append(length)

    for i in range(len(table[0])):
        for j in range(len(table)):
            table[j][i] = table[j][i].rjust(max_length[j])
            print(table[j][i], end = " ")
        print("")
        
print_table(table_data)
