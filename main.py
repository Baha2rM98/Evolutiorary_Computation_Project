from modules.evolutionary_algorithm import run_algorithm
import os


def normalize_partitions(previous_partitions):
    normalized_partitions = []
    for i in range(previous_partitions.__len__()):
        normalized_partitions.append([int(i) + 1 for i in previous_partitions[i]])
    return normalized_partitions


if __name__ == '__main__':
    while True:
        print()
        print('-------------------Graph Partitioning Using An Evolutionary Algorithm with ODPX-----------------------')
        print('Please enter the number of partitions or enter q to exit: ')
        k = input()
        if not k.isnumeric():
            exit(0)
        k = int(k)
        print('Please enter the number of generations:')
        MAX_GEN = int(input())
        graph_file_path = str(os.getcwd()) + '\\Graph.txt'
        weight_file_path = str(os.getcwd()) + '\\VertexWeights.txt'
        print('Reading graph from [' + graph_file_path + ']...')
        # Example graph in page 17-5
        graph = []
        with open(graph_file_path, 'r') as data_file:
            for line in data_file:
                data = line.split()
                graph.append([int(i) for i in data])
        print('Reading vertex weight from [' + weight_file_path + ']...')
        weight_vector = [float(i) for i in open(weight_file_path, 'r')]
        print('Running algorithm...')
        partitions = normalize_partitions(run_algorithm(graph, weight_vector, k, MAX_GEN))
        print('K=' + str(k) + ' And ' + 'Generations=' + str(MAX_GEN) + ' :Partitions -> ' + str(partitions))
        print()
