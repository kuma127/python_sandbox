# O(n^2)の非効率なソート
def bubble_sort(list: list) -> list:
    loop_size = len(list) - 1
    for i in range(loop_size):
        for j in range(loop_size):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list

# O(n^2)の非効率なソート
# 対象がほぼ整列されていると、O(n)に近づく
def insertion_sort(a_list: list) -> list:
    for i in range(1, len(a_list)):
        value = a_list[i]
        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i - 1]
            i = i - 1
        a_list[i] = value
    return a_list

test_list = [32, 1, 9, 6]
print(bubble_sort(test_list))
print(insertion_sort(test_list))
# 一番効率的な組み込みの関数
print(sorted(test_list))