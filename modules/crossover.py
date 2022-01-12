import random

from modules.odpx import odpx


def crossover(permutations, k, n):
    offsprings = []
    for i in range(0, int(n / 2)):
        r1 = random.randrange(0, n)
        r2 = random.randrange(0, n)
        q1, q2, q3, q4 = odpx(list(permutations[r1]), list(permutations[r2]), k, n)
        offsprings.append(tuple(q1))
        offsprings.append(tuple(q2))
        offsprings.append(tuple(q3))
        offsprings.append(tuple(q4))
    return offsprings
