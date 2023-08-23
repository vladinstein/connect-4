import tkinter as tk
from tkinter import Canvas

class Connect_4:
    def __init__(self):
        # https://stackoverflow.com/questions/12791501/why-does-this-code-for-initializing-a-list-of-lists-apparently-link-the-lists-to
        self.board = [[j for j in range(7)] for i in range(6)]
        
    def check_win(self):
        pass

    def make_move_player(self, move, player):
        for i in range(7):
            if isinstance(self.board[i][move], int):
                self.board[i][move] = player
                return i
            
    def switch_turns(self, turn):
        turn = not turn


game = Connect_4()

active_pl = "pl_1"
passive_pl = "pl_2"
turn = True
for i in range(42):
    move = int(input('Enter your move'))
    i = game.make_move_player(move, active_pl)
    active_pl, passive_pl = passive_pl, active_pl
    print(game.board)



window = tk.Tk()
window.geometry("800x800")
window.configure(background="grey")
window.title("Geometry")
window.resizable(False, False)

canvas = Canvas(width="750", height="750", bg="white")
canvas.pack(pady = 20)

button = canvas.create_oval(5, 5, 100, 100, width = 3, fill="orange", activefill="blue")
canvas.create_oval(105, 5, 205, 100, width = 3, fill="orange")


window.mainloop()

