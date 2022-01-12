from modules.create_partitions import create_partitions, weight_part


def compute_fitness(graph, weight, k, permutations):
    fitness = []
    for permutation in permutations:
        parts = create_partitions(graph, weight, k, permutation)
        wp = [weight_part(part, weight) for part in parts]
        fitness.append((permutation, max(wp) * k / graph.__len__()))
    return fitness
