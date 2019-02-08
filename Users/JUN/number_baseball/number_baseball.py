from random import randrange


def che(arr, n):
    for i in arr:
        if i == n:
            return False
    return True


def count(com, use):
    scou = 0
    bcou = 0
    for i in range(0, 4):
        for j in range(0, 4):
            if use[i] == com[j]:
                if i == j:
                    scou = scou+1
                else:
                    bcou = bcou+1
    print("strike:%d ball:%d out:%d" %(scou, bcou, 4-(scou+bcou)))
    if scou == 4:
        return True
    return False


def option():
    while True:
        op = (str)(input("계속?(yes/no):"))
        if op == "yes" or op == "y":
            return False
        elif op == "no" or op == "n":
            return True


while True:
    cou = 0
    computer = list()
    while len(computer) < 4:
        n = (str)(randrange(0, 9))
        if che(computer, n):
            computer += n
    while True:
        cou = cou+1
        user = (str)(input("입력(0000~9999): "))
        if len(user) > 4:
            print("큼")
            continue
        elif len(user) < 4:
            print("작음")
            continue
        for i in range(0, 4):
            for j in range(i+1, 4):
                if che(user[i], user[j]) == False:
                    break
            if j < 3:
                break
        if i < 3:
            cou = cou-1
            print("중복X")
            continue
        if count(computer, user):
            print("%d만에 성공" %cou)
            break
    if option():
        print("종료합니다.")
        break
