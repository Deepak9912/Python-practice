import tkinter as tk
from tkinter import font


welcome_message = "Welcome to tic tac toe game"
print(welcome_message)

class gameBoard(tk.TK):
# to get the game board on display
    def __init__(self):
        super().__init__()
        self.title("tic tac toe game")
        self._cells = {}
    
    def _display_board(self):
        display_frame = tk.Frame(master=self)
        display_frame.pack(fill=tk.X)
        self.display = tk.Label(
            master=display_frame,
            text="Ready?",
            font=font.Font(size=28, weight=bold),
        )
        self.display.pack()

    def _create_gameboard_grid(self):
        grid_frame = tk.Frame(master=self)
        grid_frame.pack()

        for row in range(3):
            self.rowconfigure(row, weight=1, minsize=50)



def gameLogic():
# it applies game logic