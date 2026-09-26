import tkinter as tk
from tkinter import messagebox
import random

# THE ENIGMA VAULT
# A small CSP-inspired treasure hunt.
# Run: python main.py

BG = "#120d0a"
PANEL = "#21160f"
GOLD = "#d7a83d"
LIGHT = "#f3dfb1"
MUTED = "#bda77b"
GREEN = "#6fa35a"
RED = "#a94b3f"

LEVELS = [
    {
        "title": "LEVEL 1 • NUMBER PATTERN",
        "text": "Complete the sequence: 2, 4, 8, 16, ?, ?",
        "answer": "32,64",
        "hint": "Each number is multiplied by 2.",
        "solution": "32, 64\n\nEach term doubles the previous one: 2, 4, 8, 16, 32, 64."
    },
    {
        "title": "LEVEL 2 • SYMBOL SEQUENCE",
        "text": "Find the next two symbols: ▲ ● ▲ ● ▲ ? ?",
        "answer": "circle,triangle",
        "hint": "The two symbols alternate.",
        "solution": "circle, triangle\n\nThe pattern alternates triangle, circle, triangle, circle... so after the fifth symbol (triangle) comes circle, then triangle."
    },
    {
        "title": "LEVEL 3 • COLOR ARRANGEMENT",
        "text": "Arrange RED, BLUE, GREEN, YELLOW.\nRED is not 1; GREEN is before BLUE; YELLOW is next to RED; BLUE is not 4.",
        "answer": ["green,blue,red,yellow", "green,blue,yellow,red"],
        "hint": "Try placing RED beside YELLOW first.",
        "solution": "There are two valid arrangements:\n\n1. GREEN, BLUE, RED, YELLOW\n- RED is not 1 -> RED is 3. OK\n- GREEN is before BLUE -> GREEN(1) < BLUE(2). OK\n- YELLOW is next to RED -> RED(3) and YELLOW(4) are adjacent. OK\n- BLUE is not 4 -> BLUE is 2. OK\n\n2. GREEN, BLUE, YELLOW, RED\n- RED is not 1 -> RED is 4. OK\n- GREEN is before BLUE -> GREEN(1) < BLUE(2). OK\n- YELLOW is next to RED -> YELLOW(3) and RED(4) are adjacent. OK\n- BLUE is not 4 -> BLUE is 2. OK"
    },
    {
        "title": "LEVEL 4 • LOGIC LOCK",
        "text": "Three keys A, B, C have values 1, 2, 3.\nA is not 1. B is greater than A. C is not 3.\nEnter the order from smallest to largest.",
        "answer": "c,a,b",
        "hint": "C cannot be 3, and A cannot be 1.",
        "solution": "C, A, B (smallest to largest)\n\nA is not 1, and C is not 3, so testing values: C=1, A=2, B=3 satisfies A is not 1, B > A (3>2), and C is not 3. Order smallest to largest: C, A, B."
    },
    {
        "title": "LEVEL 5 • MAGIC GRID",
        "text": "Use numbers 1–9 once each. Every row, column and diagonal must total 15.\nEnter the middle row.",
        "answer": ["3,5,7", "7,5,3", "1,5,9",  "9,5,1"],
        "hint": "A classic 3×3 magic square has 5 in the center.",
         "solution": "There are 4 possible middle rows:\n\n3, 5, 7   |   7, 5, 3   |   1, 5, 9   |   9, 5, 1\n\nValid magic squares:\n\n4 9 2       2 7 6       8 1 6       6 7 2\n3 5 7       9 5 1       3 5 7       1 5 9\n8 1 6       4 3 8       4 9 2       8 3 4\n\nEach square uses numbers 1–9 exactly once, and every row, column and diagonal totals 15."
},
    {
        "title": "LEVEL 6 • DEDUCTION",
        "text": "Four rooms A-D contain one key each. Gold is not A. Silver is after Gold. Bronze is before Silver. Diamond is in D.\nWhich room contains Gold?",
        "answer": "b",
        "hint": "Diamond occupies D, so reason about the remaining order.",
        "solution": "B\n\nDiamond is in D. Among A, B, C we place Gold, Silver, Bronze. Bronze is before Silver, and Silver is after Gold, so the order is Bronze, Gold, Silver or Gold could come before Bronze too -- testing: Gold is not A, so Gold is B or C. Bronze before Silver, Silver after Gold. The consistent assignment is A=Bronze, B=Gold, C=Silver, D=Diamond. So Gold is in room B."
    },
    {
        "title": "LEVEL 7 • CIPHER CODE",
        "text": "Decode: △ = A, ○ = B, ★ = C, □ = D, ◇ = E.\nSequence: △ ○ ★ △",
        "answer": "A,B,C,A",
        "hint": "Replace each symbol using the given mapping.",
        "solution": "A,B,C,A\n\nUsing the mapping △=A, ○=B, ★=C, □=D, ◇=E:\n△ ○ ★ △  →  A B C A"
    },
    {
        "title": "LEVEL 8 • FINAL VAULT",
        "text": "Final combination: What is the next number?\n3, 6, 12, 24, ?",
        "answer": "48",
        "hint": "The pattern doubles each time.",
        "solution": "48\n\nEach number doubles the previous one: 3, 6, 12, 24, 48."
    },
]

class Game:
    def __init__(self, root):
        self.root = root
        self.root.title("The Enigma Vault — CSP Treasure Hunt")
        self.root.geometry("1050x700")
        self.root.minsize(900, 600)
        self.level = 0
        self.solved = [False] * len(LEVELS)
        self.hints = 3
        self.score = 0
        self.build_bg()
        self.show_home()

    def clear(self):
        for w in self.root.winfo_children():
            w.destroy()

    def build_bg(self):
        self.root.configure(bg=BG)

    def label(self, parent, text, size=18, color=LIGHT, bold=False):
        return tk.Label(parent, text=text, bg=parent.cget("bg"),
                        fg=color, font=("Georgia", size, "bold" if bold else "normal"),
                        wraplength=800, justify="center")

    def button(self, parent, text, command, width=18):
        return tk.Button(parent, text=text, command=command, width=width,
                         bg="#8d5b21", fg="#fff3cf", activebackground="#c18a32",
                         activeforeground="white", relief="raised", bd=2,
                         font=("Georgia", 12, "bold"), cursor="hand2")

    def show_home(self):
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both")
        self.label(frame, "✦  THE ENIGMA VAULT  ✦", 34, GOLD, True).pack(pady=(70,10))
        self.label(frame, "A CSP TREASURE HUNT", 16, MUTED, True).pack(pady=4)
        self.label(frame, "Eight locked doors. Eight puzzles. One hidden treasure.", 17).pack(pady=30)

        treasure = tk.Label(frame, text="💎  🗝️  🏆  💰", bg=BG, fg=GOLD, font=("Segoe UI Emoji", 46))
        treasure.pack(pady=25)

        self.button(frame, "START GAME", self.show_map, 24).pack(pady=10)
        self.button(frame, "HOW TO PLAY", self.instructions, 24).pack(pady=5)
        self.label(frame, "Tip: every puzzle is a constraint satisfaction challenge.", 11, MUTED).pack(side="bottom", pady=25)

    def instructions(self):
        messagebox.showinfo("How to Play",
            "Solve each puzzle to unlock its door.\n\n"
            "Each level is represented as a small constraint satisfaction problem: "
            "find an answer that satisfies all the clues.\n\n"
            "You have 3 hints. Wrong answers do not end the game.")

    def show_map(self):
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=35, pady=25)
        self.label(frame, "YOUR JOURNEY", 30, GOLD, True).pack()
        self.label(frame, f"{sum(self.solved)} / 8 DOORS UNLOCKED   •   SCORE {self.score}", 13, MUTED).pack(pady=5)

        grid = tk.Frame(frame, bg=BG)
        grid.pack(expand=True, pady=25)

        for i in range(8):
            unlocked = i == 0 or self.solved[i-1]
            solved = self.solved[i]
            txt = f"🚪 {i+1}\n{LEVELS[i]['title'].split('•')[-1].strip()}\n" + ("✓ UNLOCKED" if solved else ("🔓 READY" if unlocked else "🔒 LOCKED"))
            b = self.button(grid, txt, lambda i=i: self.play(i), 22)
            b.grid(row=i//4, column=i%4, padx=10, pady=15, ipady=15)
            if not unlocked:
                b.config(state="disabled", bg="#332820")

        self.button(frame, "BACK TO TITLE", self.show_home, 18).pack(pady=10)

    def play(self, i):
        if i > 0 and not self.solved[i-1]:
            return
        self.level = i
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both", padx=70, pady=35)

        self.label(frame, LEVELS[i]["title"], 25, GOLD, True).pack(pady=10)
        self.label(frame, LEVELS[i]["text"], 17, LIGHT, True).pack(pady=35)

        entry = tk.Entry(frame, width=45, font=("Georgia", 15), justify="center",
                         bg="#f6ead0", fg="#24170f", relief="sunken", bd=3)
        entry.pack(pady=10)
        entry.focus()

        self.label(frame, "Enter your answer. For multiple values, use commas", 11, MUTED).pack(pady=5)
        status = self.label(frame, "", 14, LIGHT)
        status.pack(pady=15)

        controls = tk.Frame(frame, bg=BG)
        controls.pack(pady=10)

        def submit():
            raw = entry.get().strip().lower().replace(" ", "")
            ans = LEVELS[i]["answer"]
            # answer can be a single string, or a list of acceptable strings
            # (some levels have more than one valid solution)
            if isinstance(ans, list):
                accepted = [a.replace(" ", "").lower() for a in ans]
            else:
                accepted = [ans.replace(" ", "").lower()]

            if raw in accepted:
                self.solved[i] = True
                self.score += 100 + (20 if self.hints == 3 else 0)
                status.config(text="✓ CONSTRAINTS SATISFIED — DOOR UNLOCKED!", fg=GREEN)
                messagebox.showinfo("Door Unlocked!", "The ancient lock clicks open.\n\nYou found a clue for the next chamber!")
                if i == len(LEVELS)-1:
                    self.treasure()
                else:
                    self.show_map()
            else:
                status.config(text="✗ The constraints are not satisfied. Try again.", fg=RED)

        self.button(controls, "UNLOCK DOOR", submit, 18).grid(row=0, column=0, padx=8)
        self.button(controls, "HINT", lambda: self.give_hint(status), 12).grid(row=0, column=1, padx=8)
        self.button(controls, "SEE SOLUTION", lambda: self.show_solution(i), 14).grid(row=0, column=2, padx=8)
        self.button(controls, "MAP", self.show_map, 12).grid(row=0, column=3, padx=8)

    def show_solution(self, i):
        answer = messagebox.askyesno(
            "Reveal Solution?",
            "Are you sure you want to see the full solution?\n"
            "This will not count against your hints, but it does take away the fun of solving it yourself."
        )
        if not answer:
            return
        sol = LEVELS[i].get("solution", "No solution text available for this level.")
        messagebox.showinfo(f"Solution — {LEVELS[i]['title']}", sol)

    def give_hint(self, status):
        if self.hints <= 0:
            status.config(text="No hints remaining.", fg=RED)
            return
        self.hints -= 1
        status.config(text=f"💡 Hint: {LEVELS[self.level]['hint']}   ({self.hints} left)", fg=GOLD)

    def treasure(self):
        self.clear()
        frame = tk.Frame(self.root, bg=BG)
        frame.pack(expand=True, fill="both")
        self.label(frame, "✦  CONGRATULATIONS!  ✦", 32, GOLD, True).pack(pady=(70,10))
        self.label(frame, "ALL 8 DOORS UNLOCKED", 18, LIGHT, True).pack()
        self.label(frame, "💎   🏆   💰   👑   💎", 52, GOLD).pack(pady=35)
        self.label(frame, "YOU FOUND THE LOST TREASURE!", 24, GOLD, True).pack()
        self.label(frame, f"Final Score: {self.score}", 16, LIGHT).pack(pady=15)
        self.label(frame, "Your logic and patience opened the Enigma Vault.", 14, MUTED).pack(pady=10)
        self.button(frame, "PLAY AGAIN", self.restart, 18).pack(pady=25)
        self.button(frame, "EXIT", self.root.destroy, 18).pack()

    def restart(self):
        self.level = 0
        self.solved = [False] * 8
        self.hints = 3
        self.score = 0
        self.show_home()

if __name__ == "__main__":
    root = tk.Tk()
    Game(root)
    root.mainloop()