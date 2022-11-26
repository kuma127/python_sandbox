from bisect import bisect_left

def linear_search(list: list, n: int) -> bool:
    for i in list:
        if i == n:
            return True
    return False

def binary_search(list: list, n: int) -> bool:
    first = 0
    last = len(list) - 1
    while last >= first:
        mid = (first + last) // 2
        if list[mid] == n:
            return True
        else:
            if n < list[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return False

def bisect_search(list: list, n: int) -> bool:
    index = bisect_left(list, n)
    if index <= len(list) and list[index] == n:
        return True
    return False

def main():
    test_list = [1, 3, 21, 37, 57, 79, 94]
    # print(linear_search(test_list, 94))
    # print(94 in test_list)
    # print('a' in 'apple')
    # print(binary_search(test_list, 93))
    print(bisect_search(test_list, 93))

if __name__ == "__main__":
    main()
