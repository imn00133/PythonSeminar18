from random import randrange


def judgment(arr, n):
    for j in arr:
        if n == j:
            return False
    return True


def makenum(computer):
    for i in range(0, 4):
        n = randrange(10)
        if judgment(computer, n):
            computer.append(n)
    for i in computer:
        print("%d" % i, end='')
    print("")


def ball_judge(user, computer):
    strike = 0
    ball = 0
    out = 0
    for i in range(0, 4):
        out = out+1
        for j in range(0, 4):
            print("%d %d" % (user[j], computer[i]))
            if user[j] == computer[i]:
                if i == j:
                    strike = strike+1
                else:
                    ball = ball+1
                out = out-1
                break
    print("strike:%d ball:%d out:%d" % (strike, ball, out))
    if strike == 4:
        return True
    return False


def conti():
    while True:
        con = (str)(input("계속하시겠습니까?(yes/no): "))
        if cou == "yes" or cou == "y":
            return False
        elif cou == "no" or cou == "n":
            return True


computer = list()
user = list()
while True:
    cou = 0
    makenum(computer)
    while True:
        q = 1000
        n = (int)(input("입력(0000~9999): "))
        for i in range(0, 4):
            if judgment(user, n/q) and n/q >= 0 and n/q <= 9:
                user.insert(i, n/q)
                n = n % q
                q = q/10
            else:
                break
        if i != 3:
            cou = cou-1
            print("다시 입력해주세요")
            continue
        if ball_judge(user, computer):
            print("%d만에 성공하셨습니다." % cou)
            break
    if conti():
        break
