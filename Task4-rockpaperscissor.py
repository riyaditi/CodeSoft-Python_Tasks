import tkinter as tk
from tkinter import ttk
import random

class RockPaperScissorsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock, Paper, Scissors")

        self.user_score = 0
        self.computer_score = 0

        self.user_choice_var = tk.StringVar()
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Labels
        ttk.Label(self.root, text="Rock, Paper, Scissors", font=("Helvetica", 20)).pack(pady=10)

        # User's Choice
        ttk.Label(self.root, text="Your Choice:", font=("Helvetica", 12)).pack(pady=5)
        user_combobox = ttk.Combobox(self.root, values=["Rock", "Paper", "Scissors"], textvariable=self.user_choice_var, state="readonly")
        user_combobox.pack(pady=5)
        user_combobox.set("Rock")

        # Play Button
        ttk.Button(self.root, text="Play", command=self.play, style="TButton").pack(pady=10)

        # Computer's Choice
        ttk.Label(self.root, text="Computer's Choice:", font=("Helvetica", 12)).pack(pady=5)
        self.computer_choice_label = ttk.Label(self.root, text="", font=("Helvetica", 12))
        self.computer_choice_label.pack(pady=5)

        # Result
        ttk.Label(self.root, text="Result:", font=("Helvetica", 12)).pack(pady=5)
        ttk.Label(self.root, textvariable=self.result_var, font=("Helvetica", 12)).pack(pady=5)

        # Score
        ttk.Label(self.root, text="Score:", font=("Helvetica", 12)).pack(pady=5)
        ttk.Label(self.root, text=f"You: {self.user_score}   Computer: {self.computer_score}", font=("Helvetica", 12)).pack(pady=5)

        # Play Again Button
        ttk.Button(self.root, text="Play Again", command=self.play_again, style="TButton").pack(pady=10)

    def play(self):
        user_choice = self.user_choice_var.get().lower()
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # Update computer's choice label
        self.computer_choice_label.config(text=computer_choice.capitalize())

        # Determine the winner
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You win!"
            self.user_score += 1
        else:
            result = "You lose!"
            self.computer_score += 1

        # Update result and score labels
        self.result_var.set(result)
        self.update_score_label()

    def update_score_label(self):
        score_text = f"You: {self.user_score}   Computer: {self.computer_score}"
        ttk.Label(self.root, text=score_text, font=("Helvetica", 12)).pack_forget()
        ttk.Label(self.root, text=score_text, font=("Helvetica", 12)).pack(pady=5)

    def play_again(self):
        self.user_choice_var.set("Rock")
        self.result_var.set("")
        self.computer_choice_label.config(text="")
        self.update_score_label()

if __name__ == "__main__":
    root = tk.Tk()

    # Styling
    style = ttk.Style()
    style.configure("TButton", font=("Helvetica", 12), padding=5)

    game = RockPaperScissorsGame(root)

    # Run the Tkinter event loop
    root.mainloop()
