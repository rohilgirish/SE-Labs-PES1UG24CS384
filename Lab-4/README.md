# Scenario 15 — Connect Four vs AI

A terminal Connect Four game with a board module, a player turn loop, and a simple AI.

## Provided files

- `main.py` — entry point.
- `game.py` — turn handling and game flow.
- `board.py` — board state, drops, and win detection.
- `ai.py` — computer move selection.
- `requirements.txt` — dependency declaration.

## Setup

```bash
python main.py
```

## Before changing the code

Play several games, inspect all modules, and construct horizontal, vertical, and
diagonal winning positions. Trace how a move travels from the command line to the
board and then to winner detection.

## Task 1 — Complete win detection

Make win detection recognise every four-in-a-row direction, including both diagonals,
without breaking horizontal and vertical wins.

**Done when:** all four directions are detected and shorter sequences do not count.

## Task 2 — Complete game termination

Handle draws, full columns, invalid moves, and game termination consistently. A
winning move must stop the game before another turn is requested.

**Done when:** no invalid move changes the board and every terminal state is clear.

## Task 3 — Improve the AI

Add meaningful decision-making. The AI should take an immediate winning move when one
exists and block an immediate player win when necessary. Handle full columns safely.

**Done when:** the AI never selects an illegal column and responds correctly to one-move threats.

## Task 4 — Move-level feedback

Add concise feedback for a successful disc placement. It should occur once per actual
move, not once per cell inspected by win detection or AI analysis.

## Required testing

Test horizontal, vertical, both diagonals, draw positions, full columns, invalid input,
immediate AI wins, immediate AI blocks, and quitting.


## LLM usage

You may use an LLM during the lab. The goal is to use it as a coding assistant while
retaining responsibility for understanding and testing the result.

- Inspect the existing code before asking for changes.
- Ask for explanations when you do not understand a proposed change.
- Test generated code against the stated behaviour and edge cases.
- Keep your complete LLM chat history for submission.
- Do not replace the whole project with an unrelated implementation.
- Keep all state in memory; do not add CSV, JSON, SQLite, or other persistence.

## Submission checklist

- [x] Task 1 completed and the original defect was reproduced and fixed.
- [x] Tasks 2–4 completed and tested.
- [x] Boundary and invalid-input cases tested.
- [x] No unnecessary external dependencies added.
- [x] No persistent storage added.
- [x] Code remains understandable and modular.
- [x] Complete LLM chat-history link included: https://claude.ai/share/56914cc2-0791-40fb-b8c1-a1e3acbea036

## Folder structure

```text
Lab-4/
├── README.md
├── requirements.txt
├── main.py
├── game.py
├── board.py
├── ai.py
├── before.mp4
└── after.mp4
```

## Identified Bugs & Original Issues

1. **Incomplete Win Detection (`board.py`):**
   - In `winner(self, token)`, only horizontal `(0, 1)` and vertical `(1, 0)` vectors were checked. Diagonal alignments (`(1, 1)` down-right and `(1, -1)` down-left) were completely omitted, meaning diagonal 4-in-a-row connections failed to trigger game wins.
2. **Improper Game Termination & Input Validation (`game.py`):**
   - Out-of-bounds column numbers (outside 1-7), non-numeric values, or choosing full columns were not handled cleanly, leading to confusing states or improper termination.
3. **Basic AI with No Threat Evaluation (`ai.py`):**
   - The AI picked randomly from legal columns without checking if it had an immediate winning move or if the opponent was one move away from winning (leading to unblocked player wins).
4. **Missing Move-Level Feedback (`game.py`):**
   - There was no status message indicating where the player or AI dropped a disc.

---

## Changes Implemented & Tasks Completed

- **Task 1 — Complete Win Detection ([board.py](file:///C:/Users/Lenovo/Desktop/SE-Labs-PES1UG24CS384/Lab-4/board.py)):**
  - Updated `directions` to `[(0, 1), (1, 0), (1, 1), (1, -1)]` to accurately detect horizontal, vertical, and both diagonal 4-in-a-row sequences without allowing shorter sequences to trigger wins.
- **Task 2 — Complete Game Termination & Validation ([game.py](file:///C:/Users/Lenovo/Desktop/SE-Labs-PES1UG24CS384/Lab-4/game.py)):**
  - Added strict input bounds checking (columns 1–7), handled `KeyboardInterrupt` / `EOFError` / `q` gracefully, prevented moves into full columns with informative messages, and ensured terminal states (wins, draws) halt the turn loop cleanly.
- **Task 3 — Intelligent AI Decision Making ([ai.py](file:///C:/Users/Lenovo/Desktop/SE-Labs-PES1UG24CS384/Lab-4/ai.py)):**
  - Implemented 1-move lookahead: AI checks and executes immediate winning moves, detects and blocks immediate opponent threats, avoids moves that set up an opponent win directly above, and heuristics to prioritize central columns.
- **Task 4 — Move-Level Feedback ([game.py](file:///C:/Users/Lenovo/Desktop/SE-Labs-PES1UG24CS384/Lab-4/game.py)):**
  - Added feedback (`"You placed a disc in column X."` / `"AI placed a disc in column Y."`) printed exactly once per valid disc drop.

---

## Submission Checklist

Submission is only the following three things:

- [x] A 10-second video of gameplay **before** your changes, showing the bug/broken behavior (`before.mp4`)
- [x] A 10-second video of gameplay **after** your changes, showing the bug fixed and the new features working (`after.mp4`)
- [x] The Chat/LLM used page link, with the complete chat history: https://claude.ai/share/56914cc2-0791-40fb-b8c1-a1e3acbea036
