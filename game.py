from tkinter import *
from tkinter import messagebox

# Create main window
window = Tk()
window.title("Tic Tac Toe")
window.geometry("600x600")
window.resizable(True, True)

# Create GUI elements
frame = Frame(window, bg="#2A2E32")
frame.pack(fill=BOTH, expand=True)

button_list = []
player = "X"

# Define function to check for a win
def check_win():
    # Check rows for win
    for row in button_list:
        if row[0]["text"] == row[1]["text"] == row[2]["text"] != "":
            return True
    # Check columns for win
    for i in range(3):
        if button_list[0][i]["text"] == button_list[1][i]["text"] == button_list[2][i]["text"] != "":
            return True
    # Check diagonals for win
    if button_list[0][0]["text"] == button_list[1][1]["text"] == button_list[2][2]["text"] != "":
        return True
    if button_list[0][2]["text"] == button_list[1][1]["text"] == button_list[2][0]["text"] != "":
        return True
    return False

# Define function to handle button clicks
def click_handler(button):
    global player
    if button["text"] == "":
        button["text"] = player
        if check_win():
            messagebox.showinfo("Game Over", "Player {} wins!".format(player))
            window.update()
            if messagebox.askyesno("Game Over", "Do you want to play again?"):
                reset_game()
            else:
                window.destroy()
        elif all(button["text"] != "" for row in button_list for button in row):
            messagebox.showinfo("Game Over", "It's a tie!")
            window.update()
            if messagebox.askyesno("Game Over", "Do you want to play again?"):
                reset_game()
            else:
                window.destroy()
        else:
            player = "O" if player == "X" else "X"

# Define function to reset the game
def reset_game():
    global player
    player = "X"
    for row in button_list:
        for button in row:
            button["text"] = ""

# Create the buttons
for i in range(3):
    button_row = []
    for j in range(3):
        button = Button(frame, bg="#3E4347", fg="white", width=10, height=5, font=("Arial", 24, "bold"))
        button.grid(row=i, column=j, padx=10, pady=10, sticky=NSEW)
        button_row.append(button)
        
        # Make buttons resizable
        frame.grid_rowconfigure(i, weight=1)
        frame.grid_columnconfigure(j, weight=1)
        button.grid(sticky=NSEW)
        
        # Bind the button to the click handler
        button.config(command=lambda button=button: click_handler(button))
        
    button_list.append(button_row)

# Run the main event loop
window.mainloop()
