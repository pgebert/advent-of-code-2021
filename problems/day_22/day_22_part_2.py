from __future__ import annotations

from dataclasses import dataclass
from typing import List, Iterator

"""

https://adventofcode.com/2021/day/22



"""


def parse_input(line: str):
    mode, rest = line.split(" ")
    x_limits, y_limits, z_limits = rest.split(",")

    x_lower, x_upper = map(int, x_limits[2:].split(".."))
    y_lower, y_upper = map(int, y_limits[2:].split(".."))
    z_lower, z_upper = map(int, z_limits[2:].split(".."))

    mode = True if mode == "on" else False

    start = Point(x_lower, y_lower, z_lower)
    end = Point(x_upper + 1, y_upper + 1, z_upper + 1)

    return mode, start, end


@dataclass
class Point:
    x: int
    y: int
    z: int


@dataclass
class Cuboid:
    start: Point
    end: Point

    def count(self) -> int:
        return (self.end.x - self.start.x) * (self.end.y - self.start.y) * (self.end.z - self.start.z)

    def subtract(self, other: Cuboid) -> Iterator[Cuboid]:
        # no intersection
        if not (other.start.x < self.end.x and other.end.x > self.start.x
                and other.start.y < self.end.y and other.end.y > self.start.y
                and other.start.z < self.end.z and other.end.z > self.start.z):
            yield self
        # intersection
        else:
            intersection = Cuboid(
                Point(
                    min(max(other.start.x, self.start.x), self.end.x),
                    min(max(other.start.y, self.start.y), self.end.y),
                    min(max(other.start.z, self.start.z), self.end.z)
                ),
                Point(
                    min(max(other.end.x, self.start.x), self.end.x),
                    min(max(other.end.y, self.start.y), self.end.y),
                    min(max(other.end.z, self.start.z), self.end.z)
                )
            )

            yield Cuboid(
                Point(self.start.x, self.start.y, self.start.z),
                Point(intersection.start.x, self.end.y, self.end.z)
            )
            yield Cuboid(
                Point(intersection.end.x, self.start.y, self.start.z),
                Point(self.end.x, self.end.y, self.end.z)
            )
            yield Cuboid(
                Point(intersection.start.x, self.start.y, self.start.z),
                Point(intersection.end.x, intersection.start.y, self.end.z)
            )
            yield Cuboid(
                Point(intersection.start.x, intersection.end.y, self.start.z),
                Point(intersection.end.x, self.end.y, self.end.z)
            )
            yield Cuboid(
                Point(intersection.start.x, intersection.start.y, self.start.z),
                Point(intersection.end.x, intersection.end.y, intersection.start.z)
            )
            yield Cuboid(
                Point(intersection.start.x, intersection.start.y, intersection.end.z),
                Point(intersection.end.x, intersection.end.y, self.end.z)
            )


def solve(input: List[str]):
    cuboids = []
    for line in input:
        active, start, end = parse_input(line)

        cuboid = Cuboid(start, end)

        cuboids = [child for other in cuboids for child in other.subtract(cuboid) if child.count() > 0]
        if active:
            cuboids.append(cuboid)

    return sum(x.count() for x in cuboids)
