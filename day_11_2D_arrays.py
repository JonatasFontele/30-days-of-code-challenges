def find_max_hourglass(arr):
    height = 3
    width = 3
    # result = [] option
    result = -64  # Due to constraints
    # iterate through rows of arr
    for i in range(len(arr)):
        if i > height:
            break
        # iterate through columns of arr
        for j in range(len(arr[0])):
            if j > width:
                break
            sum = 0
            # iterate through rows and columns of the hourglasses
            for k in range(j, j+3):
                sum += arr[i][k]
                sum += arr[i+2][k]
            sum += arr[i + 1][j + 1]
            # result.append(sum) option
            if result < sum:
                result = sum
    # return max(result) option
    return result


def main():
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(find_max_hourglass(arr))


if __name__ == "__main__":
    main()
