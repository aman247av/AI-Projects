from copy import deepcopy
from checkers.constants import *
import math 


#define the minimax algorithm function
def minimax(board,depth, max_player, game, alpha, beta):
    
    # base case: when the maximum depth is reached or a winner is found
    if depth == 0 or board.winner(game) != None:
        return board.evaluate(game), board
    
    # maximizing player's turn
    if max_player:

        best_val,best_move=-math.inf,None
        # loop through all possible moves for the current player
        for move in get_all_moves(board,WHITE,game):
            temp_val,_ =minimax(move,depth-1,False,game,alpha,beta)
            # update best value and move if temp_val is better
            if temp_val > best_val:
                best_val=temp_val
                best_move=move

            # apply alpha-beta pruning to reduce the search space
            alpha=max(alpha,best_val)
            if alpha>=beta:     #pruning as no best move possible from this action
                break

        return best_val,best_move
    
    # minimizing player's turn
    else:
        best_val,best_move=math.inf,None
        # loop through all possible moves for the current player
        for move in get_all_moves(board,BLACK,game):
            # update best value and move if temp_val is better
            temp_val,_ =minimax(move,depth-1,True,game,alpha,beta)
            if temp_val < best_val:
                best_val=temp_val
                best_move=move

            # apply alpha-beta pruning to reduce the search space
            beta=min(beta,best_val)
            if alpha>=beta:     #pruning as no best move possible from this action
                break

        return best_val,best_move


# function to get all possible moves for a given player
def get_all_moves(board,color,game):
    
    moves=[]
    # loop through all pieces of the given color
    for piece in board.get_all_pieces(color):
        # get all valid moves for the current piece
        valid_moves=board.get_valid_moves(piece)
        
        for move, skip in valid_moves.items(): 
            # simulate the move and add the resulting board to the list of moves
            temp_board = deepcopy(board)   
            temp_piece = temp_board.get_piece(piece.row, piece.col)  
            new_board = simulate_move(temp_piece, move, temp_board, game, skip)
            moves.append(new_board) 

    return moves  


# function to simulate a move and return the resulting board
def simulate_move(piece, move, board, game, skip): 
    board.move(piece, move[0], move[1]) 
    if skip:    
        board.remove(skip)  
    return board  
