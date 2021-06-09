def first_ten_multiples(n):
    return [print(f"{n} x {multiple} = {n * multiple}") for multiple in range(1, 11)]


def main():
    n = int(input())
    if 2 <= n <= 20:
        first_ten_multiples(n)


if __name__ == "__main__":
    main()
