class InvalidIntError(Exception):
    def __init__(self, arg):
        super().__init__("정수가 아닙니다.: %s" % arg)


def convert_int(text):
    if text.isdigit():
        return int(text)
    else:
        raise InvalidIntError(text)


try:
    text = input("숫자를 입력하세요: ")
    number = convert_int(text)
except InvalidIntError as e:
    print('예외 발생 (%s)' % e)
else:
    print("정수형식으로 변환하였습니다.")
