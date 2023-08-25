import tkinter as tk
from tkinter import Canvas

class Connect_4:
    def __init__(self):
        # https://stackoverflow.com/questions/12791501/why-does-this-code-for-initializing-a-list-of-lists-apparently-link-the-lists-to
        self.board = [[j for j in range(7)] for _ in range(6)]
        self.pl_move = 'pl_1'
        self.pl_not_move = 'pl_2'
        
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
                        
    def make_move_player(self, move):
        for i in reversed(range(6)):
            if isinstance(self.board[i][move], int):
                self.board[i][move] = self.pl_move
                canvas.itemconfig(circles[i][move], fill="blue" if self.pl_move == "pl_1" else "red", 
                                  activefill="blue" if self.pl_move == "pl_1" else "red", tag="filled")
                canvas.itemconfig("empty", activefill="#FF7F7F" if self.pl_move == "pl_1" else "#0099FF")
                return
            
    def switch_turns(self):
        self.pl_move, self.pl_not_move = self.pl_not_move, self.pl_move

def make_move(event):
    j = event.x // 100 
    print(game.board)
    game.make_move_player(j)
    game.switch_turns()


game = Connect_4()

window = tk.Tk()
width = 700
height = 600
color = 'orange'
window.geometry(f"{width}x{height}")
window.configure(background="grey")
window.title("Geometry")
window.resizable(False, False)


canvas = Canvas(width=width, height=height, bg="white")
canvas.pack()
circles = [[j for j in range(7)] for _ in range(6)]
for j in range(7):
    for i in range(6):
        circles[i][j] = canvas.create_oval(width / 140 + width * j / 7 , height / 120 + height * i / 6, 
                                    width * 9 / 70 + width * j / 7, 
                                    height * 3 / 20 + height * i / 6, 
                                    width = 3, fill="orange", 
                                    activefill="#0099FF",  tag="empty")
        canvas.tag_bind(circles[i][j], "<Button-1>", make_move)

window.mainloop()
