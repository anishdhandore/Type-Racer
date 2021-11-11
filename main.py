import curses   # lets you use colors on console/cmd
from curses import wrapper
import time

# starts the cmd screen for us
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.getkey()

def wpm_test(stdscr):
    display_message = "Start typing the below line of code\n"
    target_text = "Type Hello world!"
    #stdscr.addstr(1,0, " ")
    text_list = []
    stdscr.clear()
    stdscr.addstr(display_message)
    stdscr.addstr(target_text)
    stdscr.addstr(1,0,"") # brings the cursor back to the first character, before typing

    # pairing colors together, id, text color, backg color
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    size_target_text = len(target_text)
    row = 1
    column = 0
    index = 0
    while True:
        key = stdscr.getkey()
        text_list.append(key)
        # check if key matches the correct word
        if (key == target_text[index]):
            stdscr.addstr(row, column, key, curses.color_pair(1))
        else:
            stdscr.addstr(row, column, key, curses.color_pair(2))
        column += 1
        index += 1
        size_target_text -= 1
        if (size_target_text == 0):
            break

def main(stdscr):
    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)