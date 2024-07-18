import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")

        self.CUR = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(root, text='', font=('Arial', 24), width=6, height=3,
                                   command=lambda row=i, col=j: self.click_button(row, col))
                button.grid(row=i, column=j)

    def click_button(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.CUR
            self.update_button(row, col)
            if self.check_winner():
                messagebox.showinfo("result", f"Player {self.CUR} wins!")
                self.reset_board()
            elif self.board_full():
                messagebox.showinfo("result", "It's a tie!")
                self.reset_board()
            else:
                self.CUR = 'O' if self.CUR == 'X' else 'X'

    def update_button(self, row, col):
        button = self.root.grid_slaves(row=row, column=col)[0]
        button.config(text=self.CUR)

    def check_winner(self):
        for row in self.board:
            if all(cell == self.CUR for cell in row):
                return True
        for col in range(3):
            if all(self.board[row][col] == self.CUR for row in range(3)):
                return True
        if all(self.board[i][i] == self.CUR for i in range(3)) or all(self.board[i][2-i] == self.CUR for i in range(3)):
            return True
        return False

    def board_full(self):
        return all(all(cell != ' ' for cell in row) for row in self.board)

    def reset_board(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        for child in self.root.winfo_children():
            if isinstance(child, tk.Button):
                child.config(text='')

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
