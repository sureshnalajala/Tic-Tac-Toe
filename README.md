# Introduction: 
Two search algorithms and a reinforcement learning technique are used in this research to 
implement the game of Tic Tac Toe and determine the AI player's optimal move. Alpha-beta
pruning and minimax are the two search algorithms that are employed, and Q-Learning is
used for reinforcement learning. The minimax algorithm looks through every move that
could be made and assigns a score to each one according to how likely it is that the AI
player will win. The move with the greatest score is then chosen by the algorithm. The
alpha-beta pruning algorithm is similar to minimax, but it tries to eliminate some of the
branches that are guaranteed to be less optimal than others. In certain situations, this
makes the alpha-beta pruning process faster than the minimax algorithm, but it has no
significant eƯect in our situation. Two players alternately place their markings (either "X" or
"O") on the board in this 3x3 grid game. When one player makes three consecutive marks in
a horizontal, vertical, or diagonal direction, or when the board is full and there is no winner
(in a tie game), the game is over. The AI player's mark, the human player's mark, and the
board's current condition are all tracked by the program. The application alternates
between allowing the human player to select a move and allowing the AI player to do so.
The AI player uses the minimax or alpha-beta pruning algorithm to choose the optimal
move when it is its turn. It asks the user to enter a number that matches the cell on the
board that they want to designate when it is their turn to play as the human. 

# Approach Used:
A decision-making algorithm called Minimax is utilized to figure out what a player should
do. Each potential move is given a score after a recursive search of the game tree. The
move with the highest score for the player at that moment and the lowest score for the
opponent is then selected by the algorithm. This reduces the opponent's chances of victory
while guaranteeing that the player will always select the best option. When used with the
Minimax method, alpha-beta pruning is an optimization approach that minimizes the
number of nodes in the search tree that the Minimax algorithm evaluates. As a result, we
may search for the game tree considerably more quickly and even reach deeper levels. An
agent can be trained to play Tic Tac Toe using the reinforcement learning algorithm Qlearning. 
Each state-action pair is given a reward value, which is then updated in response
to environmental feedback. These values are then used by the agent to choose its next
course of action. 
