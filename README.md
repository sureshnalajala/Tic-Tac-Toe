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

# Implementation:
We created a functional game by implementing minimax/alphabeta pruning using a
TicTacToe class, which contained all the TicTacToe functionalities. After evaluating the
optimal move using the "minimax" and "alphabeta" algorithms, we returned it as the AI
move. To choose the best course of action where AI prevails, we utilize the evaluation
function.
Since it competes with a random agent and modifies values prior to play, the Q-Learning
approach is a little diƯerent. The same TicTacToe class is used in QLearning.py, but a Player
class is also created to define human, random, and Q-Learning agents, respectively. The
player's next move is returned via the get_move(game) method of the Player class, of which
the Q-Learning agent is implemented as a subclass. The Q-Learning agent's get_move
method is responsible for selecting the agent's subsequent move based on the game's
current state and the agent's Q-Table. Every row in the Q-Table corresponds to a game
state, and every column denotes a possible action the agent could perform. The predicted
reward that the agent will obtain if it performs a specific action in a specific condition is
represented by the entries of the Q-Table. The Q-Learning agent competes against a
Random Agent during training, which selects moves at random. The rewards the agent
obtains for each action it takes are used to update its Q-Table as it interacts with the
environment. 

The get_move method of the Q-Learning agent first determines whether the agent should
explore, or exploit based on the value of epsilon, the exploration parameter. The agent
selects a random move from the game's possible moves if a random number between 0
and 1 is less than epsilon. If not, the agent chooses the move that has the highest Q-Value
for the game's present state. The agent adds a new row to the table for the current state and
sets all entries to 0 if the current state is not already in the agent's Q-Table. The agent
chooses the action with the greatest Q-Value for the current condition if it is already in the
agent's Q-Table.
The game makes the move after the agent chooses its move and gives it the index of the
selected square. The reward of the move is then determined by the game and is 0 if the
game is still in progress, 1 if the agent wins, and -1 if the agent loses. In the event that the
game is over, the Q-Learning agent uses the update rule of the Q-Learning algorithm to
update its Q-Table according to the reward it earned for each action it performed
throughout the game.The Q-Learning agent should have a Q-Table at the conclusion of the
training phase that shows the best action-selection strategy for each game state. This table
can then be used by the agent to play the game as best it can. 

# Achievements:
**_1. Q-Learning Metrics:_** <br />
• **Win Rate and Draw Rate**: Measure overall performance. <br />
• **Total Mistakes per Turn**: Measures suboptimal moves. <br />
• **Average Accumulated Rewards**: Tracks how much the agent improves over time. <br />

**_2. Minimax and Alpha-Beta Pruning:_** <br />
• **Optimal Moves**: Both methods guarantee optimal play but differ in computational efficiency: <br />
• **Minimax**: Evaluates the entire game tree. <br />
• **Alpha-Beta Pruning**: Prunes unnecessary branches, significantly improving speed. <br />

# Execution of the Code:
**_• git clone https://github.com/sureshnalajala/Tic-Tac-Toe.git_** <br />
**_• cd Tic-Tac-Toe_** <br />
**_• You can do "ls" for listing the files in Tic-Tac-Toe directory._** <br />
**_• python .\Qlearning.py_** <br />
**_• python .\Minimax.py_** <br />



