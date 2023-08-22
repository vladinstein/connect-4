class Connect_4:
    def __init__(self):
        # https://stackoverflow.com/questions/12791501/why-does-this-code-for-initializing-a-list-of-lists-apparently-link-the-lists-to
        self.board = [[j for j in range(8)] for i in range(7)]
        
    def check_win(self):
        pass

    def make_move_player(self, move, player):
        self.board[move] = player

    def switch_turns(self, turn):
        turn = not turn

game = Connect_4()
print(game.board)



