def bitwise_and(n, k):
    max_a_and_b = 0
    for i in range(1, n+1):
        for j in range(1, i):
            if max_a_and_b < (i & j) < k:
                max_a_and_b = i & j
            if max_a_and_b == k - 1:
                return max_a_and_b
    return max_a_and_b


def main():
    t = int(input().strip())
    for t_itr in range(t):
        first_multiple_input = input().split()
        count = int(first_multiple_input[0])
        lim = int(first_multiple_input[1])
        print(bitwise_and(count, lim))


if __name__ == "__main__":
    main()
