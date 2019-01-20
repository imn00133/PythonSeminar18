def is_number(num):
    try:
        float(num)
    except ValueError:
        raise Exception("부동소수점으로 변환할 수 없습니다.")
    return True


num = input("부동소수점을 입력하세요: ")
while not is_number(num):
    num = input("부동소수점을 입력해주세요: ")
num = float(num)
print(num)

