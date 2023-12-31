import tkinter as tk
from tkinter import Canvas

class Connect_4:
    def __init__(self):
        # https://stackoverflow.com/questions/12791501/why-does-this-code-for-initializing-a-list-of-lists-apparently-link-the-lists-to
        self.board = [[j for j in range(7)] for _ in range(6)]
        self.pl_move = 'pl_1'
        self.pl_not_move = 'pl_2'
        self.pl_1_color = 'red'
        self.pl_2_color = 'yellow'
        self.pl_1_col_hover = "#FF7F7F"
        self.pl_2_col_hover = "#FFFD8F"
        
    def check_win(self):
        for i in range(6):
            for j in range(7):
                if j < 4:
                    # Check victory in a row
                    if self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]:
                        return self.board[i][j], [[i, j], [i, j+1], [i, j+2], [i, j+3]]
                    # Check victory diagonal top to bottom
                    if (i > 2 and 
                        self.board[i][j] == self.board[i-1][j+1] == self.board[i-2][j+2] == self.board[i-3][j+3]):
                        return self.board[i][j], [[i, j], [i-1, j+1], [i-2, j+2],[i-3, j+3]]
                if i < 3:
                    # Check victory in a column
                    if (isinstance(self.board[i][j], str) and 
                        self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]):
                        return self.board[i][j], [[i, j], [i+1, j], [i+2, j], [i+3, j]]
                    # Check victory diagonal bottom to top
                    if (j < 4 and 
                        self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]):
                        return self.board[i][j], [[i, j], [i+1, j+1], [i+2, j+2], [i+3, j+3]]
        return None, None

    def handle_click(self, event):
        # Get the x coordinate of the click and make the move according to that coordinate.
        # 0-100 is move in column 0, 100-200 is move in column 2 e t.c.
        j = event.x // int(width/7)
        self.make_move_player(j)
        self.switch_turns()
        victory, coordinates = self.check_win()
        if victory == "pl_1" or victory == "pl_2":
            # List for drawing winning circles.
            winning_cirscles = [_ for _ in range(4)]
            # Draw white circles on top of the winning line.
            for coord in coordinates:
                i, j = coord[0], coord[1]
                for x in range(4):
                    winning_cirscles[x] = canvas.create_oval(width / 28 + width * j / 7 - width/200, 
                                                             height / 24 + height * i / 6, 
                                                             width * 7.5 / 70 + width * j / 7 - width/200,
                                                             height * 7.5 / 60 + height * i / 6, width = 3, 
                                                             fill="white",  tag="victory")
            for j in range(7):
                for i in range(6):
                    # Unbind all the buttons if the game is over.
                    canvas.tag_unbind(circles[i][j], "<Button-1>")
                    # Change hovering color to white if the game is over.
                    canvas.itemconfig("empty", activefill="white")

    def make_move_player(self, move):
        # Make a move and make changes to the visual representation.
        for i in reversed(range(6)):
            if isinstance(self.board[i][move], int):
                # Save the move.
                self.board[i][move] = self.pl_move
                # Change visuals accordingly.
                canvas.itemconfig(circles[i][move], fill=self.pl_1_color if self.pl_move == "pl_1" else 
                                  self.pl_2_color, activefill=self.pl_1_color if self.pl_move == "pl_1" else 
                                  self.pl_2_color, tag="filled")
                # Switch hovering color to next player's.
                canvas.itemconfig("empty", activefill=self.pl_2_col_hover if self.pl_move == "pl_1" else 
                                  self.pl_1_col_hover)
                return
            
    def switch_turns(self):
        self.pl_move, self.pl_not_move = self.pl_not_move, self.pl_move

game = Connect_4()

window = tk.Tk()
width = 700
height = 600
window.geometry(f"{width}x{height}")
window.title("Connect 4")
window.resizable(False, False)

canvas = Canvas(width=width, height=height, bg="blue")
canvas.pack()
# List of lists for saving circle visual objects.
circles = [[j for j in range(7)] for _ in range(6)]
# Loops for drawing all the circles.
for j in range(7):
    for i in range(6):
        circles[i][j] = canvas.create_oval(width / 140 + width * j / 7 , height / 120 + height * i / 6,
                                           width * 9 / 70 + width * j / 7, height * 3 / 20 + height * i / 6, 
                                           width = 3, fill="white", activefill=game.pl_1_col_hover,  tag="empty")
        # On click on each button, run handle_click method.
        canvas.tag_bind(circles[i][j], "<Button-1>", game.handle_click)

window.mainloop()
