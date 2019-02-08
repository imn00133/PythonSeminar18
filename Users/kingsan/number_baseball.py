from random import randint


def init():
    answer = []

    while True:
        number = randint(0, 9)

        if number not in answer:
            answer.append(number)

        if len(answer) == 4:
            break

    return answer


def number_baseball():
    while True:
        try:
            try_number = str(input("중복되지 않은 4자리수를 입력해주세요(0000~9999): "))
            if len(try_number) != 4:
                print("4자리 숫자를 입력해주세요.")
                continue

            User_answer = []

            for i in [0, 1, 2, 3]:
                if int(try_number[i]) not in User_answer:
                    User_answer.append(int(try_number[i]))

            if len(User_answer) < 4:
                print("각 자리 숫자가 중복되지 않게 입력해주세요.")
                continue

            return User_answer
        except ValueError:
            print("숫자를 입력해주세요.")
        except UnicodeDecodeError:
            print("숫자를 입력해주세요.")


def checkanswer(com, user):
    strike = 0
    ball = 0

    for index, num in enumerate(user, 0):
        if num in com:
            if user[index] == com[index]:
                strike += 1
            else:
                ball += 1

    if strike == 4:
        return True
    else:
        print(strike, "스트라이크 ", ball, "볼 입니다.")
        return False


c_answer = init()
try_count = 0

proc = True

while proc:
    u_answer = number_baseball()

    try_count += 1

    if checkanswer(c_answer, u_answer):
        print("정답입니다. 시도횟수 : ", try_count)
        while True:
            restart = input("다시 하시겠습니까?(Y/N) : ")

            if restart == 'Y':
                c_answer = init()
                try_count = 0
                print("재시작 합니다!")
                break
            elif restart == 'N':
                print("종료합니다.")
                proc = False
                break
            else:
                print("올바른 값을 입력해주세요.")
