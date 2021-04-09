def reverse(arr):
    print(' '.join(map(str, arr[::-1])))


def validate(n, arr):
    constraints = True
    for number in arr:
        if not (number in range(1, 10001)):
            constraints = False
            break
    if constraints and 1 <= n <= 1000:
        reverse(arr)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    validate(n, arr)


if __name__ == "__main__":
    main()
