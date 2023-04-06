import pygame
from .constants import *
from .pieces import *
from AI_Algorithm.minimax import get_all_moves


class Board:
    def __init__(self):
        self.board=[]
        self.red_left=self.white_left=12   
        self.red_kings=self.white_kings=0  
        self.last_moved_piece = None
        self.create_board()
        

    def draw_squares(self,win):

        pygame.draw.rect(win,WOODEN,(0,0,HEIGHT,WIDTH))
        pygame.draw.line(win,MIDNIGHT,(0,800),(800,800),5)
        for row in range(ROWS):
            for col in range(row%2,ROWS,2): 
                pygame.draw.rect(win,MIDNIGHT,(row*SQ_SIZE, col*SQ_SIZE,SQ_SIZE,SQ_SIZE))
        
        if self.last_moved_piece:
            row, col = self.last_moved_piece.row, self.last_moved_piece.col
            pygame.draw.rect(win, RED, (col * SQ_SIZE, row * SQ_SIZE, SQ_SIZE, SQ_SIZE), 4)
            

    def move(self,piece,row,col):    
        
        self.board[piece.row][piece.col],self.board[row][col] = self.board[row][col],self.board[piece.row][piece.col] #swap the design
        piece.move(row,col)  
          
        self.last_moved_piece = piece
        if row==ROWS-1 or row==0: 
            piece.make_king()           
            if piece.color==WHITE:
                self.white_kings+=1   
            else:
                self.red_kings+=1     


    def get_piece(self,row,col):
        return self.board[row][col]


    def create_board(self):
        
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if(col%2==((row+1)%2)):
                    if row<3:
                        self.board[row].append(Pieces(row,col,WHITE))
                    elif row>4:  
                        self.board[row].append(Pieces(row,col,BLACK))
                    else:
                        self.board[row].append(0)
                else:                            
                    self.board[row].append(0)
    

    def draw(self,win):
        self.draw_squares(win)
        for row in range(ROWS):
            for col in range(COLS):
                piece=self.board[row][col]
                if piece != 0:
                    piece.draw(win)


    def remove(self,pieces):   
        for piece in pieces:   
            self.board[piece.row][piece.col]=0    
            if piece!=0:                  
                if piece.color==BLACK:
                    self.red_left-=1      
                else:
                    self.white_left-=1    


    def winner(self,game): 


        if self.red_left<=0:  
            return WHITE        
        elif self.white_left<=0:  
            return BLACK 
           
        red_moves = get_all_moves(self, BLACK,game)
        white_moves = get_all_moves(self, WHITE,game)
        if len(red_moves) == 0 or len(white_moves) == 0:
            return TIE

        return None    


    def get_valid_moves(self,piece):
        moves={}
        left=piece.col-1
        right=piece.col+1
        row=piece.row

        if piece.color==BLACK or piece.king:
            moves.update(self._traverse_left(row-1,max(row-3,-1),-1,piece.color,left))
            moves.update(self._traverse_right(row-1,max(row-3,-1),-1,piece.color,right))


        if piece.color==WHITE or piece.king:
            moves.update(self._traverse_left(row+1,min(row+3,ROWS),1,piece.color,left))
            moves.update(self._traverse_right(row+1,min(row+3,ROWS),1,piece.color,right))

        return moves


    def _traverse_left(self,start,stop,step,color,left,skipped=[]):
        moves={}
        last=[]
        for r in range(start,stop,step):
            if left<0:
                break
            current =self.board[r][left]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,left)]=last+skipped
                else:
                    moves[(r,left)]=last

                if last:
                    if step==-1:
                        row=max(r-3,-1)
                    else:
                        row=min(r+3,ROWS)
                    moves.update(self._traverse_left(r+step,row,step,color,left-1,skipped=last))
                    moves.update(self._traverse_right(r+step,row,step,color,left+1,skipped=last))
                break
            elif current.color==color:
                break
            else: 
                last=[current]

            left-=1
        return moves


    def _traverse_right(self,start,stop,step,color,right,skipped=[]):
        moves={}
        last=[]
        for r in range(start, stop, step):
            if right>=COLS:
                break

            current=self.board[r][right]
            if current==0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r,right)]=last+skipped
                else:
                    moves[(r,right)]=last

                if last:
                    if step==-1:
                        row=max(r-3, -1)
                    else:
                        row=min(r+3, ROWS)
                    moves.update(self._traverse_left(r+step, row, step, color, right-1,skipped=last))
                    moves.update(self._traverse_right(r+step, row, step, color, right+1,skipped=last))
                break
            elif current.color==color:
                break
            else:
                last=[current]

            right+=1

        return moves
    

    def evaluate(self,game):
        # Piece count
        mainScore= self.white_left - self.red_left + (self.white_kings * 0.5 - self.red_kings * 0.5)

        # King safety
        white_attacks = 0
        red_attacks = 0
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece == WHITE:
                    if self.is_king(piece):
                        if self.is_under_attack(row, col, BLACK):
                            white_attacks += 1
                    else:
                        if self.is_under_attack(row, col, BLACK):
                            white_attacks += 0.5
                elif piece == BLACK:
                    if self.is_king(piece):
                        if self.is_under_attack(row, col, WHITE):
                            red_attacks += 1
                    else:
                        if self.is_under_attack(row, col, WHITE):
                            red_attacks += 0.5
        safety = red_attacks - white_attacks

        # Calculate the final score
        score = mainScore  + safety
        return score


    def get_all_pieces(self,color):
        pieces = [] 
        for row in self.board: 
            for piece in row:   
                if piece!=0 and piece.color==color: 
                    pieces.append(piece)
        return pieces