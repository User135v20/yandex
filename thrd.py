
def my_sort(array) -> list:
    if len(array) == 1:
        return array
    if len(array) == 2:
        if array[0] < array[1]:
            return array
        else:
            return array[::-1]
    median = len(array)-1
    array[median], array[len(array)//2] = array[len(array)//2], array[median]
    max_ind = 0
    min_ind = median - 1
    while min_ind > max_ind:
        while array[max_ind] <= array[median] and max_ind < median:
            max_ind += 1
        while array[min_ind] > array[median] and min_ind > 0:
            min_ind -= 1
        if min_ind > max_ind:
            array[min_ind], array[max_ind] = array[max_ind], array[min_ind]
    array[median], array[max_ind] = array[max_ind], array[median]
    median = max_ind
    array1 = []
    array2 = []
    if median > 0:
        array1 = my_sort(array[:median])
    if median+1 < len(array):
        array2 = my_sort(array[median+1:])
    return array1+[array[median]]+array2


def min_dist(_list, index, k, n):
    difference = []
    min = 0

    start = index - k if index - k > 0 else 0
    fin = index + k if index + k <= n - 1 else n - 1

    for i in range(start, fin + 1):
        if i == index:
            continue
        difference.append(abs(_list[i] - _list[index]))
    difference.sort()

    for i in range(k):
        min += (difference[i])
    return min


def main():
    result = []
    dict_result = {}
    str = input()
    str = list(map(int, str.split()))
    n = str[0]
    k = str[1]
    str = input()
    str = list(map(int, str.split()))
    mas = my_sort(str.copy())

    for i in range(n):
        index = mas.index(str[i])
        if str[i] in dict_result:
            result.append(dict_result[str[i]])
        else:
            res = min_dist(mas, index, k, n)
            result.append(res)
            dict_result[str[i]] = res
    print(*result)


if __name__ == '__main__':
    main()