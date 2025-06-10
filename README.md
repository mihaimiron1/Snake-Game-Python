# 🐍 Snake Game

A simple implementation of the classic Snake game using Python's `turtle` module. Guide the snake, collect food, and try to score as high as possible without hitting the walls or your own tail.

## 🎮 How to Play

- Control the snake using the arrow keys:
  - ⬆️ `Up` – move up
  - ⬇️ `Down` – move down
  - ⬅️ `Left` – move left
  - ➡️ `Right` – move right
- Each time the snake eats food, it grows and your score increases.
- The game ends when:
  - The snake hits the wall
  - The snake hits its own body

## 📁 Project Structure

- `main.py` – Sets up the game window and handles the main game loop
- `snake.py` – Defines the Snake class and its behavior (movement, growth, direction)
- `food.py` – Manages food generation and placement
- `scoreboard.py` – Displays and updates the score

## ▶️ Run the Game

Make sure you have Python 3 installed. Then simply run:

```bash
python main.py
