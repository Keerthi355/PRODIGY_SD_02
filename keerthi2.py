import tkinter as tk
from tkinter import messagebox
import random

class GuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number Game")
        
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        
        self.label = tk.Label(master, text="Guess the number between 1 and 100:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.result_label = tk.Label(master, text="")
        self.result_label.pack()
        
        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack()
        
        self.reset_button = tk.Button(master, text="Play Again", command=self.reset_game)
        self.reset_button.pack()
        
    def check_guess(self):
        guess = self.entry.get()
        self.attempts += 1
        
        try:
            guess = int(guess)
            if guess == self.secret_number:
                messagebox.showinfo("Correct!", f"Congratulations! You guessed the number {self.secret_number} in {self.attempts} attempts.")
                self.reset_game()
            elif guess < self.secret_number:
                self.result_label.config(text="Too low! Try again.")
            else:
                self.result_label.config(text="Too high! Try again.")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid integer.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
game = GuessingGame(root)
root.mainloop()
