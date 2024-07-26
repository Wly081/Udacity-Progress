import random


"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RockPlayer(Player):
    def move(self):
        return 'rock'
    


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


class HumanPlayer(Player):
    def move(self):
        move = input("Enter your move: rock, paper, or scissors: ").lower()
        while move not in moves:
            move = input("Invalid move. Enter rock, paper, or scissors: ").lower()
        return move


class ReflectPlayer(Player):
    def __init__(self):
        self.their_move = random.choice(moves)

    def move(self):
        return self.their_move

    def learn(self, my_move, their_move):
        self.their_move = their_move


class CyclePlayer(Player):
    def __init__(self):
        self.my_move = random.choice(moves)

    def move(self):
        return self.my_move

    def learn(self, my_move, their_move):
        if my_move == 'rock':
            self.my_move = 'paper'
        elif my_move == 'paper':
            self.my_move = 'scissors'
        elif my_move == 'scissors':
            self.my_move = 'rock'


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if beats(move1, move2):
            self.p1_score += 1
            print("** PLAYER ONE WINS **")
        elif beats(move2, move1):
            self.p2_score += 1
            print("** PLAYER TWO WINS **")
        else:
            print("** TIE **")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        print(f"Score: Player 1: {self.p1_score}, Player 2: {self.p2_score}")

    def play_game(self):
        print("Game start!")
        rounds = int(input("Enter the number of rounds to play: "))
        for round in range(rounds):
            print(f"Round {round + 1}:")
            self.play_round()
        print(f"Final score: Player 1: {self.p1_score}, Player 2: {self.p2_score}")
        if self.p1_score > self.p2_score:
            print("** PLAYER ONE WINS THE GAME **")
        elif self.p2_score > self.p1_score:
            print("** PLAYER TWO WINS THE GAME **")
        else:
            print("** THE GAME IS A TIE **")
        print("Game over!")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RockPlayer())
    game.play_game()
