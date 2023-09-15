import time
from player import HumanPlayer, RandomComputer, GeniusComputerPlayer

class TikTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def is_square_taken(self, square):
        return self.board[square] != ' '

    def board_structure(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    def empty_board(self):
        return ' ' in self.board

    def num_of_empty_string(self):
        return self.board.count(" ")

    @staticmethod
    def board_numbers():
        vim = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in vim:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, square, letter):
        if self.is_square_taken(square):
            print('particular square has been taken')
            return True

        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
               self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #to see for rows
        row_ind = square // 3
        row = self.board[row_ind * 3 : (row_ind + 1) * 3]
        if all([spot == letter for spot in row]):
            return True
        
        #to check for columns
        col_ind = square % 3
        column = [self.board[col_ind+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # to check fordiagonals
        if square % 2 == 0:
            diagonal_1 = [self.board[i] for i in [0, 4, 8]]
            if all(spot == letter for spot in diagonal_1):
                return True

            diagonal_2 = [self.board[i] for i in [2, 4, 6]]
            if all(spot == letter for spot in diagonal_2):
                return True

        return False

    def available_spaces(self):
        return[i for i, spot in enumerate(self.board) if spot == ' ']

def play(game, x_player, o_player, print_game=True):
    if print_game:
        game.board_numbers()

    letter = 'X'
    while game.empty_board():
        if letter == 'O':
            square = o_player.get_moves(game)
        else:
            square = x_player.get_moves(game)

        if game.make_move(square, letter):
            if print_game:
                print(letter + f'make a move to point {square}')
                game.board_structure()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + "wins")
                return letter

            letter = 'O' if letter =='X' else 'X'

        time.sleep(0.8)

    if print_game:
        print('it is a tie')

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TikTacToe()

    play(t, x_player, o_player, print_game=True)
            

        

  


     
