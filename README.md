



# Tic-Tac-Toe with AI (Alpha-Beta Pruning) 🎮🤖

![Tic-Tac-Toe AI Illustration](https://github.com/user-attachments/assets/944c6215-ac6f-4677-ad5e-a068e7d4b27d)

Welcome to **Tic-Tac-Toe with AI**, a console-based game where you can challenge an intelligent AI opponent powered by the Minimax algorithm with Alpha-Beta Pruning. The AI is designed to play optimally and provide a challenging gameplay experience.

## Features ✨
- **Interactive Gameplay:** Play against a smart AI in a classic Tic-Tac-Toe game.
- **AI-Powered Opponent:** The AI uses the Minimax algorithm with Alpha-Beta Pruning to make optimal moves.
- **Clear Board Display:** Easy-to-read board representation in the console.
- **Win, Lose, or Draw:** Handles all possible outcomes of the game.

## How It Works 🧠
1. **Minimax Algorithm:** Simulates all possible moves to find the best outcome.
2. **Alpha-Beta Pruning:** Optimizes the Minimax algorithm by pruning unnecessary branches of the game tree, improving performance.
3. **Game Flow:**
   - The player makes the first move (O).
   - The AI responds with the optimal move (X).
   - The game alternates turns until there is a winner or a draw.

## Getting Started 🚀

### Prerequisites 📋
- Python 3.6+

### Installation 🛠️
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/tic-tac-toe-ai.git
   ```
2. Navigate to the project directory:
   ```bash
   cd tic-tac-toe-ai
   ```
3. Run the game:
   ```bash
   python game.py
   ```

### How to Play 🎲
1. Start the game by running the script.
2. Enter your move as row and column indices (e.g., `0 1` for the top-middle cell).
3. Watch as the AI calculates and makes its move.
4. Continue until there is a winner or the game ends in a draw.

## Example Gameplay 🎮
```
Welcome to Tic-Tac-Toe with AI (Alpha-Beta Pruning)!
  |   |  
---------
  |   |  
---------
  |   |  

Enter your move (row and column, separated by a space): 0 0
X |   |  
---------
  |   |  
---------
  |   |  
AI's move:
X |   | O
---------
  |   |  
---------
  |   |  
```

## Project Structure 🗂️
- **`game.py`**: Main game logic and user interaction.
- **`ai_logic.py`**: AI implementation using Minimax and Alpha-Beta Pruning.
- **`README.md`**: Project documentation.
- **`requirements.txt`** (if needed): Any external dependencies (currently none).

## Tools and Technologies 🛠️
- **Python:** Core programming language.
- **Minimax Algorithm:** AI logic for optimal moves.
- **Alpha-Beta Pruning:** Performance optimization for the AI.

## Future Improvements 🔮
- Add a GUI for a better user experience.
- Allow players to select their symbol (X or O).
- Implement multiplayer mode.

## License 📄
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgements 🙌
- Minimax Algorithm: Core inspiration for AI decision-making.
- Alpha-Beta Pruning: Optimized performance for real-time gameplay.

## Contributing 🤝
Feel free to fork the repository and submit pull requests for enhancements or bug fixes.

---

Enjoy the game and test your skills against the AI! 🎉
