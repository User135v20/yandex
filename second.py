def pers(X):
    pers = []
    for _ in range(X):
        pers.append(True)
    return pers


def True_False_place(place):
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


def place_inform(places_bool, number_row):
    symbol = ['A', 'B', 'C', 'D', 'E', 'F']
    message = ''
    for i in range(6):
        if places_bool[i] == True:
            if message:
                message += ' '
            message += f"{number_row + 1}{symbol[i]}"
    if message:
        print(f'Passengers can take seats: {message}')


def upgrate_place(places: list, places_Bool):
    j = 0
    for i in range(6):
        if i == 3:
            j = j + 1
        if places_Bool[i] == True:
            places[j] = "X"
        j = j + 1
    return places


if __name__ == "__main__":

    N = int(input('input N: '))
    places = []
    request = []
    row = []
    places_Bool = []
    place_information = []

    for i in range(N):
        places.append([j for j in input()])

    M = int(input('input M: '))
    for i in range(M):
        request.append(input().split(' '))

    for i in range(M):
        places_Bool.clear()
        row.clear()
        sum = False
        flag = True

        for num in range(N):
            places_Bool.append(True_False_place(places[num]))
        persons = int(request[i][0])

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

        for z in range(N):
            sum = 0
            for k in range(6):
                sum = sum + places_Bool[z][k] * row[k]
            if sum == 0:
                places[z] = upgrate_place(places[z], row)
                place_inform(row, z)
                break
            elif sum != 0 and z == N - 1:
                print('Cannot fulfill passengers requirements')
                flag = False

        if flag == True:
            for z in range(N):
                print("".join(places[z]))
                for zz in range(7):
                    if places[z][zz] == 'X':
                        places[z][zz] = '#'
