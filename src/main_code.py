from run_evolution import run_evolution
from visualization import paths_gif
from visualization import plot_convergence
import os

if __name__ == '__main__':

    best_dist, best_paths, starting_population, cities = run_evolution(1000, 70, 150)

    current_dir = os.path.dirname(os.path.abspath(__file__))

    project_root = os.path.dirname(current_dir)

    graphs_dir = os.path.join(project_root, 'graphs')
    if not os.path.exists(graphs_dir):
        os.mkdir(graphs_dir)


    paths_gif(cities, best_paths, graphs_dir)

    plot_convergence(best_dist, graphs_dir)
