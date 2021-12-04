from problems import problem_002_part_2


def test_problem_002_part_2_example():

    input = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

    input = input.splitlines()

    result = problem_002_part_2.solve(input)
    assert 900 == result

def test_problem_001_problem():

    input = []

    with open("C:\\Users\\pgebert\\Projekte\\private\\advent-of-code-2021\\data\\problem_002_part_2_input.txt") as file:
        lines = file.readlines()
        input = [line.rstrip() for line in lines]

    result = problem_002_part_1.solve(input)
    assert 1781819478 == result

