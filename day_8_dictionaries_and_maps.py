def query(contacts):
    queries = 0
    name_query = input()
    # Read unknown number of lines of queries (name)
    while name_query != "" and queries <= 100000:
        try:
            found_number = contacts.get(name_query, "Not found")
            if found_number != "Not found":
                print(f"{name_query}={found_number}")
            else:
                print(found_number)
            name_query = input()
        except EOFError:
            break


def main():
    n = int(input())  # Number of entries
    if 1 <= n <= 100000:
        # for i in range(n):
        #   name_number = input().split()               name number (per line)
        #   contacts[name_number[0]] = name_number[1]   {name: number}

        contacts = dict([input().split() for _ in range(n)])  # Pythonic way
        query(contacts)


if __name__ == "__main__":
    main()
