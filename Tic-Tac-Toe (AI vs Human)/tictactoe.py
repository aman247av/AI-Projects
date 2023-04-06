"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

#Returns starting state of the board.
def initial_state():
    
    #initial state, board(3 x 3) is empty.
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


#Returns player who has the next turn on a board.
def player(board):      

    #Intial game state, X gets first moves
    if board==initial_state():
        return X;

    #players alternate after each additional moves
    cntX,cntO=0,0
    for row in board:
        cntX+=row.count(X);
        cntO+=row.count(O);
    
    if cntX==cntO:
        return X
    else:
        return O


#Returns set of all possible actions available on the board.
def actions(board):
    
    #checking each box which are marked as EMPTY, thus move is possible there
    all_possible_moves=set()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j]==EMPTY:
                all_possible_moves.add((i,j))

    return all_possible_moves


#Returns whether action made on board from making move (i, j) is a valid action or not.
def result(board, action):

    #making deepcopy of board, original board is left unmodified
    boardcopy=deepcopy(board)

    #Handle Exception
    try:
        if action in actions(boardcopy):        #making valid action move on board
            boardcopy[action[0]][action[1]]=player(boardcopy)
            return boardcopy
        else:       
            raise IndexError        #raising IndexErrorException on invalid move
    
    except IndexError:          #handling Exception
        print('Invalid Action performed on board!')


#Returns the winner of the game, if there is one.
def winner(board):
   
    for i in range(3):
        #check horizontal for winner
        if board[i][0]==board[i][1]==board[i][2] != EMPTY:
            return board[i][0]
        #check vertical for winner
        if board[0][i]==board[1][i]==board[2][i] != EMPTY:
            return board[0][i]

    #check principal diagonal for winner
    if board[0][0]==board[1][1]==board[2][2] != EMPTY:
        return board[0][0]       

    #check secondary diagonal for winner
    if board[0][2]==board[1][1]==board[2][0] != EMPTY:
        return board[0][2]  

    return None


#Returns True if game is over, False otherwise.
def terminal(board):
    
    #game is over by a win, or a tie 
    if winner(board)==None and any(EMPTY in row for row in board):#(no winner or tie(when all cells are full)
        return False
    return True

#Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
def utility(board):
    
    if winner(board)==X:
        return 10
    elif winner(board)==O:
        return -10
    else:
        return 0


#Returns the maximum value and move for the current player using alpha-beta pruning
def max_value_alpha_beta(board,alpha,beta):

    #game over,return utility of board and no move
    if terminal(board):
        return utility(board),None
    
    #intialize -ve inf for best value as it is Max alpha
    best_val,best_move=-math.inf,None

    #Loop through all possible actions and find the action which gives maximum value
    for action in actions(board):
        temp_val, _ = min_value_alpha_beta(result(board,action),alpha,beta) 
        if temp_val > best_val:
            best_val=temp_val
            best_move=action

        alpha=max(alpha,best_val)
        if alpha>=beta:     #pruning as no best move possible from this action
            break

    return best_val,best_move


#Returns the minimum value for the current player using alpha-beta pruning
def min_value_alpha_beta(board,alpha,beta):
    if terminal(board):
        return utility(board),None
    
    #intialize +ve inf for best value as it is Min beta
    best_val,best_move=math.inf,None
    for action in actions(board):
        temp_val, _ = max_value_alpha_beta(result(board,action),alpha,beta) 
        if temp_val < best_val:
            best_val=temp_val
            best_move=action

        beta=min(beta,best_val)
        if alpha>=beta:     #pruning as no best move possible from this action
            break

    #Return the best value and move
    return best_val,best_move


#Returns the optimal action for the current player on the board.
def minimax(board):
    
    if terminal(board):
        return None
    
    current_player=player(board)

    #X is maximizing player and O is minimizing player
    if current_player==X:
        _, move= max_value_alpha_beta(board,-math.inf,math.inf)
    else:
        _, move= min_value_alpha_beta(board,-math.inf,math.inf)
    
    return move
    

