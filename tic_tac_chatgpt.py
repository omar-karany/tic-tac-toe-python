import tkinter as tk
from tkinter import *
import random

def create_board():
    frame2 = tk.Frame(window)
    frame2.grid(row=1, column=0, sticky="n")
    buttons = []
    for i in range(3):
        row = []
        for j in range(3):
            button = Button(frame2, text="", height=10, width=20, bd=1, relief="solid", font=("Arial", 12, "bold"),
                            command=lambda r=i, w=j: moves(r, w))
            button.grid(row=i, column=j, sticky="nsew")
            row.append(button)
        buttons.append(row)
    return buttons

def moves(row, col):
    global count
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = "X"
        count += 1
        if check_win("X"):
            end_game("X wins")
        elif count < 9:
            computer_move()

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

def check_win(player):
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] == player:
            highlight_winner([buttons[i][0], buttons[i][1], buttons[i][2]])
            return True

        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] == player:
            highlight_winner([buttons[0][i], buttons[1][i], buttons[2][i]])
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] == player:
        highlight_winner([buttons[0][0], buttons[1][1], buttons[2][2]])
        return True

    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] == player:
        highlight_winner([buttons[0][2], buttons[1][1], buttons[2][0]])
        return True

    return False

def highlight_winner(cells):
    for cell in cells:
        cell.config(bg="cyan")

def computer_move():
    global count

    # Check for winning move for the computer
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                buttons[i][j]["text"] = "O"
                if check_win("O"):
                    count += 1
                    end_game("O wins")
                    return
                buttons[i][j]["text"] = ""

    # If no winning moves, make a random move
    pc_moves = [(i, j) for i in range(3) for j in range(3) if buttons[i][j]["text"] == ""]
    if pc_moves:
        r, c = random.choice(pc_moves)
        buttons[r][c]["text"] = "O"
        count += 1

    if count == 9:
        end_game("Tie - No winner")

def end_game(message):
    global x_score, o_score
    winner_label.config(text=message)
    if message == "X wins":
        x_score += 1
    elif message == "O wins":
        o_score += 1
    score_label.config(text=f"You: {x_score} PC: {o_score}")
    disable_buttons()

def reset_game():
    global count
    count = 0
    winner_label.config(text="I hope you win")

    # Clear the board
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=NORMAL, bg="SystemButtonFace")

window = Tk()
window.title('Tic Tac Toe Almadrsa')

buttons = create_board()
x_score = 0
o_score = 0
count = 0

frame = tk.Frame(window, height=40, width=40)
winner_label = tk.Label(frame, text="I hope you win, you 'X', PC 'O'", height=1, width=25, font=("Arial", 20), bd=2,
                        relief="sunken")
score_label = tk.Label(frame, text="Welcome to 'X' 'O' game", height=1, width=20, font=("Arial", 20), bd=2,
                       relief="sunken", anchor="center")
restart_button = tk.Button(frame, text="Restart", height=1, width=10, bd=1, font=("Arial", 15), relief="solid",
                           command=reset_game)

frame.grid(row=0, column=0, sticky="n")
score_label.grid(row=0, column=1, padx=3, pady=3, sticky="n")
winner_label.grid(row=1, column=1, padx=3, pady=3, sticky="n")
restart_button.grid(row=2, column=1, padx=3, pady=3, sticky="n")

window.mainloop()