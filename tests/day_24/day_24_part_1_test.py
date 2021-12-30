from problems.day_24 import day_24_part_1
from utils import read_lines_from_comment, read_lines_from_file


def test_day_24_part_1_example_negation():
    example = """
        inp x
        mul x -1
    """

    program = read_lines_from_comment(example)
    variables = day_24_part_1.solve(program, [1])

    assert -1 == variables.get("x")


def test_day_24_part_1_example_three_times():
    example = """
        inp z
        inp x
        mul z 3
        eql z x
    """

    program = read_lines_from_comment(example)

    assert 1 == day_24_part_1.solve(program, [1, 3]).get("z")
    assert 0 == day_24_part_1.solve(program, [1, 4]).get("z")


def test_day_24_part_1_example_binary():
    example = """
        inp w
        add z w
        mod z 2
        div w 2
        add y w
        mod y 2
        div w 2
        add x w
        mod x 2
        div w 2
        mod w 2
    """

    program = read_lines_from_comment(example)
    variables = day_24_part_1.solve(program, [14])

    assert 1 == variables.get("w")
    assert 1 == variables.get("x")
    assert 1 == variables.get("y")
    assert 0 == variables.get("z")


def test_day_24_part_1_problem():
    program = read_lines_from_file(".\\data\\day_24\\day_24_input.txt")
    result = day_24_part_1.monad(program)

    assert 4968 == result
