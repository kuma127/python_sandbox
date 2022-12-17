import time


def move_zeros(target: list) -> list:
    num_list = []
    zero_list = []
    for num in target:
        if num > 0:
            num_list.append(num)
        else:
            zero_list.append(0)
    return num_list + zero_list


def move_zeros_sample(target: list) -> list:
    zero_index = 0
    for index, n in enumerate(target):
        if n != 0:
            target[zero_index] = n
            if zero_index != index:
                target[index] = 0
            zero_index += 1
    return target


# challenge
def divide_num_array(target: list) -> tuple[list, list]:
    even_array = []
    odd_array = []
    for num in target:
        if num % 2 == 0:
            even_array.append(num)
        else:
            odd_array.append(num)
    return even_array, odd_array


def main():
    start = time.time()
    list_test = [8, 0, 0, 34, 0, 22]
    # result = move_zeros(list_test)
    result = move_zeros_sample(list_test)
    end = time.time()
    print(result)
    print(end - start)


def main_challenge():
    list_test = [2, 36, 41, 78, 97, 55, 4]
    even, odd = divide_num_array(list_test)
    print(even)
    print(odd)


if __name__ == "__main__":
    # main()
    main_challenge()
