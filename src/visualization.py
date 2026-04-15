import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter
import numpy as np
import os

def plot_convergence(best_dist, output_path):
    plt.figure(figsize=(10, 5))
    plt.plot(best_dist, color='royalblue', linewidth=2)
    plt.title('(Convergence Plot)', fontsize=14)
    plt.xlabel('Generation', fontsize=12)
    plt.ylabel('(Best Distance)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)


    final_dist = best_dist[-1]
    plt.annotate(f'Final: {final_dist:.2f}',
                 xy=(len(best_dist), final_dist),
                 xytext=(len(best_dist) * 0.8, final_dist * 1.1),
                 arrowprops=dict(facecolor='black', shrink=0.05))


    plt.savefig(os.path.join(output_path, 'plot_convergence.png'))
    plt.show()



def paths_gif(cities, history_best_paths, output_path):
    fig, ax = plt.subplots(figsize = (8,6))

    def update(frame):
        ax.clear()
        path = history_best_paths[frame]
        ordered_cities = cities[path]
        closed_path = np.vstack([ordered_cities, ordered_cities[0]])

        ax.scatter(cities[:, 0], cities[:, 1], color = 'red', zorder = 5)
        ax.plot(closed_path[:,0], closed_path[:,1], linestyle = '-', marker = 'o')

        ax.set_title(f'Generation: {frame * 5}')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')

    ani = FuncAnimation(fig, update, frames = len(history_best_paths), interval = 100)

    ani.save(os.path.join(output_path, 'evolution_paths.gif'), writer = PillowWriter(fps = 10))
    plt.show()