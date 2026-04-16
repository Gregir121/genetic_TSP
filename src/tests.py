import unittest
import numpy as np
from initialization import initialization
from fitness_calculation import fitness_calc

class TestGeneticAlgorithm(unittest.TestCase):
    def setUp(self):
        self.pop_size = 50
        self.cities_count = 10
        self.closed_pts, self.cities, self.pop, self.dist_matrix = initialization(self.cities_count, self.pop_size)

    def test_init_shapes(self):
        """Checks matrix shapes in initialization function"""
        self.assertEqual(self.pop.shape, (self.pop_size, self.cities_count))
        self.assertEqual(self.dist_matrix.shape, (self.cities_count, self.cities_count))

    def test_unique(self):
        """Tests if every city is visited exactly once"""
        for individual in self.pop:
            unique_cities = np.unique(individual)
            self.assertEqual(len(unique_cities), self.cities_count,"Error!! Cities are repeating")

    def test_fitness(self):
        """Tests if value of fitness is not equal to zero"""
        fitness, distances, best_idx = fitness_calc(self.dist_matrix, self.pop)
        self.assertTrue(np.all(fitness > 0))
        self.assertTrue(np.all(np.isfinite(fitness)))



if __name__ == '__main__':
    unittest.main()


