from problems import problem_001


def test_problem_001_example():

    input = """
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

    input = input.split()

    result = problem_001.solve(input)
    assert 7 == result

def test_problem_001_problem():

    input = []

    with open("C:\\Users\\pgebert\\Projekte\\private\\advent-of-code-2021\\data\\problem_001_input.txt") as file:
        lines = file.readlines()
        input = [line.rstrip() for line in lines]

    print(input)


    result = problem_001.solve(input)
    assert 1532 == result

