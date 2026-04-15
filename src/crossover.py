import numpy as np
import random


def crossover(selected_population: np.ndarray, crossover_rate: float):

    pop_size, cities_count = selected_population.shape
    offspring = np.zeros_like(selected_population)
    for i in range(0, pop_size, 2):
        p1 = selected_population[i]
        p2 = selected_population[i+1]
        child1 = np.full(cities_count, -1)
        child2 = np.full(cities_count, -1)
        child1[0], child2[0] = 0, 0


        if random.random() < crossover_rate:
            cut1, cut2 = sorted(random.sample(range(1, cities_count), 2))
            child1[cut1:cut2] = p1[cut1:cut2]
            child2[cut1:cut2] = p2[cut1:cut2]
            child1[child1 == -1] = p2[~np.isin(p2, child1)]
            child2[child2 == -1] = p1[~np.isin(p1, child2)]
        else:
            child1, child2 = p1.copy(), p2.copy()

        offspring[i] = child1
        offspring[i+1] = child2
    return offspring
