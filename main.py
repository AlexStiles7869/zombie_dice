from game import Game

def main():
    game = Game()
    print(game.current_player.name)
    while game.ongoing:
        game.turn()

if __name__ == "__main__":
    main()