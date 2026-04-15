from initialization import initialization
from fitness_calculation import fitness_calc
from selection import selection
from crossover import crossover
from mutation import mutation



def run_evolution(no_of_generations: int, no_of_cities: int , population_size: int):
    closed_points, cities, starting_population, distance_matrix = initialization(no_of_cities, population_size)

    best_dist = []
    best_paths = []

    if no_of_generations % 2 != 0:
        no_of_generations += 1

    for generation in range(no_of_generations):
        fitness, distances, best_index = fitness_calc(distance_matrix, starting_population, eps = 0.00001)

        best_individual = starting_population[best_index].copy()
        current_best_dist = distances[best_index]
        best_dist.append(current_best_dist)

        selected_population = selection(starting_population, fitness, 'ranked')
        offspring_population = crossover(selected_population, 0.5)
        mutated_population = mutation(offspring_population, 0.1, no_of_cities)

        mutated_population[0] = best_individual #To make sure the next result is only getting better than the best already

        starting_population = mutated_population

        if generation % 50 == 0:
            print(f'Generation: {generation}, Best distance: {current_best_dist}')

        if generation % 5 == 0:
            best_paths.append(best_individual.copy())

    return best_dist, best_paths, starting_population, cities



