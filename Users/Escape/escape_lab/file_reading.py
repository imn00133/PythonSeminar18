# 파일로부터 물품 불러오기
def load_product(file_name='data.dat'):
    result = list()
    with open(file_name, mode='r', encoding='UTF-8') as f:
        for line in f.readlines():
            # - 로 시작하는 행은 주석 처리
            if line[0] == '-' or line == '\n':
                pass
            # 소괄호 안에 정보가 들어간 경우 물품 정보로 판단
            # (품명, 가격, 재고량) 으로 인식
            elif line[0] == '(' and line[-2] == ')':
                product = line[1:len(line) - 2].split(',')
                for i, detail in enumerate(product):
                    product[i] = detail.strip()
                product[1], product[2] = int(product[1]), int(product[2])
                result.append(product)
    return result


print(load_product())
