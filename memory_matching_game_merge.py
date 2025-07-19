import tkinter as tk
from tkinter import messagebox
import random

# ✅ BACKEND
class MemoryGameBackend:
    def __init__(self):
        self.symbols = []
        self.moves = 0
        self.first_click = None
        self.second_click = None
        self.prepare_game()

    def prepare_game(self):
        pairs = ['🍎', '🍌', '🍒', '🍇', '🍋', '🥝', '🍍', '🍉']
        self.symbols = pairs * 2
        random.shuffle(self.symbols)
        self.moves = 0
        self.first_click = None
        self.second_click = None

    def check_match(self, idx1, idx2):
        return self.symbols[idx1] == self.symbols[idx2]

    def increase_moves(self):
        self.moves += 1
        return self.moves

# ✅ FRONTEND
backend = MemoryGameBackend()

# Color map for emojis
symbol_colors = {
    '🍎': "#D32F2F",
    '🍌': "#FBC02D",
    '🍒': "#C2185B",
    '🍇': "#7B1FA2",
    '🍋': "#FDD835",
    '🥝': "#388E3C",
    '🍍': "#FFA000",
    '🍉': "#43A047"
}

# Main window
memory_game = tk.Tk()
memory_game.title("Memory Matching Game")
memory_game.configure(bg="#4CAF50")  # ✅ Better green background
memory_game.attributes("-fullscreen", True)

buttons = {}

# ✅ FUNCTIONS
def button_click(x, y):
    index = (x * 4) + y
    button = buttons[(x, y)]

    if button["text"] == " " and backend.second_click is None:
        symbol = backend.symbols[index]
        button.config(text=symbol, fg=symbol_colors[symbol])

        if backend.first_click is None:
            backend.first_click = (x, y)
        else:
            backend.second_click = (x, y)
            backend.increase_moves()
            move_label.config(text=f"Moves: {backend.moves}")
            memory_game.after(500, check_match)

def check_match():
    b1 = buttons[backend.first_click]
    b2 = buttons[backend.second_click]
    idx1 = (backend.first_click[0] * 4) + backend.first_click[1]
    idx2 = (backend.second_click[0] * 4) + backend.second_click[1]

    if backend.check_match(idx1, idx2):
        b1.config(bg="#C8E6C9", state="disabled")
        b2.config(bg="#C8E6C9", state="disabled")
    else:
        b1.config(text=" ", fg="black")
        b2.config(text=" ", fg="black")

    backend.first_click = None
    backend.second_click = None

    check_win()

def check_win():
    for btn in buttons.values():
        if btn["text"] == " ":
            return
    messagebox.showinfo("Congratulations!", f"You've matched all pairs in {backend.moves} moves!")
    reset_game()

def reset_game():
    backend.prepare_game()
    for (x, y), btn in buttons.items():
        btn.config(text=" ", fg="black", bg="#ECECEC", state="normal")
    move_label.config(text=f"Moves: {backend.moves}")

# ✅ Exit Fullscreen
def exit_fullscreen():
    memory_game.attributes("-fullscreen", False)
    exit_button.pack_forget()

def enter_fullscreen():
    memory_game.attributes("-fullscreen", True)
    exit_button.pack(pady=5)

memory_game.bind("<Escape>", lambda event: exit_fullscreen())
memory_game.bind("<F11>", lambda event: enter_fullscreen())

# ✅ UI LAYOUT

# Header
header = tk.Frame(memory_game, bg="#2E7D32", pady=10)
header.pack(fill="x")
title_label = tk.Label(header, text="🍉 Memory Matching Game 🍍", font=("Arial", 24, "bold"), fg="white", bg="#2E7D32")
title_label.pack()

# Move Counter
move_label = tk.Label(memory_game, text="Moves: 0", font=("Arial", 16), bg="#4CAF50", fg="white")
move_label.pack(pady=10)

# Game Grid
grid_frame = tk.Frame(memory_game, bg="#4CAF50")
grid_frame.pack()

for i in range(4):
    for j in range(4):
        btn = tk.Button(grid_frame, text=" ", font=("Arial", 20), width=6, height=3,
                        bg="#ECECEC", command=lambda x=i, y=j: button_click(x, y))
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[(i, j)] = btn

# Footer
footer = tk.Frame(memory_game, bg="#2E7D32", pady=15)
footer.pack(fill="x", side="bottom")

# Reset Button
reset_button = tk.Button(footer, text="🔁 Reset Game", font=("Arial", 14),
                         bg="#FF7043", fg="white", command=reset_game)
reset_button.pack(side="left", padx=20)

# Exit Fullscreen Button
exit_button = tk.Button(footer, text="⛶ Exit Fullscreen", font=("Arial", 12),
                        bg="#9E9E9E", fg="white", command=exit_fullscreen)
exit_button.pack(side="right", padx=20)

# Run the App
memory_game.mainloop()