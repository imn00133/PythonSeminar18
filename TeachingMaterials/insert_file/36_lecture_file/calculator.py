"""
이 파일은 사칙연산을 함수로 가진 묘듈입니다.
"""


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def main():
    print("계산기 모듈입니다.")
    print(add(10, 10))
    print(mul(10, 10))


if __name__ == "__main__":
    main()
