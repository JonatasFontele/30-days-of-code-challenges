def query(contacts):
    queries = 0
    name_query = input()
    while name_query != "" and queries <= 10**5:
        try:
            found_number = contacts.get(name_query, "Not found")
            if found_number != "Not found":
                print("%s=%s" % (name_query, found_number))
            else:
                print(found_number)
            name_query = input()
        except EOFError:
            break


def main():
    contacts = {}
    n = int(input())
    if 1 <= n <= 10**5:
        for i in range(n):
            name_number = input().split()
            contacts[name_number[0]] = name_number[1]
        query(contacts)

    # arr = list(map(int, input().split()))


if __name__ == "__main__":
    main()
