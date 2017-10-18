'''
DNA++ (c) DNA++ 2017

All rights reserved.

@author: neilswainston
'''
import itertools
import sys


def combine(oligos, n_mutated=0, mutant_oligos=None, n_blocks=1):
    '''Design combinatorial assembly.'''

    # Assertion sanity checks:
    assert len(oligos) % 2 == 0
    assert len(oligos) / n_blocks >= 2
    assert mutant_oligos if n_mutated > 0 else True

    designs = []

    # Get combinations:
    combis = itertools.combinations(mutant_oligos, n_mutated)

    for combi in combis:
        design = list(oligos)

        for var in combi:
            design[design.index(var[0])] = var[1]

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


def main(args):
    '''main method.'''
    oligos = [str(val) for val in range(1, 29)]
    mutant_oligos = ((oligo, oligo + 'm') for oligo in oligos)

    for design in combine(oligos, int(args[0]), mutant_oligos, int(args[1])):
        print design


if __name__ == '__main__':
    main(sys.argv[1:])
