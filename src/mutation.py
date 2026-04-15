import random
import numpy as np

def mutation(offspring_population: np.ndarray, mutation_rate: float, no_of_cities: int):
    mutated_population = offspring_population.copy()
    for i in range(len(offspring_population)):
        if random.random() < mutation_rate:
            a, b = sorted(random.sample(range(1, no_of_cities), 2))
            mutated_population[i, a:b] = mutated_population[i, a:b][::-1]
    return mutated_population

