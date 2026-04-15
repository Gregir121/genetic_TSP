import numpy as np

def fitness_calc(distance_matrix: np.ndarray, population: np.ndarray, eps = 0.000001):


    pop_shift = np.roll(population, shift = -1, axis = 1 )

    city_pairs = distance_matrix[population, pop_shift]

    distance = np.sum(city_pairs, axis = 1)

    fitness = 1 / (distance + eps)

    best_index = np.argmax(fitness)

    return fitness, distance, best_index