import tkinter as tk
from tkinter import Canvas

class Connect_4:
    def __init__(self):
        # https://stackoverflow.com/questions/12791501/why-does-this-code-for-initializing-a-list-of-lists-apparently-link-the-lists-to
        self.board = [[j for j in range(7)] for i in range(6)]
        
    def check_win(self):
        for i in range(6):
            for j in range(7):
                if j < 4:
                    # Check victory in a row
                    if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j]
                    # Check victory diagonal top to bottom
                    if (i > 2 and 
                        self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]):
                        return self.board[i][j]
                if i < 3:
                    # Check victory in a column
                    if (isinstance(self.board[i][j], str) and 
                        self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
                        return self.board[i][j]
                    # Check victory diagonal bottom to top
                    if (j < 4 and 
                        self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
                        return self.board[i][j]
                        
    def make_move_player(self, move, player):
        for i in range(6):
            if isinstance(self.board[i][move], int):
                self.board[i][move] = player
                return i
            
    def switch_turns(self, turn):
        turn = not turn


game = Connect_4()

window = tk.Tk()
width = 700
height = 600
window.geometry(f"{width}x{height}")
window.configure(background="grey")
window.title("Geometry")
window.resizable(False, False)

canvas = Canvas(width=width, height=height, bg="white")
canvas.pack()
for i in range(7):
    button = canvas.create_oval(width / 140 + width * i / 7 , height / 120, width * 9 / 70 + width * i / 7, 
                                height * 3 / 20, width = 3, fill="orange", activefill="blue")



active_pl = "pl_1"
passive_pl = "pl_2"
turn = True
for i in range(42):
    move = int(input('Enter your move'))
    i = game.make_move_player(move, active_pl)
    active_pl, passive_pl = passive_pl, active_pl
    print(game.board)
    winner = game.check_win()
    print(winner)


window.mainloop()
