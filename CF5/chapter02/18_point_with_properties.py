class Point:
    __count = 0

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y
        Point.__count += 1

    def __str__(self):
        return f'({self.__x}, {self.__y})'

    @classmethod
    def get_count(cls):
        return cls.__count

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if x < 0:
            self.__x = 0
        else:
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        self.__y = y


def main():
    p1 = Point(10, 20)
    p2 = Point()
    print(Point.get_count())
    print(p1)
    print("--------")
    p1.x = -100
    p1.y = 200
    print(p1)


if __name__ == '__main__':
    main()
