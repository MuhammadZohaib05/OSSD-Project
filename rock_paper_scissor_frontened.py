# rps_gui.py

import tkinter as tk
from  rock_paper_scissor_backened import get_computer_choice, get_winner

# Main game window
root = tk.Tk()
root.title("Rock Paper Scissors")

# Result label
result_label = tk.Label(root, text="Choose Rock, Paper, or Scissors", font=("Arial", 14))
result_label.pack(pady=20)

# Function to play a round
def play(choice):
    computer_choice = get_computer_choice()
    result = get_winner(choice, computer_choice)
    result_text = f"You chose: {choice}\nComputer chose: {computer_choice}\n\n{result}"
    result_label.config(text=result_text)

# Buttons for choices
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Run the GUI loop
root.mainloop()