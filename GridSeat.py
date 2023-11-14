
def count_adjacent_occupied(grid, row, col):
    """Counts the number of occupied seats adjacent to the given seat in the grid."""
    rows, cols = len(grid), len(grid[0])
    occupied = 0 #keep track of the number of occupied seats
    """checks all adjacent seats (including diagonals) and counts how many of them are occupied."""
    for i in range(max(0, row - 1), min(rows, row + 2)): #iterates over rows adjacent to the seat
        for j in range(max(0, col - 1), min(cols, col + 2)):#iterates over columns adjacent to the seat
            # ensure that the function does not count the seat itself, only the surrounding ones
            if (i, j) != (row, col) and grid[i][j] == '#':
                occupied += 1

    return occupied #returns the number of occupied seats

def apply_rules(grid):
    """Applies the seat occupancy rules to the grid and returns a new grid."""
    rows, cols = len(grid), len(grid[0])#stores the number of rows and columns in grid
    #copy the grid in a list, bcz strings in python are immutable and we need to change grid
    new_grid = [list(row) for row in grid]

    for row in range(rows):#iterate over each row
        for col in range(cols):#for each row iterate over columns
            #apply the first rule
            if grid[row][col] == 'E' and count_adjacent_occupied(grid, row, col) == 0:
                new_grid[row][col] = '#'
            #apply the second rule
            elif grid[row][col] == '#' and count_adjacent_occupied(grid, row, col) >= 4:
                new_grid[row][col] = 'E'

    return ["".join(row) for row in new_grid]#return grid as a string

def count_occupied_seats(grid):
    """Counts the number of occupied seats in the grid."""
    return sum(row.count('#') for row in grid)

def find_stable_occupancy(grid):
    """Finds the number of occupied seats when the grid stabilizes."""
    count = 0#number to find out how many sessions we did
    while True:
        new_grid = apply_rules(grid)
        #count = 0
        if new_grid != grid:
            grid = new_grid
            count += 1
        else:
            break
        #grid = new_grid

    return count_occupied_seats(grid), count

# Specify the path to the input file
input_file_path = 'C:\\Users\\izere\\Downloads\\Take Home Question\\input.txt'
#input_file_path = 'C:\\Users\\izere\\Downloads\\ext.txt'


# Reading the file content
with open(input_file_path, 'r') as file:
    grid = [line.strip() for line in file.readlines()]

# Finding the stable occupancy count
stable_occupancy_count, count = find_stable_occupancy(grid)

print("Stable Occupancy Count:", stable_occupancy_count)
print(f"it took: {count} sessions")
