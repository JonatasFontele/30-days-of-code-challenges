def query(contacts):
    queries = 0
    name_query = input()
    # Read unknown number of lines of queries (name)
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
    n = int(input())  # Number of entries
    if 1 <= n <= 10**5:
        for i in range(n):
            name_number = input().split()  # name number (per line)
            contacts[name_number[0]] = name_number[1]  # {name: number}
        query(contacts)


if __name__ == "__main__":
    main()
