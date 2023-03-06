import pydp as dp
from pydp.algorithms.laplacian import *

ALGORITHMS = {
    "bounded_mean": dp.algorithms.laplacian.BoundedMean,
    "bounded_sum": dp.algorithms.laplacian.BoundedSum,
    "standard_deviation": dp.algorithms.laplacian.BoundedStandardDeviation,
    "variance": dp.algorithms.laplacian.BoundedVariance,
    "max": dp.algorithms.laplacian.Max,
    "min": dp.algorithms.laplacian.Min,
    "median": dp.algorithms.laplacian.Median
}

def global_bounded_algo(data: list, epsilon, input_func: str, lower_bound=None, upper_bound=None):
    """
    Returns value after a bounded algorithm has been performed on the data. Data and epsilon are required values.
    RECOMMENDED: Force the user to provide bounds.
    It may be necessary to use the max and the min of the dataset to enforce this.

    See this for more details: https://github.com/OpenMined/PyDP/blob/dev/src/pydp/algorithms/laplacian/_bounded_algorithms.py
    """

    algorithm = ALGORITHMS[input_func]

    try:
        # User bounds
        algo = algorithm(epsilon=epsilon, lower_bound=lower_bound, upper_bound=upper_bound, dtype="float")
        return algo.quick_result(data)
    except:
        # Enforce bounds
        algo = algorithm(epsilon=epsilon, lower_bound=min(data), upper_bound=max(data), dtype="float")
        return algo.quick_result(data)

# Count
def global_count(data: list, epsilon):
    """
    Return differentailly private count.
    """
    algo = Count(epsilon=epsilon, dtype="float")
    return algo.quick_result(data)

# Percentile
def global_percentile(data: list, epsilon, percentile, lower_bound=None, upper_bound=None):
    """
    Calculate differentially private percentile. Params includes percentile.
    Bounds must be included from user.
    """
    algo = Percentile(epsilon=epsilon, percentile=percentile, lower_bound=lower_bound, upper_bound=upper_bound, dtype="float")
    return algo.quick_result(data)