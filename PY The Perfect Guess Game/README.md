# The Perfect Guess (Python)

A command-line number guessing game built with Python.

The program challenges the player to guess a randomly generated number within a user-defined range, while tracking the best (lowest) number of attempts for each range across sessions.

---

## Game Rules

1. The player selects a lower and upper bound
2. The program randomly selects a number within that range
3. The player guesses until the correct number is found
4. Feedback is given after each guess:
   - Too high → ask for a lower number
   - Too low → ask for a higher number
5. The total number of attempts is recorded

If the player beats the previous best score for the same range, a new high score is saved.

---

## Features

- Interactive command-line gameplay
- User-defined number ranges
- Persistent high-score tracking across sessions
- Separate records for different ranges
- Input validation and attempt counting

---

## Implementation Overview

This project demonstrates:
- Conditional logic and loops
- Random number generation
- Basic file handling for data persistence
- Simple state management in a CLI application

High scores are stored in text files, one per range.

---

## Purpose

This project was created as a learning exercise to practice:
- Python fundamentals
- File input/output
- Control flow
- Building small interactive programs

---

## Notes

- This is a learning project, not a production system
- File-based storage is used intentionally for simplicity
- Code clarity is prioritized over optimization

---

## License

MIT License
