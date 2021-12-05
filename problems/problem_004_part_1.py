from typing import List

"""

https://adventofcode.com/2021/day/4

--- Day 4: Giant Squid ---
You're already almost 1.5km (almost a mile) below the surface of the ocean, already so deep that you can't see any sunlight. What you can see, however, is a giant squid that has attached itself to the outside of your submarine.

Maybe it wants to play bingo?

Bingo is played on a set of boards each consisting of a 5x5 grid of numbers. Numbers are chosen at random, and the chosen number is marked on all boards on which it appears. (Numbers may not appear on all boards.) If all numbers in any row or any column of a board are marked, that board wins. (Diagonals don't count.)

The submarine has a bingo subsystem to help passengers (currently, you and the giant squid) pass the time. It automatically generates a random order in which to draw numbers and a random set of boards (your puzzle input). For example:

7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
After the first five numbers are drawn (7, 4, 9, 5, and 11), there are no winners, but the boards are marked as follows (shown here adjacent to each other to save space):

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
After the next six numbers are drawn (17, 23, 2, 0, 14, and 21), there are still no winners:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
Finally, 24 is drawn:

22 13 17 11  0         3 15  0  2 22        14 21 17 24  4
 8  2 23  4 24         9 18 13 17  5        10 16 15  9 19
21  9 14 16  7        19  8  7 25 23        18  8 23 26 20
 6 10  3 18  5        20 11 10 24  4        22 11 13  6  5
 1 12 20 15 19        14 21 16 12  6         2  0 12  3  7
At this point, the third board wins because it has at least one complete row or column of marked numbers (in this case, the entire top row is marked: 14 21 17 24 4).

The score of the winning board can now be calculated. Start by finding the sum of all unmarked numbers on that board; in this case, the sum is 188. Then, multiply that sum by the number that was just called when the board won, 24, to get the final score, 188 * 24 = 4512.

To guarantee victory against the giant squid, figure out which board will win first. What will your final score be if you choose that board?
"""


class Board:
    SIZE = 5

    def __init__(self, numbers: List[int]):
        assert len(numbers) == self.SIZE ** 2

        self.state = [[None for _ in range(5)] for _ in range(5)]
        self.chosen_numbers = []

        for i, number in enumerate(numbers):
            row = i // 5
            col = i - row * 5
            self.state[row][col] = (number, False)

    def choose_number(self, number: int):

        self.chosen_numbers.append(number)

        for row in range(self.SIZE):
            for col in range(self.SIZE):

                if self._get_number(row, col) == number:
                    self._set_is_chosen(row, col)

    def is_win(self) -> bool:

        for i in range(self.SIZE):

            if (all((self._get_is_chosen(i, col) for col in range(self.SIZE)))
                    or all((self._get_is_chosen(row, i) for row in range(self.SIZE)))):
                return True

        return False

    def get_score(self) -> bool:

        sum_unchosen = 0
        last_chosen_number = 0

        if len(self.chosen_numbers) > 0:
            last_chosen_number = self.chosen_numbers[-1]

        for row in range(self.SIZE):
            for col in range(self.SIZE):

                if not self._get_is_chosen(row, col):
                    sum_unchosen += self._get_number(row, col)

        return sum_unchosen * last_chosen_number

    def _set_is_chosen(self, row: int, col: int):
        self.state[row][col] = self.state[row][col][0], True

    def _get_is_chosen(self, row: int, col: int) -> bool:
        return self.state[row][col][1]

    def _get_number(self, row: int, col: int) -> int:
        return self.state[row][col][0]

    def __repr__(self):

        representation = ""

        for row in self.state:
            for number, is_chosen in row:
                inidcator = "(x)" if is_chosen else "( )"
                representation += f"{number: >3} {inidcator: <3}"
            representation += "\n"

        return representation


def solve(input: List[str]):
    chosen_numbers = map(int, input[0].split(","))

    boards = []
    numbers = []
    for i, sequence in enumerate(input[1:]):

        numbers.extend(map(int, sequence.split()))

        if i > 0 and (i + 1) % 5 == 0:
            new_board = Board(numbers)
            boards.append(new_board)
            numbers = []

    for number in chosen_numbers:
        for board in boards:
            board.choose_number(number)
            if board.is_win():
                return board.get_score()

    return 0
