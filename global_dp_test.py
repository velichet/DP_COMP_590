import pydp as dp
from pydp.algorithms.laplacian import *
import random
import sys
from scripts.algorithms.globaldp.global_algos import global_bounded_algo
import statistics


orig_stdout = sys.stdout
f = open('./tests/global_test.csv', 'w')
sys.stdout = f

# Print
print('statistic,epsilon,result')

# Generate list of random values, 0 - 100
vals = []

for i in range(0, 10000):
    val = random.randint(0, 100)
    vals.append(val)

# True statistics
print(f'Mean,{-1},{statistics.mean(vals)}')
print(f'Sum,{-1},{sum(vals)}')
print(f'Standard Deviation,{-1},{statistics.stdev(vals)}')
print(f'Variance,{-1},{statistics.variance(vals)}')
print(f'Min,{-1},{min(vals)}')
print(f'Max,{-1},{max(vals)}')
print(f'Median,{-1},{statistics.median(vals)}')

# DP Statistics
EPSILON = [0.1, 5, 10, 25, 50]

ALGORITHMS = ["bounded_mean", "bounded_sum", "standard_deviation", "variance", "min", "max", "median"]

for algo in ALGORITHMS:
    for e in EPSILON:
        if(algo == 'max' or algo == 'min'):
            print(f'{algo},{e},{global_bounded_algo(vals, e, algo, lower_bound=0, upper_bound=100)}')
        else:
            print(f'{algo},{e},{global_bounded_algo(vals, e, algo)}')

sys.stdout = orig_stdout
f.close()