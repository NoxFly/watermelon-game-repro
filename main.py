if __name__ == '__main__':
    import core.config as config
    from core.game import Game

    game = Game(config)
    game.run()