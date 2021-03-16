def min_dist(list, index, k, n):
    difference = []
    min = 0
    for i in range(-k, k+1):
        if index + i < 0 or index + i >= n or i == 0:
            continue
        else:
            difference.append(abs(list[index + i] - list[index]))
    difference.sort()
    for i in range(k):
        min += int(difference[i])
    return min


str = []
str = input()
str = list(map(int, str.split()))
n = str[0]
k = str[1]
str = input("введите массив: ")
str = list(map(int, str.split()))
mas = []
mas = sorted(str)
for i in range(n):
    index = mas.index(str[i])
    str[i] = min_dist(mas,index,k,n)
print(*str)
