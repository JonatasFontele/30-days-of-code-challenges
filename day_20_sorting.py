def bubbleSort(n, a):
    # Traverse through all array elements
    # range(n) also work but outer loop will repeat one time more than needed.
    for i in range(n - 1):
        # Last i elements are already in place
        # traverse the array from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


def main():
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    bubbleSort(n, a)


if __name__ == "__main__":
    main()
