import tkinter as tk
import time
import random

sentences = [
    "Python makes coding fun and powerful.",
    "The quick brown fox jumps over the lazy dog.",
    "Typing fast is a skill that improves with practice.",
    "GitHub is a great place to share projects.",
    "Never stop learning new things every day.",
    "Artificial intelligence is shaping the future of technology."
]

class TypingSpeedRace:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Race 🏎️")
        self.root.configure(bg="#1e1e2f")

        self.text_to_type = random.choice(sentences)
        self.start_time = None

        self.title = tk.Label(root, text="🔥 Typing Speed Race 🔥", font=("Arial", 22, "bold"), fg="white", bg="#1e1e2f")
        self.title.pack(pady=10)

        self.label_sentence = tk.Label(root, text=self.text_to_type, font=("Arial", 16), fg="yellow", wraplength=750, bg="#1e1e2f")
        self.label_sentence.pack(pady=20)

        self.entry = tk.Entry(root, width=80, font=("Arial", 14))
        self.entry.pack(pady=15)
        self.entry.bind("<FocusIn>", self.start_timer)
        self.entry.bind("<KeyRelease>", self.update_progress)
        self.entry.bind("<Return>", self.check_result)

        self.canvas = tk.Canvas(root, width=700, height=100, bg="#333333", highlightthickness=0)
        self.canvas.pack(pady=30)

        self.canvas.create_rectangle(50, 40, 650, 60, fill="gray", outline="white")

        self.car = self.canvas.create_text(50, 50, text="🚗", font=("Arial", 20))
        
        self.result_label = tk.Label(root, text="", font=("Arial", 14), fg="white", bg="#1e1e2f")
        self.result_label.pack(pady=20)

        self.restart_button = tk.Button(root, text="Play Again", font=("Arial", 12, "bold"), bg="green", fg="white", command=self.restart)
        self.restart_button.pack(pady=10)

    def start_timer(self, event):
        if not self.start_time:
            self.start_time = time.time()

    def update_progress(self, event):
        typed_text = self.entry.get()

        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.text_to_type) and c == self.text_to_type[i])
        progress = correct_chars / len(self.text_to_type)

        new_x = 50 + int(progress * 600)
        self.canvas.coords(self.car, new_x, 50)

    def check_result(self, event):
        end_time = time.time()
        typed_text = self.entry.get()

        time_taken = round(end_time - self.start_time, 2)
        words = len(self.text_to_type.split())
        wpm = round((words / time_taken) * 60)

        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.text_to_type) and c == self.text_to_type[i])
        accuracy = round((correct_chars / len(self.text_to_type)) * 100)

        self.result_label.config(
            text=f"⏱ Time: {time_taken}s   ⚡ Speed: {wpm} WPM   🎯 Accuracy: {accuracy}%"
        )

    def restart(self):
        self.text_to_type = random.choice(sentences)
        self.label_sentence.config(text=self.text_to_type)
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.canvas.coords(self.car, 50, 50)


if __name__ == "__main__":
    root = tk.Tk()
    game = TypingSpeedRace(root)
    root.mainloop()