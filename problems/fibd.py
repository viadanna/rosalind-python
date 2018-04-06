'''
Mortal Fibonacci Rabbits
http://rosalind.info/problems/fibd/

Problem

Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence
Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed
that each pair of rabbits reaches maturity in one month and produces a single
pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic
programming solution in the case that all rabbits die out after a fixed number
of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live
for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th
month if all rabbits live for m months.

Sample Dataset
6 3

Sample Output
4
'''


def run_fibd(data):
    ''' Dynamic approach for rabbits '''
    n, m = [int(i) for i in data.split()]
    # Initialize monthly counter
    p = [{
        'mature': 0,
        'born': 1,
        'dead': 0,
    }]
    for i in range(1, n):
        # Mature rabbits procreate
        # Pups become mature
        new = {
            'mature': p[-1]['born'] + p[-1]['mature'],
            'born': p[-1]['mature']
        }
        dying_month = i - m
        if dying_month >= 0:
            # Some rabbits die
            new['mature'] -= p[dying_month]['born']
        p.append(new)
    return p[-1]['born'] + p[-1]['mature']


def fibd(data):
    ''' Naive approach for rabbits '''
    n, m = [int(i) for i in data.split()]
    # Initialize monthly counter
    p = [[0]]
    for i in range(1, n):
        print(i)
        generation = []
        for rabbit in p[i - 1]:
            if rabbit > 0:
                # Rabbit procreates
                generation.append(0)
            if rabbit + 1 < m:
                # Rabbit dies
                generation.append(rabbit + 1)
        p.append(generation)
    print(p)
    return sum(1 for _ in p[-1])
