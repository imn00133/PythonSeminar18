def error_raise():
    a = 2/0
    print("예외로 인해 실행 안됨")


def error_raise_call():
    print("error raise call")
    try:
        error_raise()
    except ZeroDivisionError:
        print("예외를 처리합니다.")


print("시작")
error_raise_call()
print("종료")
