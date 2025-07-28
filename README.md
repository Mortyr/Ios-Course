# iOS Course Repository

This repository contains sample projects for an iOS course. A small command-line
snake game has been added for fun and practice.

## Snake Game

The `snake.py` script uses Python's `curses` library to implement a simple
terminal-based snake game. Use the arrow keys (or WASD) to control the snake.

Run it with:

```bash
python3 snake.py
```

The game ends if the snake hits the wall or itself. Your score is displayed
when the game ends.

## Web-based Snake Game

A simple HTML/JavaScript version is available in `snake_web.html`.
Open `index.html` or the game file directly in your browser, or serve the
repository locally:

```bash
python3 -m http.server
```

Then browse to `http://localhost:8000/` and click **Play Snake in your
browser** (or open `http://localhost:8000/snake_web.html`) to begin playing.

