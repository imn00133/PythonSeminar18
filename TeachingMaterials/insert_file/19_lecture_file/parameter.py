# 내부에 있는 변수명임으로, 바꿔도 상관 없다.
def test(value_list):
    for value in value_list:
        print(value_list)


value_list = [1, 2, 3]
test(value_list)
