def first_ten_multiples(n):
    for multiple in range(1, 11):
        print("{} x {} = {}".format(n, multiple, n * multiple))


def main():
    n = int(input())
    if 2 <= n <= 20:
        first_ten_multiples(n)


if __name__ == "__main__":
    main()
