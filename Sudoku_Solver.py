#Dan Hrubec
#Sudoku Solver
#2/21/2020



board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

# the main algorithm behind this. it uses backtracking and recursion to find the solution
def solve(bd):
    found = findempty(bd)
    if not found: # setting up the base case
        return True
    else:
        row, col = found
    # else go through each position in the board and try to place numbers in place
    for i in range(1,10):
        if valid(bd, i, (row,col)):
            bd[row][col] = i #if it is valid then good, insert it

            if solve(bd): #recursive call to itself
                return True

            # part of the back tracking, start reseting the previous values
            bd[row][col] = 0
    return False



def valid(bd, num, position):
    #checking if the row has the same number.
    for i in range(len(bd[0])):
        if bd[position[0]][i] == num and position[1] != i: #check through each element in the row, see if the move just made is valud
            return False

    #checking the column, similar to the same logic for row
    for i in range(len(bd)):
        if bd[i][position[1]] == num and position[0] != i: #check through each element in the column, see if the move just made is valid
            return False

    #now checking the 3x3 cube we are in, to see if it is valid. First determine which of 9 boxes we are in
    #integer divide to get the proper box number
    box_X = position[1] // 3
    box_Y = position[0] // 3
    #isolate the loop to be within this box
    for i in range(box_Y * 3,box_Y*3 + 3):
        for j in range(box_X * 3, box_X*3 + 3):
            if bd[i][j] == num and (i,j) != position:
                return False
    #if we make it here, all the other tests failed, so the result must be a valid choice
    return True


#simple print board function. loops through and formats the 9x9 into 9 3x3 like in actual sudoku
def printbd(brd):
    for i in range(len(brd)):
        if i % 3 == 0 and i != 0:
               print("-----------------------") # seperating the columns

        for j in range(len(brd[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(brd[i][j])
            else:
                print(str(brd[i][j]) + " ", end="")

# find this first empty pair going by rows then columns. Hypothetically can be reversed for the same output
def findempty(bd):
    for i in range(len(bd)): # for every row in the matrix
        for j in range(len(bd[0])): #for every column
            if bd[i][j] == 0:  #if the position is empty, return the pair
                return (i,j)

    return None

