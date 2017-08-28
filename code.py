import itertools
import sys

template = """\
 |{a1} |{a2}
-+---+--
{b1}|{c11}|{c12}
-+---+--
{b2}|{c21}|{c22}\
"""

genotype_1, genotype_2 = map(sorted, sys.argv[1:])
children = map("".join, map(sorted, itertools.product(genotype_1, genotype_2)))

print(template.format(**dict(zip("a1 a2 b1 b2".split(), [*genotype_1, *genotype_2])),
                      **dict(zip("c11 c21 c12 c22".split(), children))))
