def div_che(num):
    arr = []
    temp = num
    che = 1
    while che < num:
        che *= 10
    che /= 10
    while (int)(che) != 0 and (int)(temp) != 0:
        if (int)(temp/che) % 3 == 0:
            arr += "짝"
        if (int)(temp/che) % 2 == 0:
            arr += "뽁"
        temp %= che
        che /= 10
    if len(arr) > 0:
        arr = str(arr).replace('[\'', '')
        arr = str(arr).replace('\']', '')
        arr = str(arr).replace('\', \'', '')
        return arr
    return num


arr = []
n = (int)(input("입력: "))
for i in range(1, n+1):
    arr = print("%s" % div_che(i), end=' ')
    #20번째마다 줄바꿈
    if i % 20 == 0:
        print("")
if i % 20 != 0:
    print("")
