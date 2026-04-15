import numpy as np

def initialization(no_of_cities: int,no_of_population: int ):
    cities = np.random.uniform(low = 0, high = 300, size = (no_of_cities, 2 ))
    first = cities[0]
    closed_points = np.vstack([cities, first])

    starting_population = []
    for i in range(no_of_population):
        idx = np.arange(1, no_of_cities)
        perm =  np.random.permutation(idx)
        individual = np.concatenate(([0], perm ))
        starting_population.append(individual)
    starting_population = np.array(starting_population)

    view_a = cities[:, np.newaxis, :]
    view_b = cities[np.newaxis, :, :]
    diff = view_a - view_b

    distance_matrix = np.sqrt(np.sum(diff**2, axis = 2))


    return closed_points, cities, starting_population, distance_matrix



