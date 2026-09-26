# 🔐 The Enigma Vault

**A CSP-themed treasure hunt puzzle game built with Python & Tkinter.**

Solve eight constraint-satisfaction puzzles — number patterns, ciphers, logic locks, magic squares, and more — to unlock doors one by one and claim the hidden treasure. Compete for the top spot on the local leaderboard.

![Python](https://img.shields.io/badge/python-3.x-blue)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/license-MIT-green)
![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey)

---

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation & Running](#installation--running)
- [How to Play](#how-to-play)
- [Scoring](#scoring)
- [Leaderboard](#leaderboard)
- [Levels](#levels)
- [Project Structure](#project-structure)
- [Notes](#notes)
- [License](#license)

---

## Features

- 🧩 **8 handcrafted puzzles** — each modeled as a small constraint satisfaction problem
- 🗺️ **Progressive door unlocking** — solve one puzzle to reveal the next
- 💡 **Limited hint system** — 3 hints per playthrough, with a scoring bonus for not using them
- 📜 **Full solution reveal** — for when you're truly stuck (with a spoiler confirmation)
- 🏆 **Local leaderboard** — top 10 scores saved automatically between sessions
- 🎨 **Themed UI** — a warm, vault/treasure-hunt aesthetic entirely in Tkinter, no external assets

## Requirements

- Python 3.x
- Tkinter (bundled with most standard Python installations)

No external/pip packages are required.

## Installation & Running

```bash
git clone https://github.com/<your-username>/enigma-vault.git
cd enigma-vault
python main.py
```

On some systems you may need `python3` instead of `python`:

```bash
python3 main.py
```

## How to Play

1. From the title screen, click **START GAME**.
2. Doors unlock in order — solve Level 1 to reveal Level 2, and so on.
3. Read the puzzle and type your answer into the input box.
   - For multi-part answers, separate values with commas (e.g. `32,64`).
   - Answers are case-insensitive and ignore extra spacing.
4. Click **UNLOCK DOOR** to submit.
5. Stuck? Use:
   - **HINT** — reveals a clue (3 available per game)
   - **SEE SOLUTION** — reveals the full worked answer (asks for confirmation first, since it spoils the puzzle)
6. Click **MAP** anytime to return to the level overview.
7. Unlock all 8 doors to reach the treasure screen, see your final score, and submit it to the leaderboard.

## Scoring

| Action                          | Points |
|----------------------------------|--------|
| Solve a level                    | +100   |
| Solve a level with all 3 hints unused | +20 bonus |

## Leaderboard

- Scores are saved locally to `leaderboard.json`, created automatically the first time you finish the game.
- After unlocking all 8 doors, you'll be prompted for a name; your score is saved immediately (leave it blank or cancel to skip).
- View standings anytime via the **LEADERBOARD** button on the title screen or the treasure screen.
- Keeps the **top 10 scores**, ranked highest to lowest, with 🥇🥈🥉 for the top 3.
- The leaderboard is local to your machine only — it isn't synced or shared online. Delete `leaderboard.json` to reset it.

## Levels

| # | Level Name          | Puzzle Type                  |
|---|----------------------|-------------------------------|
| 1 | Number Pattern        | Sequence completion            |
| 2 | Symbol Sequence        | Pattern recognition             |
| 3 | Color Arrangement      | Constraint satisfaction (multiple valid solutions) |
| 4 | Logic Lock             | Deductive ordering               |
| 5 | Magic Grid              | Magic square (multiple valid solutions) |
| 6 | Deduction                | Logical elimination                |
| 7 | Cipher Code               | Symbol decoding                     |
| 8 | Final Vault                | Sequence completion (finale)          |

## Project Structure

```
enigma-vault/
├── main.py            # entire game: puzzle data, UI, and game logic
├── leaderboard.json    # auto-created on first finished game (stores top scores)
└── README.md            # you are here
```

## Notes

- In-game progress (solved levels, current score, hints) resets on restart or **PLAY AGAIN** — only the leaderboard persists between sessions.
- Minimum window size: 900×600 (resizable).

## License

MIT — feel free to fork, modify, and build on this project.
