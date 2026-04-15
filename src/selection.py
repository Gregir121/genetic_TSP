import numpy as np


def selection(population: np.ndarray, fitness_score: float, type_of_selection: str):

    if type_of_selection == 'roulette':
        roulette_probability = fitness_score / np.sum(fitness_score)
        roulette_indices = np.random.choice(np.arange(0, len(population)), size = len(population), p = roulette_probability)
        roulette_population = population[roulette_indices]
        return roulette_population
    elif type_of_selection == 'ranked':
        sort_indices = np.argsort(fitness_score)
        ranked_sorted = population[sort_indices]
        ranks = np.arange(1, len(population) + 1)
        total_ranks = np.sum(ranks)
        ranking_probability = ranks / total_ranks
        ranked_indices = np.random.choice(np.arange(0, len(population)), size=len(population), p=ranking_probability)
        ranked_population = ranked_sorted[ranked_indices]
        return ranked_population