
# 🎮 Hangman Game Challenge

Build the classic word-guessing game using Python strings, loops, and user input.

## � What You'll Build

Create a Hangman game where players guess letters to reveal a hidden word before running out of attempts.

**Skills practiced:** String manipulation, loops, conditionals, random selection

## ✅ Must Have's

Your game must:
- Randomly select words from a predefined list
- Accept letter guesses and show current progress (_ _ _ format)
- Track incorrect guesses remaining
- End when word is guessed or attempts exhausted
- Display win/lose messages
## Learning objectives

- Practice working with strings, lists, and loops
- Use conditionals to control game flow and determine win/lose state
- Read user input and update program state each turn
- Use randomness to choose game data and design a simple game loop

## Difficulty & estimated time

- Difficulty: Beginner → Intermediate  
- Estimated time: 1–3 hours

## Starter files (place these in the assignment folder)

- starter-code.py — minimal scaffold with word list and game loop placeholder
- words.txt — optional list of words (one per line)
- README.md — this file (explain how to run and submit)

## Setup & run

1. Ensure Python 3 is installed.
2. From the assignment folder run:
    - python3 starter-code.py
3. Follow on-screen prompts to play.

## Requirements (acceptance criteria)

In addition to the Must Have's above, your submission should:
- Include a clear README with run instructions
- Contain well-named functions (for example: choose_word(), display_progress(), handle_guess())
- Handle invalid input (non-letter, repeated guesses) gracefully
- Not crash on empty or short word lists

## Tests & manual checks

- Try guessing every letter to confirm win condition
- Exhaust attempts to confirm lose condition and reveal the word
- Test repeated guesses and non-letter input to validate robustness

## Stretch goals (optional)

- Allow guessing the full word
- Add ASCII-art hangman that progresses with wrong guesses
- Load words from a file and categorize by difficulty
- Save high scores or fastest wins to a simple JSON file

## Submission

- Commit your code to the assignment folder or create a ZIP named games-in-python-yourname.zip
- Include:
  - starter-code.py (or main script)
  - words.txt (if used)
  - README.md with run and design notes
- Add a short comment in your code explaining any non-obvious logic

## Grading rubric (suggested)

- Basic functionality (random word, guessing loop, win/lose): 60%
- Input validation and error handling: 15%
- Code organization and comments: 15%
- Stretch goals / extras: 10%

## Hints

- Use a set to track guessed letters for O(1) membership checks
- Build the display string by iterating the target word and revealing letters in guessed set
- Keep the game loop small: get input → validate → update state → render → check end conditions

Good luck — build something fun and readable!