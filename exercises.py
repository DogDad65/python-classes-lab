import os
from typing import Optional

class Game:
    #Game initialization
    def __init__(self):
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board: dict[str, Optional[str]] = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }
    #Clears the terminal
    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')  
    #Starts the game
    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        print("Get ready to play!")
        self.play_round()
    # Prints the board
    def print_board(self):
        b = self.board
        print(f"""
            A   B   C
        1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
            ----------
        2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
            ----------
        3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.winner:
            print(f"Player {self.winner} wins!")
        elif self.tie:
            print("It's a tie!")
        else:
            print(f"It's {self.turn}'s turn.")
    # Handle player input
    def get_move(self):
        while True:
            move = input(f"Player {self.turn}, enter your move (e.g. A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move! Try again.")
    # Check for winner
    def check_for_winner(self):
        winning_combinations = [
            ['a1', 'b1', 'c1'],
            ['a2', 'b2', 'c2'],
            ['a3', 'b3', 'c3'],
            ['a1', 'a2', 'a3'],
            ['b1', 'b2', 'b3'],
            ['c1', 'c2', 'c3'],
            ['a1', 'b2', 'c3'],
            ['c1', 'b2', 'a3']
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] and self.board[combo[0]] is not None:
                self.winner = self.turn
                return True
        return False
    # Check for a tie
    def check_for_tie(self):
        if all(self.board[key] is not None for key in self.board):
            self.tie = True
            return True
        return False
    # Switches turns between players
    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'
    # Main game loop
    def play_round(self):
        while not self.winner and not self.tie:
            self.clear_screen()  # Clear the screen before each turn
            self.print_board()
            self.print_message()
            self.get_move()
            if self.check_for_winner():
                break
            if self.check_for_tie():
                break
            self.switch_turn()
        self.clear_screen()  # Clear the screen one last time at the end
        self.print_board()
        self.print_message()
# Ensures that the game is started.
if __name__ == "__main__":
    game = Game()
    game.play_game()
