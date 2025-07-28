# Simple snake game using curses
import curses
import random

# Constants
HEIGHT = 20
WIDTH = 40

UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    stdscr.timeout(100)

    snake = [(HEIGHT // 2, WIDTH // 2 + i) for i in range(3)]
    direction = LEFT
    food = place_food(snake)
    score = 0

    while True:
        key = stdscr.getch()
        new_direction = direction
        if key in [curses.KEY_UP, ord('w')]:
            new_direction = UP
        elif key in [curses.KEY_DOWN, ord('s')]:
            new_direction = DOWN
        elif key in [curses.KEY_LEFT, ord('a')]:
            new_direction = LEFT
        elif key in [curses.KEY_RIGHT, ord('d')]:
            new_direction = RIGHT

        # Prevent reversing directly
        if (new_direction[0] * -1, new_direction[1] * -1) != direction:
            direction = new_direction

        head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if (
            head[0] < 0 or head[0] >= HEIGHT or
            head[1] < 0 or head[1] >= WIDTH or
            head in snake
        ):
            msg = f"Game over! Score: {score}".center(WIDTH)
            stdscr.addstr(HEIGHT // 2, 0, msg)
            stdscr.nodelay(False)
            stdscr.getch()
            break

        snake.insert(0, head)
        if head == food:
            score += 1
            food = place_food(snake)
        else:
            snake.pop()

        stdscr.clear()
        draw_border(stdscr)
        stdscr.addstr(0, 2, f" Score: {score} ")
        stdscr.addch(food[0] + 1, food[1] + 1, '*')
        for y, x in snake:
            stdscr.addch(y + 1, x + 1, '#')
        stdscr.refresh()

def place_food(snake):
    while True:
        pos = (random.randint(0, HEIGHT - 1), random.randint(0, WIDTH - 1))
        if pos not in snake:
            return pos

def draw_border(stdscr):
    for x in range(WIDTH + 2):
        stdscr.addch(0, x, '#')
        stdscr.addch(HEIGHT + 1, x, '#')
    for y in range(1, HEIGHT + 1):
        stdscr.addch(y, 0, '#')
        stdscr.addch(y, WIDTH + 1, '#')

if __name__ == "__main__":
    curses.wrapper(main)
