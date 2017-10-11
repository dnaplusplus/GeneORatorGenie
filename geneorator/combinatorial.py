'''
DNA++ (c) DNA++ 2017

All rights reserved.

@author: neilswainston
'''
import itertools
import sys


def combine(oligos, n_mutated=0, n_blocks=1):
    '''Design combinatorial assembly.'''

    # Assertion sanity checks:
    assert(len(oligos) % 2 == 0)
    assert(len(oligos) / n_blocks >= 2)

    designs = []

    # Get combinations:
    combis = itertools.combinations(oligos, n_mutated)

    for combi in combis:
        design = list(oligos)

        for var in combi:
            design[design.index(var)] = var + 'm'

        block_lengths = [0] * n_blocks

        for idx in itertools.cycle(range(0, n_blocks)):
            block_lengths[idx] = block_lengths[idx] + 2

            if sum(block_lengths) == len(design):
                break

        idx = 0
        blocks = []

        for val in block_lengths:
            blocks.append(design[idx: idx + val])
            idx = idx + val

        designs.append(blocks)

    return designs


def _pairwise(iterable):
    '''s -> (s0,s1), (s1,s2), (s2, s3), ...'''
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def main(args):
    '''main method.'''
    oligos = [str(val) for val in range(1, 7)]

    for design in combine(oligos, int(args[0]), int(args[1])):
        print design


if __name__ == '__main__':
    main(sys.argv[1:])
