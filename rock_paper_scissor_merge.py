import tkinter as tk
from rock_paper_scissor_backened import get_computer_choice, get_winner
from game_db import save_result  # Import at the top

# Main game window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("800x600")  # Optional: Set a standard window size

# Function to play a round
def play(choice):
    computer_choice = get_computer_choice()
    result = get_winner(choice, computer_choice)
    result_text = f"You chose: {choice}\nComputer chose: {computer_choice}\n\n{result}"
    
    # Save the result to the database
    save_result("Rock Paper Scissors", result)

    # Clear old content and insert new result
    result_display.config(state="normal")
    result_display.delete("1.0", tk.END)
    result_display.insert(tk.END, result_text)
    result_display.config(state="disabled")

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_button = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_button.grid(row=0, column=2, padx=5)

# Scrollable Text widget for result display
result_frame = tk.Frame(root)
result_frame.pack(fill="both", expand=True, padx=20, pady=10)

scrollbar = tk.Scrollbar(result_frame)
scrollbar.pack(side="right", fill="y")

result_display = tk.Text(
    result_frame,
    wrap="word",
    font=("Arial", 14),
    yscrollcommand=scrollbar.set
)
result_display.pack(fill="both", expand=True)
scrollbar.config(command=result_display.yview)

# Insert default message
result_display.insert(tk.END, "Choose Rock, Paper, or Scissors to start.")
result_display.config(state="disabled")

# Run the GUI loop
root.mainloop()
