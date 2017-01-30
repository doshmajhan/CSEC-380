"""
    Python program to simulate conways game of life

    1/25/2017
    @author: Cameron Clark
"""
from __future__ import print_function
import argparse
import random
import os
import sys
import time

def setup(size, pattern):
    """
        Sets up our board of neighbors and the rules of the game

        :param size: the dimension of our board to be created
        :param pattern: the pattern to initialize the board with
        :return board: our populated board ready to be simulated
    """
    board = [[0 for x in range(size)] for y in range(size)]

    if pattern == 'random':
        board = random_pattern(board, size)

    if pattern == 'glider':
        board = glider(board, size)

    elif pattern == 'small exploder':
        board = small_exploder(board, size)

    elif pattern == 'exploder':
        board = exploder(board, size)

    elif pattern == '10-row cell':
        board = ten_row_cell(board, size)

    elif pattern == 'lightweight space ship':
        board = lightweight_space_ship(board, size)

    elif pattern == 'tumbler':
        board = tumbler(board, size)

    return board


def random_pattern(board, size):
    """
        Function to setup our board for a random pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    population = random.randint(1, (size*size) - 1) # generate a random number of spaces to populate
    for i in range(population):
        # Loop until we've inserted a live cell
        while True:
            x = random.randint(0, size - 1)
            y = random.randint(0, size - 1)
            # if the location doesn't already have a live cell, insert there
            if not board[x][y]:
                board[x][y] = 1
                break

    return board


def glider(board, size):
    """
        Function to setup our board for the glider pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    x = size/2
    y = size/2
    positions = [(x, y-1), (x, y+1), (x-1, y+1), (x-2, y)]
    board[x][y] = 1
    for n in positions:
        board[n[0]][n[1]] = 1

    return board


def small_exploder(board, size):
    """
        Function to setup our board for the small exploder pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    x = size/2
    y = size/2
    positions = [(x+1, y), (x-1, y), (x-2, y), (x, y-1),
                 (x, y+1), (x-1, y-1), (x-1, y+1)]
    for n in positions:
        board[n[0]][n[1]] = 1

    return board


def exploder(board, size):
    """
        Function to setup our board for the exploder pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    x = size/2
    y = size/2
    positions = [(x+2, y), (x-2, y), (x, y-2), (x, y+2),
                 (x-2, y-2), (x-2, y+2), (x+2, y-2), (x+2, y+2),
                 (x-1, y+2), (x-1, y-2), (x+1, y+2), (x+1, y-2)]
    for n in positions:
        board[n[0]][n[1]] = 1

    return board


def ten_row_cell(board, size):
    """
        Function to setup our board for the 10-row cell pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    x = size/2
    y = size/2
    positions = [(x, y-1), (x, y-2), (x, y-3), (x, y-4),
                 (x, y+1), (x, y+2), (x, y+3), (x, y+4)]
    board[x][y] = 1
    for n in positions:
        board[n[0]][n[1]] = 1

    return board


def lightweight_space_ship(board, size):
    """
        Function to setup our board for the lightweight space ship pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    x = size/2
    y = size/2
    positions = [(x-1, y), (x-1, y-1), (x-1, y+1), (x-1, y+2),
                 (x, y+2), (x, y-2), (x+1, y+2), (x+2, y+1), (x+2, y-2)]
    for n in positions:
        board[n[0]][n[1]] = 1

    return board


def tumbler(board, size):
    """
        Function to setup our board for the tumbler pattern

        :param board: the 2d array of ints board to be set up
        :param size: the dimension of the board
        :return board: the setup 2d array of ints
    """
    x = size/2
    y = size/2
    positions = [(x, y-1), (x, y+1), (x-1, y+1), (x-1, y+2), (x-2, y+1),
                 (x-2, y+2), (x-1, y-1), (x-1, y-2), (x-2, y-1), (x-2, y-2),
                 (x+1, y-1), (x+1, y+1), (x+2, y-1), (x+2, y+1), (x+3, y-2),
                 (x+3, y+2), (x+3, y-3), (x+3, y+3), (x+2, y-3), (x+2, y+3),
                 (x+1, y-3), (x+1, y+3)]
    for n in positions:
        board[n[0]][n[1]] = 1

    return board


def print_board(board, size):
    """
        prints our board out

        :param board: the board to be printed
        :param size: the dimension of the board
    """
    for x in range(size):
        for y in range(size):
            if board[x][y]:
                print('+', end=" ")
            else:
                print(' ', end=" ")
        print("\n")


def simulate(board, size):
    """
        Begins running the simulation according to the rules of the game

        :param board: the populated board to be ran in the simulation
        :param size: the size of the board
    """
    count = 1
    print("Initial")
    change_list = {}
    print_board(board, size)
    time.sleep(2)
    while True:
        for x in range(size):
            for y in range(size):
                result = check_neighbors(board, x, y)
                change_list[(x, y)] = result

        # update all our changes for the board
        for key in change_list:
            board[key[0]][key[1]] = change_list[key]

        #clear()
        print("Cycle: %d" % count)
        print_board(board, size)
        count += 1
        time.sleep(2)


def check_neighbors(board, x, y):
    """
        Checks the neighbors of a given position to see if it will live or dimension

        :param board: the board holding our cell
        :param x: the x position of the cell
        :param y: the y position of the cell
        :return result: wether the cell should live or die
    """
    alive = 0
    result = board[x][y]

    # list of possible neighbor locations to check
    neighbors = [(1, 1), (1, 0), (1, -1), (-1, 1), (-1, 0), (-1, -1), (0, 1), (0, -1)]
    for n in neighbors:
        temp_x = x + n[0]
        temp_y = y + n[1]
        # prevent negative array indexing so we don't wrap around
        if temp_x < 0 or temp_y < 0:
            continue

        # try to index, catch error if we over index
        try:
            if board[temp_x][temp_y]:
                alive += 1

        except IndexError:
            continue

    if alive < 2:
        result = 0

    elif alive > 3:
        result = 0

    elif board[x][y] == 0 and alive == 3:
        result = 1

    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simulates Conway's game of life")
    parser.add_argument('-s', help='Enter the size of the board(at least 5)', dest="dimension", required="True")
    parser.add_argument('-p', help='The type of pattern to run, glider, small exploder, exploder, 10-row cell, lightweight space ship, and tumbler. Or just random',
                              dest='pattern', required="True")

    pattern_list = ['glider', 'small exploder', 'exploder', '10-row cell', 'lightweight space ship', 'tumbler', 'random']
    args = parser.parse_args()

    if int(args.dimension) < 5:
        print("Error: Please enter a size of atleast 5")
        sys.exit()

    if args.pattern not in pattern_list:
        print("Error: Please enter a pattern type listed")
        sys.exit()

    board = setup(int(args.dimension), args.pattern)
    simulate(board, int(args.dimension))
