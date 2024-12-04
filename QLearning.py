import random
import numpy as np

# Tic Tac Toe Implementation
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        print('|---|---|---|')
        print('| ' + self.board[0] + ' | ' + self.board[1] + ' | ' + self.board[2] + ' |')
        print('|---|---|---|')
        print('| ' + self.board[3] + ' | ' + self.board[4] + ' | ' + self.board[5] + ' |')
        print('|---|---|---|')
        print('| ' + self.board[6] + ' | ' + self.board[7] + ' | ' + self.board[8] + ' |')
        print('|---|---|---|')

    def available_moves(self):
        return [i for i, x in enumerate(self.board) if x == " "]

    def num_empty_squares(self):
        return self.board.count(" ")

    def make_move(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind+1)*3]
        if all([s == letter for s in row]):
            return True

        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in column]):
            return True

        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True

        return False

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.print_board()

    letter = 'X'
    while game.num_empty_squares() > 0 and not game.current_winner:
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' wins!!!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if print_game:
        print("It's a tie!!!")
    return None

# Player classes (Human, Random for training and QLearning)
class Player:
    def __init__(self, letter):
        self.letter = letter
        self.win_count = 0  # Tracks the number of wins
        self.draw_count = 0  # Tracks the number of draws
        self.mistakes = 0  # Tracks mistakes per turn
        self.total_rewards = 0  # Tracks total accumulated rewards

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = str(int(input(self.letter + "'s turn. Pick a spot (1-9): ")) - 1)
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print("Invalid input. Please select an available spot.")
        return val

class RandomAgent(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        return random.choice(game.available_moves())

    
class QLearningAgent(Player):
    def __init__(self, letter, alpha=0.5, discount=0.9, epsilon=0.1):
        super().__init__(letter)
        self.alpha = alpha
        self.discount = discount
        self.epsilon = epsilon
        self.q_table = {}

        # Metrics tracking
        self.total_mistakes = 0
        self.total_turns = 0
        self.total_rewards = 0
        self.win_count = 0
        self.draw_count = 0

    def get_state(self, game):
        return str(game.board)

    def get_move(self, game):
        state = self.get_state(game)
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)

        # Exploration vs. Exploitation
        if random.uniform(0, 1) < self.epsilon:
            move = random.choice(game.available_moves())
        else:
            move = np.argmax(self.q_table[state])

        # Mistakes per turn metric
        optimal_move = np.argmax(self.q_table[state])
        if move != optimal_move:
            self.total_mistakes += 1
        self.total_turns += 1

        return move

    def update(self, state, action, reward, next_state):
        if state not in self.q_table:
            self.q_table[state] = np.zeros(9)
        if next_state not in self.q_table:
            self.q_table[next_state] = np.zeros(9)

        old_value = self.q_table[state][action]
        next_max = np.max(self.q_table[next_state])

        # Q-Learning formula
        new_value = (1 - self.alpha) * old_value + self.alpha * (reward + self.discount * next_max)
        self.q_table[state][action] = new_value

        # Accumulate rewards for tracking
        self.total_rewards += reward



def play(game, x_player, o_player, print_game=True, track_metrics=False):
    if print_game:
        game.print_board()

    letter = 'X'
    while game.num_empty_squares() > 0 and not game.current_winner:
        if letter == 'X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes a move to square {square}')
                game.print_board()
                print('')

            if game.current_winner:
                if track_metrics:
                    if letter == 'X':
                        x_player.win_count += 1
                        o_player.total_rewards -= 1
                    else:
                        o_player.win_count += 1
                        x_player.total_rewards -= 1

                if print_game:
                    print(letter + ' wins!!!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

    if track_metrics:
        x_player.draw_count += 1
        o_player.draw_count += 1

    if print_game:
        print("It's a tie!!!")
    return None



# Training the QLearning AI with metrics
q_agent = QLearningAgent('O')
r_agent = RandomAgent('X')
t = TicTacToe()

num_episodes = 10000
for i in range(num_episodes):
    play(t, q_agent, r_agent, print_game=False, track_metrics=True)
    if i % 1000 == 0:
        print(f"Finished {i} training games")

mistakes = 0
total_rewards = 0
win_count = 0
draw_count = 0

for episode in range(num_episodes):
    game = TicTacToe()
    state = q_agent.get_state(game)

    while not game.current_winner and game.num_empty_squares() > 0:
        move = q_agent.get_move(game)
        if move not in game.available_moves():
            mistakes += 1  # Increment mistakes for invalid moves
            continue

        game.make_move(move, q_agent.letter)
        reward = 1 if game.current_winner == q_agent.letter else 0
        next_state = q_agent.get_state(game)

        q_agent.update(state, move, reward, next_state)
        state = next_state

    if game.current_winner == q_agent.letter:
        win_count += 1
    elif game.current_winner is None:
        draw_count += 1

    total_rewards += q_agent.total_rewards
    q_agent.total_rewards = 0  # Reset rewards after each episode

# Metrics after training
print("Training Metrics:")
print(f"Total Mistakes per Turn: {mistakes / (num_episodes * 9):.2f}")
print(f"Average Accumulated Rewards: {total_rewards / num_episodes:.2f}")
print(f"Win Rate: {100 * win_count / num_episodes:.2f}%")
print(f"Draw Rate: {100 * draw_count / num_episodes:.2f}%")


# Run the Program
if __name__ == "__main__":
    print("Welcome to Tic Tac Toe!!!")
    while True:
        t = TicTacToe()
        human_agent = HumanPlayer('X')
        q_agent = QLearningAgent('O')  # Reset agent
        winner = play(t, human_agent, q_agent)

        if winner == 'X':
            print("You win!!!")
        elif winner == 'O':
            print("You lose!!!")
        else:
            print("It's a tie!!!")

        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break
