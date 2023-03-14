from scripts.algorithms.globaldp.global_algos import global_bounded_algo

def driver_global_algo(data: dict, stats: dict):

    result = {}

    # Get column names to compute global stats
    col_names = data.keys()

    # Iterate over column names
    for col in col_names:

        temp = {}

        # Get the specified stats
        stats_list = stats[col].keys()

        # Compute all stats for column
        for stat in stats_list:
            params = stats[col][stat]
            val = global_bounded_algo(data[col],params['epsilon'], stat, params['low'], params['high'])
            temp[stat] = val

        result[col] = temp
   
    return result
