from fitness_calculation import fitness_calc
from initialization import initialization
from selection import selection

closed_points, cities, starting_population, distance_matrix = initialization(20, 50)

fitness, distance, best_index = fitness_calc(distance_matrix, starting_population, 0.0000001)

selection(starting_population, fitness, 'ranked')



