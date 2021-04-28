class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))

        # Nested and not recommended way
        # for a in self.__elements:
        #    for b in self.__elements:
        #        if abs(a - b) > self.maximumDifference:
        #            self.maximumDifference = abs(a - b)


def main():
    _ = input()
    a = [int(e) for e in input().split(' ')]
    d = Difference(a)
    d.computeDifference()
    print(d.maximumDifference)


if __name__ == "__main__":
    main()
