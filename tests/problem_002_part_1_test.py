from problems import problem_002_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_problem_002_part_1_example():
    example = """
        forward 5
        down 5
        forward 8
        up 3
        down 8
        forward 2
    """

    input = read_lines_from_comment(example)
    result = problem_002_part_1.solve(input)

    assert 150 == result


def test_problem_002_part_1_problem():
    input = read_lines_from_file(".\\data\\problem_002_part_1_input.txt")
    result = problem_002_part_1.solve(input)

    assert 1635930 == result
