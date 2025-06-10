import tkinter as tk
from tkinter import messagebox


root = tk.Tk()
root.title("Tic-Tac-Toe")

current_player = "X"
winner = False


label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 15))
label.grid(row=0, column=0, columnspan=3)


buttons = []

def check_winner():
    global winner
    winning_combos = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    for combo in winning_combos:
        if (buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != ""):
            winner = True
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            root.quit()
            return
    # Check for tie
    if all(button["text"] != "" for button in buttons) and not winner:
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        root.quit()

def button_click(index):
    global current_player
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "O" if current_player == "X" else "X"
    label.config(text=f"Player {current_player}'s turn")

# Create 3x3 grid of buttons
for i in range(9):
    button = tk.Button(root, text="", font=("normal", 25), width=6, height=2,
                       command=lambda i=i: button_click(i))
    button.grid(row=(i//3)+1, column=i%3)
    buttons.append(button)

root.mainloop()
