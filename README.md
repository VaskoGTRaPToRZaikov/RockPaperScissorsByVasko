  Rock Paper Scissors Game

A colorful console-based Python implementation of the classic Rock Paper Scissors game with score tracking.

  Project Goals

This project implements the timeless Rock Paper Scissors game in a digital format, providing:

Classic Gameplay: Traditional rock-paper-scissors rules with computer opponent
Score Tracking: Persistent score tracking throughout the gaming session
Visual Feedback: Colorful output using the colorama library for enhanced user experience
Continuous Play: Option to play multiple rounds without restarting the program
Educational Value: Demonstrates basic game logic, user input handling, and random number generation
Entertainment: Provides quick, fun gaming sessions for all ages

  Solution

  Game Logic Algorithm
The game implements the classic rules:
1. Rock beats Scissors
2. Paper beats Rock
3. Scissors beats Paper
4. Same choices result in a Draw

  Core Algorithm Flow:
1. Accept player input (r/rock, p/paper, s/scissors)
2. Generate random computer choice (1-3 mapped to moves)
3. Compare moves using conditional logic
4. Update scores and display results with colors
5. Offer replay option with input validation

  Technologies Used
- Python 3.x: Core programming language
- random module: For generating computer's random moves
- colorama library: For colorful console output
  - `Fore.GREEN`: Win messages
  - `Fore.RED`: Lose messages  
  - `Fore.YELLOW`: Draw messages
  - `Style.RESET_ALL`: Reset colors
- Built-in input/output: User interaction and display

  Key Features
- Input Flexibility: Accepts both single letters (r/p/s) and full words
- Input Validation: Handles invalid inputs gracefully
- Score Persistence: Tracks wins/losses throughout session
- Colorful Interface: Visual feedback with different colors for outcomes
- Continuous Play: Play multiple rounds without restarting
- Clean Exit: Proper game termination with thank you message

  Source Code

The complete source code is available in:
- [Main Game File](rock_paper_scissors.py)
- Dependencies: Requires `colorama` library installation

  Installation Requirements
```bash
pip install colorama
```

  Screenshots

  Game Start & Input

<img width="356" height="99" alt="image" src="https://github.com/user-attachments/assets/bbeaf106-124a-4611-92da-a4f36cc3941a" />

  Different Game Outcomes

<img width="331" height="98" alt="image" src="https://github.com/user-attachments/assets/5b36d271-5181-4ea6-ab61-0072242ea0bc" />

  Play Again Option

<img width="486" height="176" alt="image" src="https://github.com/user-attachments/assets/20cfc671-7766-42f2-b409-4f0c43c319d4" />

  Invalid Input Handling

<img width="429" height="114" alt="image" src="https://github.com/user-attachments/assets/59fbf891-45fe-4133-915c-918ab50c4f98" />

  Live Demo

  Local Installation & Run:

1. Install Python 3.x if not already installed
2. Install colorama library:
   ```bash
   pip install colorama
   ```
3. Download the source code and save as [rock_paper_scissors.py](rock_paper_scissors.py)
4. Run the game:
   ```bash
   python rock_paper_scissors.py
   ```
5. Play: Follow on-screen instructions!

  Online Demo Options:

[<img alt="Play Game" src="https://github.com/user-attachments/assets/2117a2a4-c5f8-46f6-8359-d3b8a2798d38" />](https://replit.com/@vaskozaikov/RockPaperScissorsByVasko)

---

  Game Rules & Controls

  Controls:
- [r] → Rock
- [p] → Paper  
- [s] → Scissors
- [y] → Play again
- [n] → Quit game

  Winning Conditions:
- Rock crushes Scissors
- Paper covers Rock  
- Scissors cuts Paper
- Same choice = Draw

  Code Structure

```python
# Game Variables
rock, paper, scissors = "Rock", "Paper", "Scissors"
player_score, computer_score = 0, 0

# Main Game Loop
while True:
    # 1. Get player input
    # 2. Generate computer move  
    # 3. Compare moves
    # 4. Update scores
    # 5. Display results with colors
    # 6. Ask to play again
```

  Future Enhancements

- [ ] Add game statistics and win/loss ratios

---

Ready to test your luck against the computer? Let the games begin!
