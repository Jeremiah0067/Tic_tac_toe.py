import math
import random


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_moves(self):
        pass

class RandomComputer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        square = random.choice(game.available_spaces())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)
    
    def get_moves(self, game):
        val = None
        valid_square = False
        while not valid_square:
            square = input(self.letter + "/s input move from 0-9: ")
            try:
                val = int(square)
                if val not in game.available_spaces():
                    raise ValueError
                valid_square = True

            except ValueError:
                print('input integer')

        return val 

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_moves(self, game):
        if len(game.available_spaces()) == 9:
            square = random.choice(game.available_spaces())
        else:
            square = self.minimax(game, self.letter)['position']

        return square

    def minimax(self, state, player):
        max_player = self.letter # You
        other_player = 'O' if player == 'X' else 'X'

        if state.current_winner == other_player:
            return {'position': None,
                    'score': (1 * state.num_of_empty_string() + 1) if other_player == max_player else (-1 * state.num_of_empty_string() + 1)
                    }

        elif not state.empty_board():
            return {'position':None,
                    'score':0}

        if player == max_player:
            best = {'position': None,
                    'score': -math.inf            
            }
        
        else:
            best = {'position': None,
                    'score': math.inf}

        for possible_moves in state.available_spaces():
            #make a move try that spot
            state.make_move(possible_moves, player)
            #recurse using minimax to simulate a game making that move
            sim_player = self.minimax(state, other_player)

            #Undo the move
            state.board[possible_moves] = ' '
            state.current_winner = None
            sim_player['position'] = possible_moves

            #update the dictionary if necessary
            if player == max_player:
                if sim_player['score'] > best['score']:
                    best = sim_player
                
            else:
                if sim_player['score'] < best['score']:
                    best = sim_player
        
        return best





