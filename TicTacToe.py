import tkinter as tk
from tkinter import messagebox

class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Tic Tac Toe")
        self.current_player = 'X'
        self.opponent = 'O'
        self.buttons = [None] * 9

        for i in range(3):
            for j in range(3):
                index = i * 3 + j
                button = tk.Button(master, text='', font=('normal', 25, 'bold'), fg='white', bg='black', width=7, height=3,
                                   command=lambda idx=index: self.action(idx))
                button.grid(row=i, column=j)
                self.buttons[index] = button

    def validmove(self, row, col):
        if 0 <= row < 3 and 0 <= col < 3 and self.buttons[row * 3 + col]['text'] == '':
            return True
        else:
            return False

    def switch(self):
        self.current_player, self.opponent = self.opponent, self.current_player

    def find_winner(self):
        for i in range(3):
            if (self.buttons[i * 3]['text'] == self.current_player and
                    self.buttons[i * 3 + 1]['text'] == self.current_player and
                    self.buttons[i * 3 + 2]['text'] == self.current_player):
                return self.current_player
            if (self.buttons[i]['text'] == self.current_player and
                    self.buttons[i + 3]['text'] == self.current_player and
                    self.buttons[i + 6]['text'] == self.current_player):
                return self.current_player
        if (self.buttons[0]['text'] == self.current_player and
                self.buttons[4]['text'] == self.current_player and
                self.buttons[8]['text'] == self.current_player):
            return self.current_player
        if (self.buttons[2]['text'] == self.current_player and
                self.buttons[4]['text'] == self.current_player and
                self.buttons[6]['text'] == self.current_player):
            return self.current_player
        return None

    def action(self, idx):
        row, col = divmod(idx, 3)
        if not self.validmove(row, col):
            print("Invalid Move")
            return
        else:
            self.buttons[idx]['text'] = self.current_player
            winner = self.find_winner()

            if winner:
                messagebox.showinfo("Game Over", f"{winner} wins!")
                self.reset_board()
            elif all(button['text'] != '' for button in self.buttons):
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_board()
            else:
                self.switch()

    def reset_board(self):
        for button in self.buttons:
            button['text'] = ''
        self.current_player = 'X'


root = tk.Tk()
app = TicTacToeGUI(root)
root.mainloop()
