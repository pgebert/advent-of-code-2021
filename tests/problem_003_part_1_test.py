from problems import problem_003_part_1


def test_problem_003_part_1_example():

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

    result = problem_003_part_1.solve(input)
    assert 198 == result

def test_problem_003_part_1_problem():

    input = []

    with open("C:\\Users\\pgebert\\Projekte\\private\\advent-of-code-2021\\data\\problem_003_part_1_input.txt") as file:
        lines = file.readlines()
        input = [line.rstrip() for line in lines]

    result = problem_003_part_1.solve(input)
    assert 3687446 == result

