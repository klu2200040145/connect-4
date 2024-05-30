import tkinter as tk

ROW_COUNT = 6
COLUMN_COUNT = 7
SQUARE_SIZE = 100
WIDTH = COLUMN_COUNT * SQUARE_SIZE
HEIGHT = (ROW_COUNT + 1) * SQUARE_SIZE
BLUE = "#0080FF"
RED = "#FF0000"
YELLOW = "#FFFF00"

def create_board():
    return [[0] * COLUMN_COUNT for _ in range(ROW_COUNT)]

def drop_piece(board, col, player):
    for row in range(ROW_COUNT-1, -1, -1):
        if board[row][col] == 0:
            board[row][col] = player
            return row, col
    return None

def check_win(board, row, col, player):
    count = 0
    for c in range(COLUMN_COUNT):
        if board[row][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    
    count = 0
    for r in range(ROW_COUNT):
        if board[r][col] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
    
    count = 0
    r, c = row, col
    while r > 0 and c > 0:
        r -= 1
        c -= 1
    while r < ROW_COUNT and c < COLUMN_COUNT:
        if board[r][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        r += 1
        c += 1
    
    count = 0
    r, c = row, col
    while r < ROW_COUNT - 1 and c > 0:
        r += 1
        c -= 1
    while r >= 0 and c < COLUMN_COUNT:
        if board[r][c] == player:
            count += 1
            if count == 4:
                return True
        else:
            count = 0
        r -= 1
        c += 1
    
    return False

class ConnectFourGUI:
    def __init__(self, master):
        self.master = master
        self.board = create_board()
        self.player = 1
        self.create_widgets()
    
    def create_widgets(self):
        self.canvas = tk.Canvas(self.master, width=WIDTH, height=HEIGHT)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.drop_piece)

        self.draw_board()

    def draw_board(self):
        for row in range(ROW_COUNT):
            for col in range(COLUMN_COUNT):
                x0 = col * SQUARE_SIZE
                y0 = (row + 1) * SQUARE_SIZE
                x1 = x0 + SQUARE_SIZE
                y1 = y0 + SQUARE_SIZE
                self.canvas.create_rectangle(x0, y0, x1, y1, fill=BLUE, outline="")
                if self.board[row][col] == 1:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=RED, outline="")
                elif self.board[row][col] == 2:
                    self.canvas.create_oval(x0 + 5, y0 + 5, x1 - 5, y1 - 5, fill=YELLOW, outline="")

    def drop_piece(self, event):
        col = event.x // SQUARE_SIZE
        move = drop_piece(self.board, col, self.player)
        if move:
            row, col = move
            self.draw_board()
            if check_win(self.board, row, col, self.player):
                winner = "Player 1" if self.player == 1 else "Player 2"
                tk.messagebox.showinfo("Winner", f"{winner} wins!")
                self.canvas.unbind("<Button-1>")
                return
            self.player = 3 - self.player  # Switch players
    
def main():
    root = tk.Tk()
    root.title("Connect Four")
    gui = ConnectFourGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
