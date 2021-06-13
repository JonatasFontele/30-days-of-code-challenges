# Separates even index to left and odd index to right
def even_odd_index(s):
    even = ""
    odd = ""
    for i in range(len(s)):
        # string.index(value, start, end)
        if s.index(s[i], i, len(s)) % 2:
            odd = odd + s[i]
        else:
            even = even + s[i]
    print(f"{even} {odd}")


def main():
    t = int(input())
    for i in range(t):
        s = input()
        if 1 <= t <= 10 and 2 <= len(s) <= 10000:
            even_odd_index(s)


if __name__ == "__main__":
    main()
