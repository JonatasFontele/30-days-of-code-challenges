from math import sqrt


def is_prime(n):
    # Corner case
    if n <= 1:
        return "Not prime"
    # O(sqrt(n)) instead of brute-force 2 to n-1
    # because a larger factor of n must be a multiple of a smaller factor that has been already checked
    for i in range(2, int(sqrt(n) + 1)):
        if n % i == 0:
            return "Not prime"
    return "Prime"


def main():
    T = int(input())
    for _ in range(T):
        print(is_prime(int(input())))


if __name__ == "__main__":
    main()
