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
        print("예외를 상위 호출자에게 던집니다.")
        raise


print("시작")
try:
    check_value_call()
except Exception as err:
    print(err)
    print("예외를 처리합니다.")
print("종료")
