# chatgpt_prompts.py

import asyncio
import tkinter as tk
from tkinter import ttk, messagebox
from your_module import (
    diyExpert, socialMediaInfluencer, socrat, socraticMethod, virtualDoctor,
    personalChef, legalAdvisor, personalStylist, itExpert, chessPlayer,
    midjourneyPromptGenerator, ticTacToeGame, passwordGenerator,
    newLanguageCreator, mathematicalHistoryTeacher, songRecommender,
    coverLetter, technologyTransferer, unconstrainedAiModelDan, gomokuPlayer,
    proofreader
)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Function Runner")

        self.functions = {
            "DIY Expert": diyExpert,
            "Social Media Influencer": socialMediaInfluencer,
            "Socrat": socrat,
            "Socratic Method": socraticMethod,
            "Virtual Doctor": virtualDoctor,
            "Personal Chef": personalChef,
            "Legal Advisor": legalAdvisor,
            "Personal Stylist": personalStylist,
            "IT Expert": itExpert,
            "Chess Player": chessPlayer,
            "Midjourney Prompt Generator": midjourneyPromptGenerator,
            "Tic Tac Toe Game": ticTacToeGame,
            "Password Generator": passwordGenerator,
            "New Language Creator": newLanguageCreator,
            "Mathematical History Teacher": mathematicalHistoryTeacher,
            "Song Recommender": songRecommender,
            "Cover Letter": coverLetter,
            "Technology Transferer": technologyTransferer,
            "Unconstrained AI Model Dan": unconstrainedAiModelDan,
            "Gomoku Player": gomokuPlayer,
            "Proofreader": proofreader
        }

        self.create_widgets()

    def create_widgets(self):
        self.label = ttk.Label(self.root, text="Choose a function:")
        self.label.pack(pady=10)

        self.combo = ttk.Combobox(self.root, values=list(self.functions.keys()))
        self.combo.pack(pady=10)

        self.message_label = ttk.Label(self.root, text="Enter your message:")
        self.message_label.pack(pady=10)

        self.message_entry = ttk.Entry(self.root, width=50)
        self.message_entry.pack(pady=10)

        self.run_button = ttk.Button(self.root, text="Run", command=self.run_function)
        self.run_button.pack(pady=20)

    def run_function(self):
        choice = self.combo.get()
        message = self.message_entry.get()

        if choice and message:
            async def run_async_function():
                instance = None  # Replace with actual instance if needed
                result = await self.functions[choice](instance).async_method(message)
                messagebox.showinfo("Result", f"Result: {result}")

            asyncio.run(run_async_function())
        else:
            messagebox.showwarning("Input Error", "Please select a function and enter a message.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
