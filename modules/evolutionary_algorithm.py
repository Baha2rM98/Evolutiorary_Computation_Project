import random

from modules.compute_fitness import compute_fitness
from modules.crossover import crossover
from modules.create_partitions import create_partitions


def run_algorithm(graph, weight_vector, k, MAX_GEN=500):
    n = len(graph)
    p = []
    for i in range(2 * n):
        temp = list(range(n))
        random.shuffle(temp)
        p.append(tuple(temp))
    for i in range(MAX_GEN):
        fitness = compute_fitness(graph, weight_vector, k, p)
        fitness.sort(key=lambda tup: tup[1])
        p = [fitness[j][0] for j in range(n)]
        p = crossover(p, k, n)
    fitness = compute_fitness(graph, weight_vector, k, p)
    fitness.sort(key=lambda tup: tup[1])
    p = fitness[0][0]
    return create_partitions(graph, weight_vector, k, p)
