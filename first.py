
N = int(input())
input_str = map(int, input().split())
input_str = list(input_str)
check = True
if input_str[-1] == max(input_str):
    for i in range(1, N):
        if input_str[i-1] <= input_str[i]:
            input_str[i-1] = input_str[i] - input_str[i-1]
        else:
            check = False
            break
else:
    check = False
input_str[-1] = 0
if check == True:
    N = sum(input_str)
else:
    N = -1
print(N)
