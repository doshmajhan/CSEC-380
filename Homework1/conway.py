# Python program to simulate conways game of life
# @author: Cameron Clark

import argparser
import sys

def setup(size):
    """
        Sets up our board of neighbors and the rules of the game
    """
    board = [[0 for x in range(size)] for y in range(size)]


def simulate():
    """
        Begins running the simulation according to the rules of the game
    """


if __name__ == '__main__':
    parser = argparser.ArgumentParser(description="Simulates Conway's game of life")
    parser.add_argument('-s', help='Enter the size of the board, between 5 and 20', dest="dimension", required="True")
    args = parser.parse_args()
    if int(args.dimension) < 5 or int(args.dimension) > 20:
        print("Error: Please enter a size between 5 and 20")
        sys.exit()

    setup(int(args.dimension))
