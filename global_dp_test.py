import pydp as dp
from pydp.algorithms.laplacian import *
import random
import sys
from scripts.algorithms.globaldp.global_algos import global_bounded_algo
import statistics


orig_stdout = sys.stdout
f = open('./tests/global_test.txt', 'w')
sys.stdout = f

# Generate list of random values, 0 - 100
vals = []

for i in range(0, 10000):
    val = random.randint(0, 100)
    vals.append(val)

# True statistics
print(f'Mean: {statistics.mean(vals)}')
print(f'Sum: {sum(vals)}')
print(f'Standard Deviation: {statistics.stdev(vals)}')
print(f'Variance: {statistics.variance(vals)}')
print(f'Min: {min(vals)}')
print(f'Max: {max(vals)}')
print(f'Median: {statistics.median(vals)}')

# DP Statistics
EPSILON = [0.1, 5, 10, 25, 50]

ALGORITHMS = ["bounded_mean", "bounded_sum", "standard_deviation", "variance", "min", "max", "median"]

for algo in ALGORITHMS:
    for e in EPSILON:
        print(f'{algo} || Epsilon: {e} || {global_bounded_algo(vals, e, algo)}')

sys.stdout = orig_stdout
f.close()