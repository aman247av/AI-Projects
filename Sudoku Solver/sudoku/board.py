import pygame
from sudoku.constants import *

# Initialize Pygame
pygame.init()

font = pygame.font.SysFont("Arial", 40)
font2 = pygame.font.SysFont("Arial", 36)

button_surface = pygame.Surface((BUTTON_WIDTH, BUTTON_HEIGHT))
button_rect = button_surface.get_rect()

class Board:

    def __init__(self,win):
        self.make_board(win)
        self.make_btn(win,"SOLVE IT")

    def make_btn(self,win,txt):
        
        # Set button position
        button_rect.center = (WIN_WIDTH // 2, WIN_HEIGHT - (BUTTON_HEIGHT // 2)-5)
        text = font2.render(txt, True, WHITE)
        text_rect = text.get_rect(center=button_surface.get_rect().center)
        button_surface.fill(BLACK)
        button_surface.blit(text, text_rect)

        # Draw button on the window
        win.blit(button_surface, button_rect)
        pygame.display.update()

    def make_board(self,win):

        win.fill(WHITE)
        
        # Draw the Sudoku grid
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(win, BLACK, (i*60, j*60, 60, 60), 1)
    
        # Draw the Sudoku grid
        for i in range(9):
            for j in range(9):
                pygame.draw.rect(win, BLACK, (i*60, j*60, 60, 60), 1)
    
        #draw the sub-grid
        for i in range(10):
            if i % 3 == 0:
                thickness = 4
            else:
                thickness = 1
            pygame.draw.line(win, BLACK, (grid_size*i, 0), (grid_size*i, grid_height), thickness)
            pygame.draw.line(win, BLACK, (0, grid_size*i), (grid_width, grid_size*i), thickness)

    # Draw the numbers on the board
    def draw_numbers(self,win,sudoku_grid,sudukoCopy):
        for i in range(9):
            for j in range(9):
                if str(sudukoCopy[i][j]) != "0":
                    num_surface = font.render(str(sudukoCopy[i][j]), True, BLACK)
                    win.blit(num_surface, (j*60+20, i*60+10))
                else:
                    if str(sudoku_grid[i][j]) != "0":
                        num_surface = font.render(str(sudoku_grid[i][j]), True, LIGHT_BLUE)
                        win.blit(num_surface, (j*60+20, i*60+10))

        
    def update_screen(self,win,sudoku_grid,sudukoCopy):
        self.make_board(win)
        self.draw_numbers(win,sudoku_grid,sudukoCopy)
        self.make_btn(win,"SOLVE IT")
        pygame.display.flip()


