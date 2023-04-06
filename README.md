# AI Projects (CS235 / CS50 AI)
This repository contains projects related to Artificial Intelligence, which were developed as part of the CS 235 course at IIIT Guwahati.

Reference has been taken from Harvard's CS50 AI course and TechWithTim.

## Projects
1. Tic Tac Toe 
2. Checkers

Implementation of Game Theory, Min-Max algorithm, and Alpha-Beta Pruning.

### Tic Tac Toe
The Tic Tac Toe project is an implementation of the game using game theory concepts and algorithms. The computer player uses the Min-Max algorithm with Alpha-Beta pruning to decide its moves. The project is developed using Python programming language, and the user interface is built using the Pygame library.

### Checkers
Checkers is a two-player board game that is played on an 8x8 checkered board. Each player starts with 12 pieces called checkers, which are placed on the dark squares of the board. The objective of the game is to capture all of the opponent's pieces or block them so that they cannot make a move. The game involves strategic planning, and players need to think ahead to anticipate their opponent's moves. In this project, the game has been implemented using game theory concepts and algorithms like Min-Max with Alpha-Beta pruning to create an intelligent computer player.

## Installation
To run the projects, make sure you have Python 3.x installed on your system. To check, open the command prompt (Windows) or terminal (Mac/Linux) and type 'python --version'. 

If Python is not installed on your system, you can download and install it from the official Python website: https://www.python.org/downloads/


1. Clone the repository using the following command: 
   ```
   git clone https://github.com/aman247av/AI-Projects.git
   ```
   
2. Navigate to the project folder using the following command: 
   ```
   cd AI-Projects/<project-name>
   ```

3. Install the required packages using the following command: 
   ```
   pip install -r requirements.txt
   ```
   
4. Run the project using the following command: 
   ```
   python runner.py
   ```
   
## Minimax Algorithm (Using Tic-Tac-Toe)

Minimax is a artificial intelligence algorithm applied to a two player Tic Tac Toe game. This games are known as zero-sum games, because in a mathematical representation: one player wins (+10) and other player loses (-10) or both of anyone not to win (0).

Minimax is a recursive algorithm which is used to choose the best move that leads the Max player to win or not lose (draw). It consider the current state of the game and the available moves at that state, then for each valid move it plays (alternating min and max) until it finds a terminal state - win, draw or lose.

Its goal is to minimize the maximum loss i.e. minimize the worst case scenario.

#### Explanation with Example

To apply this, let's take an example from near the end of a game, where it is my turn. I am X. My goal here, obviously, is to maximize my end game score.

<p align="center"><img src="Images/Minimax_1.png" width="450" height="290" /></p>

If the top of this image represents the state of the game when it is my turn, then I have some choices to make, there are three places I can play, one of which clearly results in me wining and earning the 10 points. If I don't make that move, O could very easily win. And I don't want O to win, so my goal here, as the first player, should be to pick the maximum scoring move.

#### But What About O?

We should assume that O is also playing to win this game, but relative to us, the first player, O wants obviously wants to chose the move that results in the worst score for us, it wants to pick a move that would minimize our ultimate score. Let's look at things from O's perspective, starting with the two other game states from above in which we don't immediately win.

<p align="center"><img src="Images/Minimax_2.png" width="450" height="290" /></p>

The choice is clear, O would pick any of the moves that result in a score of -10.

#### Describing Minimax

The key to the Minimax algorithm is a back and forth between the two players, where the player whose "turn it is" desires to pick the move with the maximum score. In turn, the scores for each of the available moves are determined by the opposing player deciding which of its available moves has the minimum score. And the scores for the opposing players moves are again determined by the turn-taking player trying to maximize its score and so on all the way down the move tree to an end state.

A description for the algorithm, assuming X is the turn taking player:

* If the game is over, return the score from X's perspective.
* Otherwise get a list of new game states for every possible move.
* Create a scores list.
* For each of these states add the minimax result of that state to the scores list.
* If it's X's turn, return the maximum score from the scores list.
* If it's O's turn, return the minimum score from the scores list. 

Let's walk through the algorithm's execution with the full move tree, and algorithmically, how the instant winning move will be picked:

<p align="center"><img src="Images/Minimax_3.png" width="450" height="290" /></p>

* It's X's turn in state 1. X generates the states 2, 3, and 4 and calls minimax on those states.
* State 2 pushes the score of +10 to state 1's score list, because the game is in an end state.
* State 3 and 4 are not in end states, so 3 generates states 5 and 6 and calls minimax on them, while state 4 generates states 7 and 8 and calls minimax on them.
* State 5 pushes a score of -10 onto state 3's score list, while the same happens for state 7 which pushes a score of -10 onto state 4's score list.
* State 6 and 8 generate the only available moves, which are end states, and so both of them add the score of +10 to the move lists of states 3 and 4.
* Because it is O's turn in both state 3 and 4, O will seek to find the minimum score, and given the choice between -10 and +10, both states 3 and 4 will yield -10.
* Finally the score list for states 2, 3, and 4 are populated with +10, -10 and -10 respectively, and state 1 seeking to maximize the score will chose the winning move with score +10, state 2.

Let's see what is happening here by looking through the possible move tree:

<p align="center"><img src="Images/Minimax_4.png" width="450" height="290" /></p>

* Given the board state 1 where both players are playing perfectly, and O is the computer player. O choses the move in state 5 and then immediately loses when X wins in state 9.
* But if O blocks X's win as in state 3, X will obviously block O's potential win as shown in state 7.
* This puts two certain wins for X as shown in state 10 and 11, so no matter which move O picks in state 7, X will ultimately win.

Another important factor in this algorithm is depth. 

The key improvement to this algorithm, such that, no matter the board arrangement, the perfect player will play perfectly, is to take the "depth" or number of turns till the end of the game into account. Basically the perfect player should play perfectly, but prolong the game as much as possible.

So each time we invoke minimax, depth is incremented by 1 and when the end game state is ultimately calculated, the score is adjusted by depth.
 
Since this is a very complex algorithm, we have a computer to execute this algorithm.

