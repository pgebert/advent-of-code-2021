from problems import problem_003_part_2


def test_problem_003_part_2_example():

    input = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""

    input = input.splitlines()

    result = problem_003_part_2.solve(input)
    assert 230 == result

def test_problem_003_part_2_problem():

    input = []

    with open("C:\\Users\\pgebert\\Projekte\\private\\advent-of-code-2021\\data\\problem_003_part_2_input.txt") as file:
        lines = file.readlines()
        input = [line.rstrip() for line in lines]

    result = problem_003_part_2.solve(input)
    assert 4406844 == result

