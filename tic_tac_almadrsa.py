import tkinter as tk
from tkinter import *
import random

window = Tk()
window.title('Tic Tac Toe Almadrsa')

buttons = []
x_score = 0
o_score = 0
count = 0



#create board
frame2 = tk.Frame(window)
frame2.grid(row=1,column=0,sticky="n")
for i in range (3):
    row = []
    for j in range(3):
        button = Button(frame2, text="", height=10, width=20, bd=1, relief="solid",font=("Arial", 12,"bold"),command=lambda r=i,w=j:moves(r,w))
        button.grid(row=i , column = j,sticky="nsew")
        row.append(button)
    buttons.append(row)

def moves(row, col):
    global x_score,o_score
    global clicked,count
    if buttons[row][col]["text"] == "" :
        buttons[row][col]["text"] = "x"
        
        computer_move()
        count +=1
        #print(count)

    if check_win ("x"):
        winner_label.config(text="X wins")
        x_score += 1
        score_label.config(text=f"you: {x_score} pc: {o_score}")
        disable_butt()
    
    elif check_win ("o"):
        winner_label.config(text="O wins")
        o_score += 1
        score_label.config(text=f"you: {x_score} pc: {o_score}")
        disable_butt()
    
    elif count == 9:
        winner_label.config(text="'Tie' no winner")
        for row in buttons:
            for button in row:
                button.config(bg="red")
        
        disable_butt()





def disable_butt():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)




def check_win(player):
    
    

    for i in range(3):

        if  buttons[i][0]["text"] == player and buttons[i][1]["text"] == player and buttons[i][2]["text"] == player:
            buttons[i][0].config(bg="cyan")
            buttons[i][1].config(bg="cyan")
            buttons[i][2].config(bg="cyan")
            return True
    
        if  buttons[0][i]["text"] == player and buttons[1][i]["text"] == player and buttons[2][i]["text"] == player:
            buttons[0][i].config(bg="cyan")
            buttons[1][i].config(bg="cyan")
            buttons[2][i].config(bg="cyan")
            return True
            
    if buttons[0][0]["text"] == player and buttons[1][1]["text"] == player and buttons[2][2]["text"]== player:
        buttons[0][0].config(bg="cyan")
        buttons[1][1].config(bg="cyan")
        buttons[2][2].config(bg="cyan")
        return True 
    if buttons[0][2]["text"] ==player and buttons[1][1]["text"] == player and buttons[2][0]["text"] == player:
       
        buttons[0][2].config(bg="cyan")
        buttons[1][1].config(bg="cyan")
        buttons[2][0].config(bg="cyan")
        return True     







def computer_move():
    global count
    pc_moves = []
   
    for i in range(3):
        for j in range(3):
            if buttons[i][j]["text"] == "":
                pc_moves.append((i, j))
    if pc_moves:
        r,c = random.choice(pc_moves)
        buttons[r][c]["text"] = "o"
        count +=1
 
    
def reset_game():
    global clicked,count
    count = 0
    clicked = True
    winner_label.config(text=" i hope you win ")



    # Clear the board
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="",state=NORMAL,bg="SystemButtonFace")




#creat widgets
frame = tk.Frame(window,height=40, width=40)
winner_label = tk.Label(frame,text=" i hope you win, you 'x',pc 'o' ",height=1, width=25,font=("arial",20),bd=2,relief="sunken")
score_label = tk.Label(frame,text="welcom to 'X' 'O' game",height=1, width=20,font=("arial",20),bd=2,relief="sunken",anchor="center")
restart_button = tk.Button(frame, text="Restart",height=1,width=10,bd=1,font=("arial",15),relief="solid" ,command=reset_game)


frame.grid(row=0,column=0,sticky="n")
score_label.grid(row=0,column=1,padx=3,pady=3,sticky="n")
winner_label.grid(row=1,column=1,padx=3,pady=3,sticky="n")
restart_button.grid(row=2,column=1,padx=3,pady=3,sticky="n")


window.mainloop()