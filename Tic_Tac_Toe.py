import tkinter as tk

window = tk.Tk()
window.title("Tic Tac Toe")

buttons = [[None for _ in range(3)] for _ in range(3)]
CUR = 'X'

rl = tk.Label(window, text='', font=('normal', 20))
rl.grid(row=3, column=0, columnspan=3)

def cwin():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != '':
            return True
    for col in range(3):
        if buttons[0][col]['text'] == buttons[1][col]['text'] == buttons[2][col]['text'] != '':
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
            return True
    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
            return True
    return False

def oc(row, col):
    global CUR
    if buttons[row][col]['text'] == '' and CUR != '':
        buttons[row][col]['text'] = CUR
        if cwin():
            rl.config(text=f"Player {CUR} wins")
            reset()
        elif all(buttons[row][col]['text'] != '' for row in range(3) for col in range(3)):
            rl.config(text="Tie")
            reset()
        else:
            CUR = 'O' if CUR == 'X' else 'X'

def reset():
    global CUR
    CUR = 'X'
    for row in range(3):
        for col in range(3):
            buttons[row][col]['text'] = ''

for row in range(3):
    for col in range(3):
        button = tk.Button(window, text='', font=('Times new roman', 42), width=6, height=3,
                           command=lambda row=row, col=col: oc(row, col))
        button.grid(row=row, column=col)
        buttons[row][col] = button

window.mainloop()
