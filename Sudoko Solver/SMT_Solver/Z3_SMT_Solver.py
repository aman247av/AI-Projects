from z3 import *

def Z3_SMT(win,sudoku_grid):
    sudoko = Solver()

    grid = [[Int("x_%s_%s" % (i, j)) for j in range(9)] for i in range(9)]      #creating variable for each cell

    #Constraint for each cell
    for i in range(9):
        for j in range(9):
            cell_constraint = And(grid[i][j]>=1, grid[i][j]<=9)     #each cell has a value from 1 to 9
            sudoko.add(cell_constraint)                             #Add cell constraint to the solver


    #Constraint for each row
    for i in range(9):
        row = [grid[i][j] for j in range(9)]            #Get variables for the cells in i-th row
        row_constraint = Distinct(row)                  #Each row contains all numbers from 1 to 9 exactly once
        sudoko.add(row_constraint)                      #Add row constraint to the solver


    #Constraint for each column
    for j in range(9):
        col = [grid[i][j] for i in range(9)]            #Get variables for the cells in i-th column
        col_constraint = Distinct(col)                  #Each column contains all numbers from 1 to 9 exactly once
        sudoko.add(col_constraint)                      #Add column constraint to the solver


    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            subgrid = [grid[x][y] for x in range(i, i+3) for y in range(j, j+3)]        #variables for the cells in the (i,j)-th sub-grid
            subgrid_constraint = Distinct(subgrid)                                      #sub-grid contains all numbers from 1 to 9 exactly once   
            sudoko.add(subgrid_constraint)                                              #Add the sub-grid constraint to the solver


    for i in range(9):
        for j in range(9):
            try:
                if sudoku_grid[i][j]!=0:
                    sudoko.add(grid[i][j]==sudoku_grid[i][j])
                    
            except Z3Exception:
                sudoku_grid[i][j]=0


    if sudoko.check() == sat:
        solution = sudoko.model()
        for i in range(9):
            for j in range(9):
                sudoku_grid[i][j]=solution.eval(grid[i][j])
                print(sudoku_grid[i][j], end=' ')
            print()
        return True
    else:
        print("No solution found.")
        return False



