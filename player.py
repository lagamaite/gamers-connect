class Player:
    name = "" # name of player
    email = "" # email of player
    game_list = [] # list of games, depends on Game class

    # constructor function    
    def __init__(self, name, email, game_list):
        self.name = name
        self.email = email
        self.game_list = game_list
