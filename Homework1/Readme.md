This program runs using python 2.7
The libraries using are default libraries, but incase any are missing I included
a requriements.txt so just pip install -r requriements.txt to fix any dependency issues.

usage: conway.py [-h] -s DIMENSION -p PATTERN

Simulates Conway's game of life

optional arguments:
  -h, --help    show this help message and exit
  -s DIMENSION  Enter the size of the board(at least 5)
  -p PATTERN    The type of pattern to run, glider, small exploder, exploder,
                10-row cell, lightweight space ship, and tumbler. Or just
                random


Examples of running with different patterns:

python conway.py -s 40 -p "10-row cell"
python conway.py -s 40 -p "small exploder"
python conway.py -s 40 -p "exploder"
python conway.py -s 40 -p "lightweight space ship"
python conway.py -s 40 -p "random"
