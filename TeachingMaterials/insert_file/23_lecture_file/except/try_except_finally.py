number_list = [1, 2, 3]

try:
    index = int(input("인덱스를 입력하세요."))
    print(number_list[index])

except IndexError as e:
    print("인덱스 범위가 아닙니다.", e)

finally:
    print("언제나 실행됩니다.")

