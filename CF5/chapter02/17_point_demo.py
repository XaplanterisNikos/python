class Point:
    def __init__(self, x, y):
        # self.__x = x # Name Mangling!
        # self.__y = y

        self._x = x
        self._y = y

    def __str__(self):
        return f"({self._x}, {self._y})"

    def distance_to(self, other):
        return ((self._x - other._x) ** 2 + (self._y - other._y) ** 2) ** 0.5


def main():
    p1 = Point(0, 3)
    p2 = Point(4, 0)

    # print("p1.x = ", p1._Point__x)
    # print("p1.y = ", p1._Point__y)
    print(f"p1: {p1}")
    print(f"p2: {p2}")

    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
