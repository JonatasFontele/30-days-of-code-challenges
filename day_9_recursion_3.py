import os


def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    # The above came in Hackerrank, write variables into your operating system as environment variables

    n = int(input())
    if 2 <= n <= 12:
        print(factorial(n))
        # result = factorial(n)

    # fptr.write(str(result) + '\n')
    # fptr.close()


if __name__ == "__main__":
    main()
