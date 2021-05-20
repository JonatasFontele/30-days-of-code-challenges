def bubbleSort(n, a):
    swaps_number = 0
    # Traverse through all array elements
    # range(n) also work but outer loop will repeat one time more than needed.
    for i in range(n - 1):
        # Last i elements are already in place
        # traverse the array from 0 to n-i-1
        for j in range(0, n - i - 1):
            # Swap if the element found is greater than the next element
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps_number += 1
        if swaps_number == 0:
            break
    print(f"Array is sorted in {swaps_number} swaps.")
    print("First Element:", a[0])
    print("Last Element: %d" % a[n - 1])


def main():
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    bubbleSort(n, a)


if __name__ == "__main__":
    main()
