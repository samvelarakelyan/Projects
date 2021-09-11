from tkinter import (Tk, Frame, Label, IntVar, StringVar,
                     Button, CENTER, LEFT, RIDGE, RIGHT,
                     Entry)
import tkinter.messagebox


root = Tk()
root.geometry("1750x750+0+0")
root.title("Tic Tac Toe")
root.configure(background="Blue")


Tops = Frame(root, bg="Blue", pady=2, width=1350,
             height=100, relief=RIDGE)
Tops.grid(row=0, column=0)

lb1Title = Label(Tops, font=("arial", 50, "bold"), text="Tic Tac Toe Game",
                 bd=21, bg="Blue", fg="Cornsilk", justify=CENTER)
lb1Title.grid(row=0, column=0)

MainFrame = Frame(root, bg="Powder Blue", pady=2, width=1350,
                  height=600, relief=RIDGE)
MainFrame.grid(row=1, column=0)

LeftFrame = Frame(MainFrame, bd=10, width=700, height=500,
                  pady=2, padx=10, bg="Blue", relief=RIDGE)
LeftFrame.pack(side=LEFT)

RightFrame = Frame(MainFrame, bd=10, width=500, height=500,
                   pady=2, padx=10, bg="Blue", relief=RIDGE)
RightFrame.pack(side=RIGHT)

RightFrame1 = Frame(RightFrame, bd=10, width=500, height=200,
                    pady=2, padx=10, bg="Blue", relief=RIDGE)
RightFrame1.grid(row=0, column=0)

RightFrame2 = Frame(RightFrame, bd=10, width=500, height=200,
                    pady=2, padx=10, bg="Blue", relief=RIDGE)
RightFrame2.grid(row=1, column=0)


playerX = IntVar()
playerO = IntVar()


playerX.set(0)
playerO.set(0)


button = StringVar()

click = True


def checker(buttons):
    global click
    if buttons["text"] == " " and click:
        buttons["text"] = "X"
        click = False
    elif buttons["text"] == " " and not click:
        buttons["text"] = "O"
        click = True

    scoreKeeper()


def reset():
    button1["text"] = " "
    button2["text"] = " "
    button3["text"] = " "
    button4["text"] = " "
    button5["text"] = " "
    button6["text"] = " "
    button7["text"] = " "
    button8["text"] = " "
    button9["text"] = " "

    button1.configure(bg="gainsboro")
    button2.configure(bg="gainsboro")
    button3.configure(bg="gainsboro")
    button4.configure(bg="gainsboro")
    button5.configure(bg="gainsboro")
    button6.configure(bg="gainsboro")
    button7.configure(bg="gainsboro")
    button8.configure(bg="gainsboro")
    button9.configure(bg="gainsboro")


def newGame():
    reset()
    playerX.set(0)
    playerO.set(0)


def scoreKeeper():
    # For X============================
    if button1["text"] == "X" and\
            button2["text"] == "X" and\
            button3["text"] == "X":

        button1.configure(bg="green")
        button2.configure(bg="green")
        button3.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button4["text"] == "X" and\
            button5["text"] == "X" and\
            button6["text"] == "X":

        button4.configure(bg="green")
        button5.configure(bg="green")
        button6.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button7["text"] == "X" and\
            button8["text"] == "X" and\
            button9["text"] == "X":

        button7.configure(bg="green")
        button8.configure(bg="green")
        button9.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button3["text"] == "X" and\
            button5["text"] == "X" and\
            button7["text"] == "X":

        button3.configure(bg="green")
        button5.configure(bg="green")
        button7.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button1["text"] == "X" and\
            button5["text"] == "X" and\
            button9["text"] == "X":

        button1.configure(bg="green")
        button5.configure(bg="green")
        button9.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button1["text"] == "X" and\
            button4["text"] == "X" and\
            button7["text"] == "X":

        button1.configure(bg="green")
        button4.configure(bg="green")
        button7.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button2["text"] == "X" and\
            button5["text"] == "X" and\
            button8["text"] == "X":

        button2.configure(bg="green")
        button5.configure(bg="green")
        button8.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    if button3["text"] == "X" and\
            button6["text"] == "X" and\
            button9["text"] == "X":

        button3.configure(bg="green")
        button6.configure(bg="green")
        button9.configure(bg="green")
        n = float(playerX.get())
        score = n + 1
        playerX.set(score)
        tkinter.messagebox.showinfo("Winner X!", "You have just won a game!")

    # For O=======================================
    if button1["text"] == "O" and\
            button2["text"] == "O" and\
            button3["text"] == "O":

        button1.configure(bg="green")
        button2.configure(bg="green")
        button3.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button4["text"] == "O" and\
            button5["text"] == "O" and\
            button6["text"] == "O":

        button4.configure(bg="green")
        button5.configure(bg="green")
        button6.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button7["text"] == "O" and\
            button8["text"] == "O" and\
            button9["text"] == "O":

        button7.configure(bg="green")
        button8.configure(bg="green")
        button9.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button3["text"] == "O" and\
            button5["text"] == "O" and\
            button7["text"] == "O":

        button3.configure(bg="green")
        button5.configure(bg="green")
        button7.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button1["text"] == "O" and\
            button5["text"] == "O" and\
            button9["text"] == "O":

        button1.configure(bg="green")
        button5.configure(bg="green")
        button9.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button1["text"] == "O" and\
            button4["text"] == "O" and\
            button7["text"] == "O":

        button1.configure(bg="green")
        button4.configure(bg="green")
        button7.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button2["text"] == "O" and\
            button5["text"] == "O" and\
            button8["text"] == "O":

        button2.configure(bg="green")
        button5.configure(bg="green")
        button8.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")

    if button3["text"] == "O" and\
            button6["text"] == "O" and\
            button9["text"] == "O":

        button3.configure(bg="green")
        button6.configure(bg="green")
        button9.configure(bg="green")
        n = float(playerO.get())
        score = n + 1
        playerO.set(score)
        tkinter.messagebox.showinfo("Winner O!", "You have just won a game!")


lb1PlayerX = Label(RightFrame1, font=("arial", 40, "bold"), text="Player X :",
                   padx=2, pady=2, bg="Cadet Blue")
lb1PlayerX.grid(row=0, column=0,  sticky='W')
txtPlayerX = Entry(RightFrame1, font=("arial", 40, "bold"), bd=2, fg="black",
                   textvariable=playerX, width=14).grid(row=0, column=1)


lb1PlayerO = Label(RightFrame1, font=("arial", 40, "bold"), text="Player O :",
                   padx=2, pady=2, bg="Cadet Blue")
lb1PlayerO.grid(row=1, column=0,  sticky='W')
txtPlayerO = Entry(RightFrame1, font=("arial", 40, "bold"), bd=2, fg="black",
                   textvariable=playerO, width=14).grid(row=1, column=1)


# btnReset
btnReset = Button(RightFrame2, text="Reset", font=("Times 26 bold"),
                  width=38, height=4, bg="gainsboro", command=reset)
btnReset.grid(row=2, column=0, padx=5, pady=5)

# btnNewGame
btnNewGame = Button(RightFrame2, text="New Game", font=("Times 26 bold"),
                    width=38, height=4, bg="gainsboro", command=newGame)
btnNewGame.grid(row=3, column=0, padx=5, pady=5)


# 1
button1 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button1))
button1.grid(row=1, column=0, sticky='S'+'N'+'E'+'W')

# 2
button2 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button2))
button2.grid(row=1, column=1, sticky='S'+'N'+'E'+'W')

# 3
button3 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button3))
button3.grid(row=1, column=2, sticky='S'+'N'+'E'+'W')

# 4
button4 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button4))
button4.grid(row=2, column=0, sticky='S'+'N'+'E'+'W')

# 5
button5 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button5))
button5.grid(row=2, column=1, sticky='S'+'N'+'E'+'W')

# 6
button6 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button6))
button6.grid(row=2, column=2, sticky='S'+'N'+'E'+'W')

# 7
button7 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button7))
button7.grid(row=3, column=0, sticky='S'+'N'+'E'+'W')

# 8
button8 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button8))
button8.grid(row=3, column=1, sticky='S'+'N'+'E'+'W')

# 9
button9 = Button(LeftFrame, text=" ", font=("Times 26 bold"),
                 width=8, height=3, bg="gainsboro",
                 command=lambda: checker(button9))
button9.grid(row=3, column=2, sticky='S'+'N'+'E'+'W')


root.mainloop()
