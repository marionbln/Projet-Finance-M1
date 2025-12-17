import matplotlib.pyplot as plt
import numpy as np

def plot_paths(paths, n=50):
    for i in range(n):
        plt.plot(paths[i], alpha=0.4)
    plt.title("Trajectoires Monte-Carlo")
    plt.xlabel("Années")
    plt.ylabel("Indice")
    plt.show()
