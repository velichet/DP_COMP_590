from scripts.algorithms.globaldp.global_algos import global_bounded_algo

def driver_global_algo(data: dict, stats: dict):
    '''
    Compute the specified global DP statistics on the data

    Input (data: dict, stats: dict):
        data = {
            age: [10,20,30]
            height: [50,60,70]
            wight: [100,110,120]
        }
        stats = {
            age: {
                bounded_mean: {
                    epsilon: 5,
                    low: 0,
                    height: 100
                }
            },
            ...
        }

    Output:
        stats = {
            age: {
                bounded_mean: 20.5,
                ...
            }
        }
    '''
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
            val = global_bounded_algo(data[col], float(params['epsilon']), stat, float(params['low']), float(params['high']))
            temp[stat] = val

        result[col] = temp
   
    return result

# TODO: COUNT and (DYNAMIC) PERCENTILE SUPPORT