import pygame
from .board import *
from .constants import *
pygame.init()

class Game:


    def __init__(self,win):
        self._init()        # initialize the game state
        self.win=win


    # method to update the game state and draw the board
    def update(self):
        self.board.draw(self.win)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()


    # helper method to initialize the game state
    def _init(self):
        self.selected=None
        self.board=Board()
        self.turn=BLACK
        self.valid_moves={}


    # method to determine the winner of the game
    def winner(self,game):
        return self.board.winner(game)

    # method to reset the game state
    def reset(self):
        self._init()


    def select(self,win,row,col):
        if self.selected:
            # try to move the selected piece to (row, col)
            result=self._move(win,row,col)
            # if the move is not valid, deselect the piece and select again
            if not result:
                self.selected=None
                self.select(win,row,col)
        
        # get the piece at (row, col)
        piece=self.board.get_piece(row,col)
        # if the piece exists and is the current player's color
        if piece !=0 and piece.color==self.turn:
            self.selected=piece
            # get valid moves for the selected piece
            self.valid_moves=self.board.get_valid_moves(piece)
            return True
        
        return False
    

    def _move(self,win,row,col):
        piece=self.board.get_piece(row,col)
        if self.selected and piece==0 and (row,col) in self.valid_moves:
            # move the selected piece to (row, col)
            self.board.move(self.selected,row,col) 
            print('You moved',(row,col))
            # check if any pieces were skipped during the move
            skipped=self.valid_moves[(row,col)]
            if skipped:
                # remove any skipped pieces from the board
                self.board.remove(skipped)
            self.change_turn(win)
        else:
            return False
        return True
    

    def draw_valid_moves(self,moves):
        for move in moves:
            row,col=move
            pygame.draw.circle(self.win,WHITE,(col*SQ_SIZE+SQ_SIZE//2,row*SQ_SIZE+SQ_SIZE//2),14)
            pygame.draw.circle(self.win,RED,(col*SQ_SIZE+SQ_SIZE//2,row*SQ_SIZE+SQ_SIZE//2),12)
    

    # draw the turn message
    def change_turn(self,win):
            
        self.valid_moves={}
        if self.turn==BLACK:
            pygame.draw.rect(win,BLACK,(0,800,800,50))
            self.turn=WHITE
            title = f"AI Thinking..."
        else:
            pygame.draw.rect(win,BLACK,(0,800,800,50))
            self.turn=BLACK
            title = f"Your turn..."

        largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
        title = largeFont.render(title, True, WHITE)
        titleRect = title.get_rect()
        titleRect.center = (WIDTH//2,820)
        win.blit(title, titleRect)
        pygame.display.update()


    def get_board(self):
        return self.board
    

    def ai_move(self,win,board):
        self.board=board
        self.change_turn(win)       # change to the AI's turn
       