from tkinter import *
from tkinter import messagebox

# Created Some Global Variable
clicked = True
count = 0
winner = False


# Created A Class
class TicTacToe:
    # Initialize ALl The Required Things
    def __init__(self, root):
        self.root = root
        root.title('Tic-Tac-Toe')
        root.wm_iconbitmap('tictactoe.ico')

        # Create A Menu Bar To Reset
        self.Mymenu = Menu(root)
        root.config(menu=self.Mymenu)
        option = Menu(self.Mymenu, tearoff=False)
        self.Mymenu.add_cascade(label='Options', menu=option)
        option.add_command(label='Reset Game', command=self.reset)

        # Create Buttons To Interact With
        self.b1 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b1))
        self.b2 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b2))
        self.b3 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b3))

        self.b4 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b4))
        self.b5 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b5))
        self.b6 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b6))

        self.b7 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b7))
        self.b8 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b8))
        self.b9 = Button(self.root, text=' ', font=('a big deal', 15), height=4, width=7, bg='systembuttonface',
                         command=lambda: self.b_click(self.b9))

        # Grid All Buttons
        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

    # Create A Reset Button To Revert To Its Original State
    def reset(self):
        global clicked, count, winner
        clicked = True
        count = 0
        winner = False
        for b in [self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9]:
            b.config(text=' ', state=NORMAL, bg='systembuttonface')

    # Disables All The Buttons
    def disable_all_button(self):
        self.b1.config(state=DISABLED)
        self.b2.config(state=DISABLED)
        self.b3.config(state=DISABLED)
        self.b4.config(state=DISABLED)
        self.b5.config(state=DISABLED)
        self.b6.config(state=DISABLED)
        self.b7.config(state=DISABLED)
        self.b8.config(state=DISABLED)
        self.b9.config(state=DISABLED)

    # This Will Check If There Is A Winner And If Not It Will Show Draw Message
    def WinnerCheck(self):
        global winner, count
        if self.b1['text'] == 'X' and self.b2['text'] == 'X' and self.b3['text'] == 'X':
            self.b1.config(bg='red')
            self.b2.config(bg='red')
            self.b3.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b4['text'] == 'X' and self.b5['text'] == 'X' and self.b6['text'] == 'X':
            self.b4.config(bg='red')
            self.b5.config(bg='red')
            self.b6.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b7['text'] == 'X' and self.b8['text'] == 'X' and self.b9['text'] == 'X':
            self.b7.config(bg='red')
            self.b8.config(bg='red')
            self.b9.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b1['text'] == 'X' and self.b4['text'] == 'X' and self.b7['text'] == 'X':
            self.b1.config(bg='red')
            self.b4.config(bg='red')
            self.b7.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b2['text'] == 'X' and self.b5['text'] == 'X' and self.b8['text'] == 'X':
            self.b2.config(bg='red')
            self.b5.config(bg='red')
            self.b8.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b3['text'] == 'X' and self.b6['text'] == 'X' and self.b9['text'] == 'X':
            self.b3.config(bg='red')
            self.b6.config(bg='red')
            self.b9.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b1['text'] == 'X' and self.b5['text'] == 'X' and self.b9['text'] == 'X':
            self.b1.config(bg='red')
            self.b5.config(bg='red')
            self.b9.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b3['text'] == 'X' and self.b5['text'] == 'X' and self.b7['text'] == 'X':
            self.b3.config(bg='red')
            self.b5.config(bg='red')
            self.b7.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nX Won\nGame End's")
            self.disable_all_button()

        elif self.b1['text'] == 'O' and self.b2['text'] == 'O' and self.b3['text'] == 'O':
            self.b1.config(bg='red')
            self.b2.config(bg='red')
            self.b3.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b4['text'] == 'O' and self.b5['text'] == 'O' and self.b6['text'] == 'O':
            self.b4.config(bg='red')
            self.b5.config(bg='red')
            self.b6.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b7['text'] == 'O' and self.b8['text'] == 'O' and self.b9['text'] == 'O':
            self.b7.config(bg='red')
            self.b8.config(bg='red')
            self.b9.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b1['text'] == 'O' and self.b4['text'] == 'O' and self.b7['text'] == 'O':
            self.b1.config(bg='red')
            self.b4.config(bg='red')
            self.b7.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b2['text'] == 'O' and self.b5['text'] == 'O' and self.b8['text'] == 'O':
            self.b2.config(bg='red')
            self.b5.config(bg='red')
            self.b8.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b3['text'] == 'O' and self.b6['text'] == 'O' and self.b9['text'] == 'O':
            self.b3.config(bg='red')
            self.b6.config(bg='red')
            self.b9.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b1['text'] == 'O' and self.b5['text'] == 'O' and self.b9['text'] == 'O':
            self.b1.config(bg='red')
            self.b5.config(bg='red')
            self.b9.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()

        elif self.b3['text'] == 'O' and self.b5['text'] == 'O' and self.b7['text'] == 'O':
            self.b3.config(bg='red')
            self.b5.config(bg='red')
            self.b7.config(bg='red')
            messagebox.showinfo('Tic-Tac-Toe', "Congratulations\nO Won\nGame End's")
            self.disable_all_button()
        elif count == 9 and winner == False:
            messagebox.showinfo('Tic-Tac-Toe', 'Draw\nNo One Won')
            self.disable_all_button()

    # This Method Is Responsible To Update The Button And Etc
    def b_click(self, b):
        global clicked, count
        if b['text'] == ' ' and clicked == True:
            b['text'] = 'X'
            clicked = False
            count += 1
            self.WinnerCheck()
        elif b['text'] == ' ' and clicked == False:
            b['text'] = 'O'
            clicked = True
            count += 1
            self.WinnerCheck()
        else:
            messagebox.showerror('Tic-Tac-Toe', 'Please Use Other Box')


# This Code Is For Script Only
if __name__ == '__main__':
    root = Tk()
    app = TicTacToe(root)
    root.mainloop()
