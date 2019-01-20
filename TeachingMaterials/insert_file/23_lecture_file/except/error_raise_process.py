def check_value():
    num = int(input("5의 배수를 입력하세요: "))
    if num % 5 != 0:
        raise Exception('5의 배수가 아닙니다!')
    print(num)


def check_value_call():
    try:
        check_value()
    except Exception as err:
        print(err)
        print("예외를 처리합니다.")


print("시작")
check_value_call()
print("종료")
