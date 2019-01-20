def check_value():
    num = int(input("5의 배수를 입력하세요: "))
    if num % 5 != 0:
        raise Exception('5의 배수가 아닙니다!')
    print(num)


def check_value_call():
    check_value()


print("시작")
check_value()
print("종료")
