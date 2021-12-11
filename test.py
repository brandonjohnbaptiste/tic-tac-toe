import curses
from time import sleep
from curses import wrapper


def main(stdscr):

    board = ['-', '-', '-', '-', '-', '-', '-', '-', '-']

    stdscr.clear()
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[0]}  |  {board[1]}  |  {board[2]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[3]}  |  {board[4]}  |  {board[5]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[6]}  |  {board[7]}  |  {board[8]}\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.refresh()
    sleep(2)

    board = ['X', '-', '-', '-', '-', '-', '-', '-', '-']

    stdscr.clear()
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[0]}  |  {board[1]}  |  {board[2]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[3]}  |  {board[4]}  |  {board[5]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[6]}  |  {board[7]}  |  {board[8]}\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.refresh()
    sleep(2)

    board = ['X', '-', '-', '-', 'X', '-', '-', '-', '-']

    stdscr.clear()
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[0]}  |  {board[1]}  |  {board[2]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[3]}  |  {board[4]}  |  {board[5]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[6]}  |  {board[7]}  |  {board[8]}\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.refresh()
    sleep(2)

    board = ['X', '-', '-', '-', 'X', '-', '-', '-', 'X']

    stdscr.clear()
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[0]}  |  {board[1]}  |  {board[2]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[3]}  |  {board[4]}  |  {board[5]}\n')
    stdscr.addstr('\t_____|_____|_____\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.addstr(f'\t  {board[6]}  |  {board[7]}  |  {board[8]}\n')
    stdscr.addstr('\t     |     |\n')
    stdscr.refresh()
    sleep(2)


wrapper(main)
