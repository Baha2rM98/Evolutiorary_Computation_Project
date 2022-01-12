import random


def odpx(parent_1, parent_2, k, n):
    interval = [val for val in parent_1[:k] if val in parent_2[:k]]
    for i in range(0, k):
        if not (parent_1[i] in interval):
            j = random.randrange(k, n)
            temp = parent_1[i]
            parent_1[i] = parent_1[j]
            parent_1[j] = temp
    m = parent_1[:k]
    for i in range(0, k):
        if not (parent_2[i] in interval):
            j = random.randrange(k, n)
            while parent_2[j] in m:
                j = random.randrange(k, n)
            temp = parent_2[i]
            parent_2[i] = parent_2[j]
            parent_2[j] = temp
    q1 = parent_1[:k]
    q2 = parent_2[:k]
    q3 = parent_1[:k]
    q4 = parent_2[:k]
    l1 = []
    l2 = []
    for i in range(0, 2 * (n - k)):
        if (i % 2 == 1) is True:
            l1.append(parent_2[int(k + (i - 1) / 2)])
            l2.append(parent_1[int(k + (i - 1) / 2)])
        else:
            l1.append(parent_1[int(k + i / 2)])
            l2.append(parent_2[int(k + i / 2)])
    for i in range(0, 2 * (n - k)):
        if not (l1[i] in q1):
            q1.append(l1[i])
        else:
            q2.append(l1[i])
        if not (l2[i] in q4):
            q4.append(l2[i])
        else:
            q3.append(l2[i])
    return q1, q2, q3, q4
