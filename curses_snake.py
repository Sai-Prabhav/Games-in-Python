import copy
import curses
import random
import time


class snake:
    """The snake game call the runSnake function to run the game"""

    def __init__(self, stdscr: curses.window) -> None:
        """Defines self and basic veriables

        Args:
            stdscr (curses.window): the curses windows that the game runs
        """
        self.HEIGHT, self.WIDTH = stdscr.getmaxyx()
        self.stdscr = stdscr
        self.score = 0
        self.hiscore = 0
        self.direction = 1
        self.snake_head = [int(round(self.WIDTH / 2)),
                           int(round(self.HEIGHT / 2))]
        self.snake_body = [
            copy.deepcopy(self.snake_head),
            [int(round(self.WIDTH / 2)) - 1, int(round(self.HEIGHT / 2))],
        ]
        self.food = [
            random.randint(1, self.WIDTH),
            random.randint(1, self.HEIGHT),
        ]
        self.stdscr.keypad(True)
        self.stdscr.clear()
        self.stdscr.nodelay(True)
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

    run = True

    def start(self) -> None:
        """The start and end screen for the game"""
        self.hiscore = self.score if self.score > self.hiscore else self.hiscore
        self.stdscr.nodelay(False)
        self.stdscr.clear()
        text = f"your score {self.score} and hi-score is {self.hiscore}"
        text1 = "to play once more"
        text11 = "plz press any key"
        self.stdscr.addstr(self.HEIGHT // 2, self.WIDTH //
                           2 - len(text) // 2, text)
        self.stdscr.addstr(self.HEIGHT // 2 - 1,
                           (self.WIDTH - len(text1)) // 2, text1)
        self.stdscr.addstr(self.HEIGHT // 2 - 1,
                           (self.WIDTH - len(text11)) // 2, text11)
        self.stdscr.getch()
        self.stdscr.clear()
        text3 = "use w a s d to move up, right"
        text4 = ", down and left respectively"
        self.stdscr.addstr(self.HEIGHT // 2, self.WIDTH //
                           2 - len(text3) // 2, text3)
        self.stdscr.addstr(
            self.HEIGHT // 2 + 1, self.WIDTH // 2 - len(text4) // 2, text4
        )
        self.score = 0

        self.stdscr.getch()
        self.stdscr.nodelay(True)
        self.stdscr.clear()

    def collide(self) -> None:
        """Checks if the snakes goes out of the screen or if it has eatten food or it has bit it self"""
        for i, cords in enumerate(self.snake_body):
            if cords[0] >= self.WIDTH - 1:
                self.snake_body[i][0] = 1
            if cords[0] <= 0:
                self.snake_body[i][0] = self.WIDTH - 2
            if cords[1] > self.HEIGHT - 1:
                self.snake_body[i][1] = 1
            if cords[1] <= 0:
                self.snake_body[i][1] = self.HEIGHT - 2
        cords = self.snake_head
        if cords[0] >= self.WIDTH - 1:
            self.snake_head[0] = 1
        if cords[0] <= 0:
            self.snake_head[0] = self.WIDTH - 2
        if cords[1] >= self.HEIGHT - 1:
            self.snake_head[1] = 1
        if cords[1] <= 0:
            self.snake_head[1] = self.HEIGHT - 2
        if self.snake_head[0] == self.food[0] and self.snake_head[1] == self.food[1]:
            self.score += 1
            self.stdscr.addstr(self.food[1], self.food[0], "█")
            self.food = (
                random.randint(1, self.WIDTH - 3),
                random.randint(1, self.HEIGHT - 3),
            )
            self.snake_body.append(self.snake_body[-1])
        for part in self.snake_body[1:]:
            if part == self.snake_head:
                self.run = False

    def move(self) -> None:
        """Takes input from user and moves the snake accordingly"""
        input = self.stdscr.getch()

        if input == ord("w") and self.direction != 2:

            self.direction = 0
        if input == ord("d") and self.direction != 3:
            self.direction = 1
        if input == ord("s") and self.direction != 0:
            self.direction = 2
        if input == ord("a") and self.direction != 1:
            self.direction = 3
        if input == ord("q"):
            self.run = False

        if self.direction == 0:
            self.snake_head[1] -= 1

        if self.direction == 1:
            self.snake_head[0] += 1

        if self.direction == 2:
            self.snake_head[1] += 1

        if self.direction == 3:
            self.snake_head[0] -= 1

        self.snake_body.insert(0, copy.deepcopy(self.snake_head))

        self.stdscr.addstr(self.snake_head[1], self.snake_head[0], "█")

        self.stdscr.addstr(
            self.snake_body[len(self.snake_body) - 1][1],
            self.snake_body[len(self.snake_body) - 1][0],
            " ",
        )
        self.snake_body.pop(-1)
        self.stdscr.addstr(self.food[1], self.food[0], "@")

    def runGame(self) -> None:
        """The main game loop"""
        self.start()
        while self.run:
            t = time.time()
            self.collide()
            self.move()
            self.stdscr.border('|', '|', '-', '-', '+', '+', '+', '+')
            self.stdscr.refresh()
            time.sleep(0.15 - (time.time() - t))

        if self.run is False:
            self.start()


def runSnake(stdscr: curses.window) -> None:
    """A callable function to run the game. creates a new window and pass it to snake class and runs it

    Args:
        stdscr (curses.window): the window in which the game runs
    """
    LINES, WIDTH = stdscr.getmaxyx()
    if LINES < 30 or WIDTH < 30:
        print(f"screen size in only {LINES} ,{WIDTH}")
        return
    win = curses.newwin(30, 30, (LINES-30)//2, (WIDTH-30)//2)
    snakee = snake(win)
    snakee.runGame()


if __name__ == "__main__":
    curses.wrapper(runSnake)
