import math
import random
import numpy as np

# Game Class for Tic-Tac-Toe Implementation
class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]  # Initialize grid for playing the game
        self.current_winner = None  # Track the winner of the game
    
    # Display the game grid
    def print_board(self):
        print("-------------")
        for i in range(3):
            row = "| "
            for j in range(3):
                row += self.board[i*3 + j] + " | "
            print(row)
            print("-------------")

    # Available moves (empty cells)
    def get_empty_cells(self):
        return [i for i in range(len(self.board)) if self.board[i] == " "]

    # Determine game outcome
    def check_winner(self):
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i+1] == self.board[i+2] != " ":
                return self.board[i]
        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i+3] == self.board[i+6] != " ":
                return self.board[i]
        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != " ":
            return self.board[0]
        if self.board[2] == self.board[4] == self.board[6] != " ":
            return self.board[2]
        # Check for tie game
        if " " not in self.board:
            return "Tie"
        # No winner yet
        return None

    # Assess state of the grid
    def evaluate(self, ai_player, human_player):
        winner = self.check_winner()
        if winner == ai_player:
            return 1
        elif winner == human_player:
            return -1
        else:
            return 0

# Recursive Minimax logic
def minimax(board, depth, is_maximizing, ai_player, human_player):
    score = game.evaluate(ai_player, human_player)
    if score != 0:
        return score
    if depth == 5:  # Limit depth to avoid infinite recursion
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for cell in game.get_empty_cells():
            new_board = board.copy()
            new_board[cell] = ai_player
            score = minimax(new_board, depth + 1, False, ai_player, human_player)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for cell in game.get_empty_cells():
            new_board = board.copy()
            new_board[cell] = human_player
            score = minimax(new_board, depth + 1, True, ai_player, human_player)
            best_score = min(best_score, score)
        return best_score

# Alpha-Beta Pruning algorithm
def alphabeta(board, depth, alpha, beta, is_maximizing, ai_player, human_player):
    score = game.evaluate(ai_player, human_player)
    if score != 0:
        return score
    if depth == 5:  # Limit depth to avoid infinite recursion
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for cell in game.get_empty_cells():
            new_board = board.copy()
            new_board[cell] = ai_player
            score = alphabeta(new_board, depth + 1, alpha, beta, False, ai_player, human_player)
            best_score = max(best_score, score)
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = float('inf')
        for cell in game.get_empty_cells():
            new_board = board.copy()
            new_board[cell] = human_player
            score = alphabeta(new_board, depth + 1, alpha, beta, True, ai_player, human_player)
            best_score = min(best_score, score)
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score

# AI Move Selection using Minimax or Alpha-Beta
def ai_move(board, ai_player, human_player, AI):
    best_score = float('-inf')
    best_move = None
    for cell in game.get_empty_cells():
        new_board = board.copy()
        new_board[cell] = ai_player
        if AI == 1:  # Minimax
            score = minimax(new_board, 0, False, ai_player, human_player)
        else:  # Alpha-Beta
            score = alphabeta(new_board, 0, float('-inf'), float('inf'), False, ai_player, human_player)
        if score > best_score:
            best_score = score
            best_move = cell
    return best_move

# Get Player's move (human player)
def get_player_move(board, player):
    while True:
        try:
            cell = int(input(f"{player}'s turn. Enter a number from 1-9: ")) - 1
            if cell in game.get_empty_cells():
                return cell
            else:
                print("That cell is not empty. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")

# Game Execution
def play_game():
    board = game.board
    game.print_board()
    ai_player = "O"
    human_player = "X"
    current_player = ai_player

    while True:
        if current_player == ai_player:
            print("AI is making its move...")
            cell = ai_move(board, ai_player, human_player, AI)
        else:
            cell = get_player_move(board, human_player)
        
        board[cell] = current_player
        game.print_board()
        
        winner = game.check_winner()
        if winner is not None:
            if winner == "Tie":
                print("It's a tie!!!")
            else:
                print(f"{winner} won the game!!!")
            break
        
        # Switch players
        if current_player == ai_player:
            current_player = human_player
        else:
            current_player = ai_player

# Choose AI Method (Minimax or Alpha-Beta Pruning)
if __name__ == "__main__":
    print("Tic-Tac-Toe AI: Choose your Strategy")
    AI = int(input("Input your choice (use only the numbers): \n1. MiniMax\n2. Alpha Beta Pruning\n"))
    game = TicTacToe()
    play_game()
