#! python3

def print_table(table):
    """Prints a given list as a text-based table, right-justified for each
    column.
    
    Args:
        table: A list of lists representing the columns of items in the table.
    """

    #Finds the length of the longest string in each category, then stores
    #these lengths in an array.
    
    max_length = []
    for category in table:
        length = 0
        for item in category:
            if len(item) > length:
                length = len(item)
        max_length.append(length)

    #For each column, print the item, right-justified according to the
    #array of lengths.

    for i in range(len(table[0])):
        for j in range(len(table)):
            table[j][i] = table[j][i].rjust(max_length[j])
            print(table[j][i], end = " ")
        print("")

table_data = [["apples", "oranges", "cherries", "banana"],
             ["Alice", "Bob", "Carol", "David"],
             ["dogs", "cats", "moose", "goose"]]
print_table(table_data)
