def list_alphabetically_order(names):
    names = sorted(names)
    for name in names:
        print(name)


def main():
    names = []
    N = int(input().strip())
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()
        first_name = first_multiple_input[0]
        email_id = first_multiple_input[1]
        if '@gmail.com' in email_id:
            names.append(first_name)
    list_alphabetically_order(names)


if __name__ == "__main__":
    main()
