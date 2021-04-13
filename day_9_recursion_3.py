def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    n = int(input())
    if 2 <= n <= 12:
        print(factorial(n))


if __name__ == "__main__":
    main()
