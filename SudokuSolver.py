'''
Created on July. 6, 2021
Randomly generates a 9x9 Sudoku grid based on the user's desired level of difficulty.
When desired, the user may reveal a possible solution to the Sudoku grid.
@author: Tao Shen
'''

## Imports libraries used in the program
from random import shuffle, randint
import copy
import string

if __name__ == '__main__':
    pass

## Creates the empty Sudoku grid.
grid = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
]

## Randomly fills the board to create a random solution.
def grid_solution(grid):
    
    ## Creates list of numbers that will later be randomly shuffled.
    num_list = [1,2,3,4,5,6,7,8,9]
    
    ## Calls check_empty to check if the grid has filled up with numbers.
    empty = check_empty(grid)
    if empty == None:
        return True
    row, col = empty
    
    ## Shuffles the list of numbers.
    shuffle(num_list)
    
    ## Checks the validity of a number in the list entering a specific position on the grid.
    for num in num_list:
        if check_valid(grid, num, row, col):
            grid[row][col] = num        
            if grid_solution(grid):
                return True
            grid[row][col] = 0
    return False    
    
## Deletes numbers from the filled-in solution. The number of numbers deleted varies depending on the level of difficulty chosen.
def num_deleter(grid):
    
    # Creates a global variable called checker.
    global checker
    
    # Declares variables.
    valid= 0
    numdel = 0
    
    # Loops until the user inputs a valid level of difficulty.
    while valid != 1:
        
        # Asks user to input their desired level of difficulty.
        diff = str(input("Enter level of difficulty: Easy, Medium, Hard\n"))
        
        # Checks user input and changes the number of values that will be deleted from the solved Sudoku.
        if diff.upper() == "EASY":
            numdel = 0
            valid = valid + 1
            checker = "easy"
        elif diff.upper() == "MEDIUM":
            numdel = 10
            valid = valid + 1
            checker = "medium"
        elif diff.upper() == "HARD":
            numdel = 18
            valid = valid + 1
            checker = "hard"
    
    tempnumdel = numdel
    
    # Loops until the appropriate number of numbers have been removed from the Sudoku grid.
    while numdel - tempnumdel < 36:
        
        # Randomly selects a position in the grid that has not yet been deleted..
        x = randint(0, 8)
        y = randint(0, 8)
        while grid[x][y] == 0:
            x = randint(0, 8)
            y = randint(0, 8)
        
        # Stores the original value in a temporary spot.
        temp = grid[x][y]
        
        # Changes the grid value to 0 indicating the value has been deleted.
        grid[x][y] = 0
        copygrid = copy.deepcopy(grid)
        
        # Checks if the board after having one value deleted is still possible to solve.
        if solver(copygrid) == True:
            
            # If the Sudoku grid is still possible to solve, numdel is incremented by 1.
            numdel = numdel + 1
        else:
            
            # If the Sudoku grid is no longer solvable, the deletion is reverted.
            grid[x][y] = temp
    return True
    
# Solves the Sudoku with the help of the check_valid helper function.
def solver(grid):
    
    # Repeats the function until the grid has no more 0's to replace.
    empty = check_empty(grid)
    if empty == None:
        return True
    else:
        row, col = empty
    
    # Checks if a number can go in a specific position.
    for num in range(1, 10):
        if check_valid(grid, num, row, col):
            grid[row][col] = num
            
            # Calls itself, the solver function.
            if solver(grid):
                return True
            grid[row][col] = 0
    return False
            
# Checks if it is valid for a number to be input into a specific position.
def check_valid(grid, num, row, col):
    
    # Check row
    for x in range(0, 9):
        if grid[row][x] == num:
            return False
    
    # Check column
    for y in range(0, 9):
        if grid[y][col] == num:
            return False
    
    # Check box
    box_x = (row // 3) * 3
    box_y = ((col) // 3) * 3
    for a in range(0, 3):
        for b in range(0, 3):
            if grid[a + box_x][b + box_y] == num:
                return False
            
    return True

# Prints the grid with dividers between each 3x3 box to help readability.
def printer(grid):
    for x in range(len(grid)):
        if x % 3 == 0 and x != 0:
            print("- - - - - - - - - - - ")
             
        for y in range(0,9):
            loca = grid[x][y]
            if y % 3 == 0 and y != 0:
                print("| ", end = "")
            if y == 8:
                print(loca)
            else:
                print(str(loca) + " ", end = "") 

# Helper function checks if a position in the grid is empty.
def check_empty(grid):
    
    # Logops through the grid positions.
    for x in range(len(grid)):
        for y in range(0,9):
            loca = grid[x][y]
            
            #Checks if the position is empty.
            if loca == 0:
                return x, y
    return None

# Calls functions and prints lines to guide the user.
grid_solution(grid)
num_deleter(grid)
print("Here is your", checker, "difficulty Sudoku board, good luck!\n")
printer(grid)
check_empty(grid)
solver(grid)
solution = input("\nEnter anything to see one of the possible solutions for your grid.")
print("\nSolved solution is below: \n")
printer(grid)