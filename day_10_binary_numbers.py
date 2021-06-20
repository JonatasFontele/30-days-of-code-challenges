def longest_sequence_count(representation):
    longest_sequence = 0
    current_sequence = 1
    for i in range(1, len(representation)):
        if representation[i] == representation[i - 1]:
            # If the current number is the same as the previous number, the sequence size increases
            current_sequence += 1
        else:
            # If the number is different, we start a new sequence
            current_sequence = 1
        if current_sequence > longest_sequence:
            # If the size of the sequence is larger than before, it updates the size of the largest sequence.
            longest_sequence = current_sequence
    return longest_sequence


def convert(n, base):
    representation = ""
    while n != 0:
        representation += str(n % base)
        n = int(n / base)
    # return representation also works, but I wanted to keep the binary conversion correctly
    return representation[::-1]
    # representation = bin(n)
    # return representation[2::]


def main():
    n = int(input())
    base = 2  # Base to be converted
    if 1 <= n <= 10**6:
        print(longest_sequence_count(convert(n, base)))


if __name__ == "__main__":
    main()
