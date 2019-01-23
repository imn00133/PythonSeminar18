def nmche(n, m):
    if n == 0 or m == 0:
        print("0은 안되. 지옥으로 가!")
        return True
    if n <= 30 and m <= 30:
        return False
    else:
        print("자네 무엇을 입력한게야!!!")
        return True


def value_push(cou, snail_arr, i, j):
    snail_arr[i][j] = cou
    return cou + 1


while True:
    n = (int)(input("열입력: "))
    m = (int)(input("행입력: "))
    snail_arr = [[0]*n for i in range(m)]
    i = 0
    j = 0
    cou = 1
    if n < 0 or m < 0:
        break
    if nmche(n, m):
        continue
    while True:
        if cou == n*m:
            break
        while j+1 != n:
            if snail_arr[i][j+1] == 0:
                cou = value_push(cou, snail_arr, i, j)
                j += 1
            else:
                break
        while i+1 != m:
            if snail_arr[i+1][j] == 0:
                cou = value_push(cou, snail_arr, i, j)
                i += 1
            else:
                break
        while j-1 != -1:
            if snail_arr[i][j-1] == 0:
                cou = value_push(cou, snail_arr, i, j)
                j -= 1
            else:
                break
        while i-1 != -1:
            if snail_arr[i-1][j] == 0:
                cou = value_push(cou, snail_arr, i, j)
                i -= 1
            else:
                break
    snail_arr[i][j] = cou
    for i in range(0, m):
        for j in range(0, n):
            print("%4d" % (snail_arr[i][j]), end='')
        print("")
    snail_arr.clear()
