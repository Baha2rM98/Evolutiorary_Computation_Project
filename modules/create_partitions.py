def create_partitions(graph, weights, k, permutations):
    partitions = []
    free = []
    n = len(permutations)
    for i in range(k):
        partitions.append([permutations[i]])
        free.append(False)
    for i in range(k, n):
        free.append(True)
    some_free = True
    while some_free:
        some_free = False
        for i in range(k, n):
            if free[i]:
                smallest = float('inf')
                index = -1
                for m in range(k):
                    for j in range(n):
                        if graph[permutations[i]][j] > 0 and j in partitions[m]:
                            if weight_part(partitions[m], weights) < smallest:
                                smallest = weight_part(partitions[m], weights)
                                index = m
                if index == -1:
                    some_free = True
                else:
                    partitions[index].append(permutations[i])
                    free[i] = False
    return partitions


def weight_part(part, weights):
    w = 0
    for i in part:
        w += weights[i]
    return w
