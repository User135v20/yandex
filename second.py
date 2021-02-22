
def pers(X):
    pers = []
    for _ in range(X):
        pers.append(True)
    return pers

def True_False_place(place ):
    row = []
    for i in place:
        if i == '.':
            row.append(False)
        elif i == '#':
            row.append(True)
    return row

def half_row_add(row, window, right, pers):
    while pers < 3:
        if (window == True and right == False) or (window == False and right == True):
            row.append(False)
            pers = pers + 1
        elif (window == True and right == True) or (window == False and right == False):
            row.insert(0, False)
            pers = pers +1
    return row

def row_add(row, right):
    for _ in range(3):
        if right == True:
            row.insert(0, False)
        else:
            row.append(False)
    return row

def upgrate_place(places: list, places_Bool):
    j = 0
    print(places_Bool)
    print('места : \n', places)
    for i in range(6):

        if i == 3:
            j = j + 1

        if places_Bool[i] == True:
            places[j] = "X"
       # print(places[j], ' / ', places_Bool[i])
        j = j + 1
    return places



N = int(input('input N: '))
places = []
request = []
row = []
places_Bool = []

for i in range(N):
    places.append([ j for j in input()])


M = int(input('input M: '))
for i in range(M):
    request.append(input().split(' '))

for i in range(N):
    places_Bool.append(True_False_place(places[i]))
    print(places_Bool)

for i in range(M):
    persons = int(request[i][0])

    row.clear()
    sum = False

    if request[i][1] == "right":
        right = True
    elif request[i][1] == "left":
        right = False
    if request[i][2] == "window":
        window = True
    elif request[i][2] == "aisle":
        window = False
    row = pers(persons)
    half_row_add(row, window, right, persons)
    row = row_add(row, right)

    print('требуется: ', row)

    for z in range(N):
        for k in range(6):
            sum = sum + places_Bool[z][k]*row[k]
        print(sum)
        if sum == 0:
            print(type(places))
            places[z] = upgrate_place(places[z], row)



for z in range(N):
    print("".join(places[z]))


# for z in range(N):
#    print(places[z])