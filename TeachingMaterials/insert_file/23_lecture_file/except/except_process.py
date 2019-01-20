def error_raise():
    a = 2/0


def error_raise_call():
    print("error raise call")
    error_raise()


print("시작")
error_raise_call()
