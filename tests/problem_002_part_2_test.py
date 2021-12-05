from problems import problem_002_part_2
from utils import read_lines_from_comment, read_lines_from_file


def test_problem_002_part_2_example():
    example = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    """

    input = read_lines_from_comment(example)
    result = problem_002_part_2.solve(input)

    assert 900 == result


def test_problem_001_problem():
    input = read_lines_from_file(".\\data\\problem_002_part_2_input.txt")
    result = problem_002_part_2.solve(input)

    assert 1781819478 == result
