# Is there a late fee
def fine(returned_date, due_date):
    # Using list
    # Year
    if returned_date[2] > due_date[2]:
        return 10000
    # If the book is returned in the previous year, returns 0
    elif returned_date[2] == due_date[2]:
        # Month
        if returned_date[1] > due_date[1]:
            return 500 * (returned_date[1] - due_date[1])
        # And if the book is returned in the previous month of the same year, returns 0
        elif returned_date[1] == due_date[1]:
            # Day
            if returned_date[0] > due_date[0]:
                return 15 * (returned_date[0] - due_date[0])
    return 0

    # Could use tuples
    
    # returned_day, returned_month, returned_year = returned_date
    # due_day, due_moth, due_year = due_date
    # if (returned_day, returned_month, returned_year) <= (due_day, due_moth, due_year):
    #     return 0
    # elif (returned_year, returned_month) == (due_year, due_moth):
    #     return 15 * (returned_day - due_day)
    # elif returned_year == due_year:
    #     return 500 * (returned_month - due_moth)
    # else:
    #     return 10000


def main():
    returned_date = list(map(int, input().split()))
    due_date = list(map(int, input().split()))
    print(fine(returned_date, due_date))


if __name__ == "__main__":
    main()
