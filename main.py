from game import Game
from player import Player

PLAYER_COUNT = 4
POINTS_TO_WIN = 10

if __name__ == "__main__":
    players = [Player(str(i), str(i), i) for i in range(PLAYER_COUNT)]
    game = Game(players, POINTS_TO_WIN)
    game.loop()
    print(game.winner)
