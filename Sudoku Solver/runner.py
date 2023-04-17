import pygame
from sudoku.constants import *
from sudoku.board import *
from SMT_Solver.Z3_SMT_Solver import *

win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Sudoku Solver")

# Set up the font
font = pygame.font.SysFont("Arial", 40)


#function to draw cursor on selected cell
def draw_cursor(x, y):
    cursor_x = x * grid_size
    cursor_y = y * grid_size
    pygame.draw.rect(win, LIGHT_BLUE, (cursor_x, cursor_y, grid_size, grid_size), 3)


#main func
def main(sudoku_copy):

    run=True
    solve=True
    result=True
    board=Board(win)
    selected_cell = None
    clock=pygame.time.Clock()
    
    while run:

        FPS=60          #prevent flickering of board(Refresh Rate)
        clock.tick(FPS)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN and solve:
                # Handle mouse click events
                mouse_pos = pygame.mouse.get_pos()
                cell_x = mouse_pos[0] // (WIN_WIDTH // 9)
                cell_y = mouse_pos[1] // (WIN_HEIGHT // 10)
                selected_cell = (cell_x, cell_y)
                if cell_y!=9:
                    draw_cursor(cell_x,cell_y)
                print("Pressed cell:",selected_cell)

            elif event.type == pygame.KEYDOWN and solve:
            
                if selected_cell is not None and event.unicode.isdigit():
                    # Update the selected cell with the entered number
                    number = int(event.unicode)
                    try:
                        sudoku_grid[selected_cell[1]][selected_cell[0]] = number
                    except IndexError:
                        pygame.display.update()
                        continue

                    selected_cell = None
                    print(number)
                    board.update_screen(win,sudoku_grid,sudoku_copy)
            
            if event.type == pygame.MOUSEBUTTONDOWN and solve:
                # Check if solve button is pressed
                if button_rect.collidepoint(event.pos):
                    solve=False
                    sudoku_copy=copy.deepcopy(sudoku_grid)
                    board.make_btn(win,"WAIT")
                   
                    # Solve the Sudoku puzzle using the z3-SMT solver 
                    result=Z3_SMT(win,sudoku_grid)
                
                    board.update_screen(win,sudoku_grid,sudoku_copy)
                    if result==False:
                        break
                    board.make_btn(win,"SOLUTION")

        if result==False:
            board.make_btn(win,"NO SOL.")
        pygame.display.update()
     
    pygame.quit()       # Quit Pygame
    
#Inital board State
sudoku_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

#Create a copy of the empty Sudoku grid
sudoku_copy = copy.deepcopy(sudoku_grid)

main(sudoku_copy)