
# 🎮 Games in Python — Hangman

Short assignment to build a terminal Hangman game that reinforces strings, lists, control flow, and simple I/O. Follow the project template and file layout so instructors and automated checks can find your work.

---

## Summary
Create a terminal-based Hangman game that:
- Randomly selects a word from an internal list or words.txt
- Lets the player guess single letters (optionally full words)
- Shows progress each turn (e.g., _ a _ _ m _ n)
- Tracks remaining incorrect attempts and ends with a clear win/lose message

Difficulty: Beginner → Intermediate  
Estimated time: 1–3 hours

---

## Learning objectives
- Manipulate strings and lists to represent game state
- Implement control flow (loops, conditionals) for a game loop
- Validate and handle user input robustly
- Use randomness and modular functions to structure code
- Separate core logic from I/O to make testing easier

---

## Prerequisites
- Python 3.x installed
- Basic familiarity with Python (variables, loops, functions)
- Recommended: ability to run a script from the command line

---

## Assignment folder (required files)
Place these files in assignments/games-in-python/:
- starter-code.py — scaffold with main game loop and function placeholders
- words.txt — optional words list (one word per line)
- README.md — this file (how to run and submit)

Recommended minimal layout:
- assignments/games-in-python/starter-code.py
- assignments/games-in-python/words.txt
- assignments/games-in-python/README.md

---

## Setup & run
## Required functions & structure (suggested)
Provide well-named functions such as:
- choose_word(word_list) -> str
- display_progress(word, guessed_set) -> str
- handle_guess(guess, word, guessed_set, wrong_guesses) -> (updated_state)
- play_game() -> None

Keep the game loop isolated in a main function and protect with:
```
if __name__ == "__main__":
     play_game()
```

## Acceptance criteria (requirements)
Your submission must:
- Randomly pick words from a predefined list or words.txt
- Accept single-letter guesses and render progress each turn
- Track and display remaining incorrect attempts
- End correctly on win or loss and show an appropriate message
- Handle invalid input (non-letters, repeated guesses) without crashing
- Work with short or empty word lists (fail gracefully or show an informative message)
- Include a clear README with run instructions

## Tests & manual checks
- Guess every letter to confirm the win condition is detected
- Intentionally exhaust attempts to confirm the lose condition and reveal the word
- Enter repeated guesses and non-letter input to validate robustness
- Test with words.txt empty or with a single word

## Stretch goals (optional)
- Allow guessing the full word (bonus input)
- Add ASCII-art hangman that progresses with wrong guesses
- Load words from a file and categorize by difficulty
- Save high scores or fastest wins to a simple JSON file
- Implement unit tests for core functions

## Submission
- Commit your solution to assignments/games-in-python/ in this repository or create a ZIP named games-in-python-yourname.zip
- Include:
  - starter-code.py (or the main script)
  - words.txt (if used)
  - README.md with run and short design notes
- Add a short inline comment explaining any non-obvious logic

## Grading rubric (suggested)
- Basic functionality (random word, guessing loop, win/lose): 60%
- Input validation and error handling: 15%
- Code organization and comments: 15%
- Stretch goals / extras: 10%

## Hints
- Use a set for guessed letters for O(1) membership checks
- Build the display string by iterating the target word and revealing letters present in the guessed set
- Keep loop steps small: read input → validate → update state → render → check end conditions
- Separate I/O from logic where possible to simplify testing

Good luck — keep the code clear, modular, and student-friendly!