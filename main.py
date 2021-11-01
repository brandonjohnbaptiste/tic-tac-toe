#!/usr/bin/env python3


# Tic Tac Toe: By Brandon J-B (01/11/2021)
ROWS = 3
COLUMNS = 3


def create_board():
    global ROWS, COLUMNS
    board_arr = ['-' for i in range(ROWS * COLUMNS)]
    return board_arr


def display_board(board):
    """ Takes in an array and displays it in a grid """
    print('\n')
    print('\t     |     |')
    print(f'\t  {board[0]}  |  {board[1]}  |  {board[2]}')
    print('\t_____|_____|_____')

    print('\t     |     |')
    print(f'\t  {board[3]}  |  {board[4]}  |  {board[5]}')
    print('\t_____|_____|_____')

    print('\t     |     |')
    print(f'\t  {board[6]}  |  {board[7]}  |  {board[8]}')
    print('\t     |     |')
    print('\n')


def update_board(board, pos, sign):
    board[pos] = sign
    return board


def check_row(board, row, sign):
    global ROWS
    row = board[(3 * (row - 1)):(3 * row)]
    if row.count(sign) == ROWS:
        print(f'win condition met in row {row}')
    else:
        print(f'no win for row {row}')


def check_winner(board, sign):
    global ROWS, COLUMNS
    for row in range(ROWS):
        check_row(board, row + 1, 'X')


if __name__ == '__main__':
    game_board = create_board()
    print(game_board)
    display_board(game_board)
    update_board(game_board, 0, 'X')
    update_board(game_board, 1, 'X')
    update_board(game_board, 2, 'X')
    display_board(game_board)
    check_winner(game_board, 'X')


