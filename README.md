# Overview
This project is to simulate DNA circularization and concatemerization using mathematical model.

Circularization direcotry contains all models simulating circularization. Similarly, concatemerization directory\
contains all models simulating concatemerization. Models in these two files consider circularization and \
concatemerization independently, which might be a limitation.

Data directory contains all data for all models. Same for figure directory.

## `circularization\`
For circularization, we have several models.

### Eventual Return Formula
It uses combinatorial formula to count number of returns of DNA to calculate probability of circularization. It is\
counted as circularization as it reaches the origin. The limitation is that there is a big gap from reality.

### Random Walk Model
We use a random package for choosing the next step, and let it walk for a certain number and count number of\
circularization. We define circularization happens if the head of DNA is within a sphere with radius 1 length of\
nucleotide created based on the position of tial of DNA.

There are many ways for randomly walk. For a fast method, one is for 6 directions, and another is 5 directions, which\
does not include completely going back direction. We also have lattice grid with 360 * 180 directions and another way\
that distribute directions based on Fibonacci sphere and it cannot go to directions too sharply curved from previous\
direction.

We use numba to accelerate the speed of running.

`3d_eventual_return_formula.py` implements a math formula from a math paper.

`3d_random_walk_baisc.py` uses 6 directions.

`3d_random_walk_5_dir.py` uses 5 directions.

`3d_random_walk_numpy.py` uses numpy.

`jit_3d_random_walk_5_dir.py` uses 5 directions and jit.

## `concatemerization\`
For concatemerization, we use Monte Carlo method to get probability.

We defined concatemerization happens if, similarly from circularization, distance between head and tail  is elss than 1.
For `comcatemerization_ranom.py`, the DNA tails are randomly generated according to uniform distribution. Other files\
assumed DNA tails are evenly distributed, which is far from reality.

## Others
`direction_functions.py` contains all functions generating directions.

`directionTest.py` is to test functions in `directions_functions.py`.

`simulation.py` contains a model considering circularization and concatemerization together.

`npyReader.py`
to heads.npy and furthest.npy generated in simulation.py

`distance.png`
ratio of cir and con with increasing distance and fixed DNA length

`original.py`
the original version

`previous.py`
a temporary file saving last edition

`byGPT.py`
a very basic example generated by GPT with visualization

`heads.npy` and `furtherest.npy`
positions of all heads and the furthest distance from head to tail for each molecule

`output.txt is`
the output of simulation.py