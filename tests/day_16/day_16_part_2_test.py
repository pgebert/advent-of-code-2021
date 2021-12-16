from problems.day_16 import day_16_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_day_16_part_2_example():
    example = """
        110100101111111000101000
    """

    input = read_lines_from_comment(example)
    result = day_16_part_2.solve(input)

    assert 6 == result


def test_day_16_part_2_problem():
    input = read_lines_from_file(".\\data\\day_16\\day_16_input.txt")
    result = day_16_part_2.solve(input)

    assert 2935 == result
