#! python3
"""Prints a grid from a list of lists of characters."""

test_grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def picture_grid(grid):
    """Takes a list of lists containing characters and prints a grid.

    Args:
        grid: The list of lists containing the characters.
    """
    
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            print(grid[row][column], end = "")
        print("")

picture_grid(test_grid)
