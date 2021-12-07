import curses   # lets you use colors on console/cmd
from curses import wrapper
import time
import random

# starts the cmd screen for us
def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the Speed Typing Test!")
    stdscr.addstr("\nPress any key to begin!")
    stdscr.getkey()

def load_text():
    with open("randomtext.txt", "r") as f:
	    lines = f.readlines()
	    return random.choice(lines).strip()

def display_text(stdscr, key, target_text, row, column, index, redo, wpm=0):
    stdscr.addstr(2, 0, f"WPM: {wpm}")
    if redo == True:
        stdscr.addstr(row, column, key, curses.color_pair(3))
    else:
        # check if key matches the correct wordS
        if (key == target_text[index]):
            stdscr.addstr(row, column, key, curses.color_pair(1))
        else:
            stdscr.addstr(row, column, key, curses.color_pair(2))

def wpm_test(stdscr):
    display_message = "Start typing the below line of code\n"
    # target_text = "Type Hello world!"
    target_text = load_text()
    #stdscr.addstr(1,0, " ")
    text_list = []
    speed_test_list = []
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
    redo = False
    start_time = time.time()
    while True:
        key = stdscr.getkey()
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(text_list) / (time_elapsed / 60)) / 5)
        speed_test_list.append(key) # used to store all chars entered by user for calculating typing speed
        text_list.append(key)
        if key in ("KEY_BACKSPACE", '\b', "\x7f"):
            if len(text_list) > 0:
                text_list.pop()
                column -= 1
                index -= 1
                size_target_text += 1
                display_text(stdscr, key=target_text[index], target_text=target_text, row=row, column=column, index=index, redo=True, wpm=wpm)

        else:
            display_text(stdscr, key, target_text, row, column, index, redo, wpm=wpm)
            column += 1
            index += 1
            size_target_text -= 1
            if (size_target_text == 0):
                break
        if key == "@":
            break

def main(stdscr):
    start_screen(stdscr)
    wpm_test(stdscr)
    

wrapper(main)
# print(display_text())