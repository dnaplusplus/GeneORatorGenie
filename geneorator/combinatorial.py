'''
DNA++ (c) DNA++ 2017

All rights reserved.

@author: neilswainston
'''
import itertools
import sys


def combine(oligos, n_mutated, n_blocks):
    '''Design combinatorial assembly.'''
    designs = []

    len_block = len(oligos) / n_blocks

    # Get combinations:
    combis = itertools.combinations(oligos, n_mutated)

    for combi in combis:
        design = list(oligos)

        for var in combi:
            design[design.index(var)] = var + 'm'

        designs.append([design[i:i + len_block]
                        for i in xrange(0, len(design), len_block)])

    return designs


def main(args):
    '''main method.'''
    oligos = [str(val) for val in range(1, 28)]

    for design in combine(oligos, int(args[0]), int(args[1])):
        print design


if __name__ == '__main__':
    main(sys.argv[1:])
