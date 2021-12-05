from problems import problem_001
from utils import read_lines_from_comment, read_lines_from_file


def test_problem_001_example():
    example = """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
    """

    input = read_lines_from_comment(example)
    result = problem_001.solve(input)

    assert 7 == result


def test_problem_001_problem():
    input = read_lines_from_file(".\\data\\problem_001_part_1_input.txt")
    result = problem_001.solve(input)

    assert 1532 == result
