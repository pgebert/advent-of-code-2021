from itertools import permutations
from typing import List

from .number import Number

"""

https://adventofcode.com/2021/day/18


"""


def solve(input: List[str]):
    max_result = 0

    for a, b in permutations(input, 2):

        result = (Number(eval(a)) + Number(eval(b))).magnitude()
        if result > max_result:
            max_result = result

    return max_result
