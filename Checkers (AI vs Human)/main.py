import pygame
from checkers.constants import *
from checkers.board import Board
from checkers.game import Game
from AI_Algorithm.minimax import minimax
import math,time

WIN=pygame.display.set_mode((WIDTH,HEIGHTL))     # Initialize the game window
pygame.display.set_caption("CHECKERS")


#Returns position(row,col) where mouse click is detected
def get_curr_mouse_pos(pos):        
    x,y=pos
    row=y//SQ_SIZE
    col=x//SQ_SIZE
    return row,col


def main():
    value=0
    run=True
    clock=pygame.time.Clock()
    game=Game(WIN)      #Initialize the game object

    while run:
        FPS=60          #prevent flickering of board(Refresh Rate)
        clock.tick(FPS)

        if game.turn==WHITE:
            value, new_board=minimax(game.get_board(),4,WHITE,game,-math.inf,math.inf)
            game.ai_move(WIN,new_board)
            print('AI moves',value)

        if game.winner(game)!=None:
            WIN.fill(BLACK)
            if game.winner(game)==BLACK:
                winner='YOU WON'
            elif game.winner(game)==WHITE:
                winner='AI WON'
            elif game.winner(game)==TIE:
                winner='MATCH TIED'

            time.sleep(2)
            
            print('Hurray', winner)
            largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
            winner = largeFont.render(winner, True, WHITE)
            titleRect = winner.get_rect()
            titleRect.center = (WIDTH//2,HEIGHT//2)
            WIN.blit(winner, titleRect)
            pygame.display.update()
            time.sleep(5)
            run=False
            

        for event in pygame.event.get():        #detects keypress Event
            if event.type==pygame.QUIT:         #If user clicks X button,quit the game
                run=False

            if event.type==pygame.MOUSEBUTTONUP:#detect mouse click
                pos=pygame.mouse.get_pos()      #pos in pixel on mouse click
                row,col=get_curr_mouse_pos(pos) #identify row,col through pos

                game.select(WIN,row,col)        #Selects the piece at the current position(mouse clicked here)
    
        game.update()   #Updates game display

    
    pygame.quit()       #Quits pygame


#calling main() func to start game
main()
