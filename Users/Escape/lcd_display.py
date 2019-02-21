# 가로줄(위, 중앙, 아래), 세로줄(좌측 상단, 우측 상단, 좌측 하단, 우측 하단)
# 출력 여부를 이진 데이터로 저장
# 예: 숫자 '4' 의 출력 결과에서 위쪽 부분의 출력 여부: TOP[4] → 출력하지 않으므로 0
TOP = (1, 0, 1, 1, 0, 1, 1, 1, 1, 1)
MIDDLE = (0, 0, 1, 1, 1, 1, 1, 0, 1, 1)
BOTTOM = (1, 0, 1, 1, 0, 1, 1, 0, 1, 1)
TOP_LEFT = (1, 0, 0, 0, 1, 1, 1, 0, 1, 1)
TOP_RIGHT = (1, 1, 1, 1, 1, 0, 0, 1, 1, 1)
BOTTOM_LEFT = (1, 0, 1, 0, 0, 0, 1, 0, 1, 0)
BOTTOM_RIGHT = (1, 1, 0, 1, 1, 1, 1, 1, 1, 1)

# 입력받을 값의 범위 설정
SIZE_RANGE = range(1, 10)
DIGIT_RANGE = range(0, 10 ** 8)


# 가로줄(-) 1줄 출력 함수
def write_horizontal(digit, size, floor):
    # floor 값에 따라 위, 중간, 아래 중 무엇을 출력할지 결정합니다.
    # 1 = 아래, 2 = 중간, 3 = 위
    byte_data = (BOTTOM, MIDDLE, TOP)[floor - 1]
    s = str()

    # 입력받은 숫자 하나하나씩 순환합니다.
    for d in (int(x) for x in digit):
        # 해당 부분을 출력해야 할 경우 양 옆 공백과 함께 size만큼의 '-'을 출력합니다.
        if byte_data[d]:
            s += ' ' + '-' * size + ' '
        # 출력하지 않는 경우 양 옆의 공백 1칸과 size만큼의 공백이 필요하므로 size + 2 만큼의 공백을 추가합니다.
        else:
            s += ' ' * (size + 2)
        # 지금 숫자와 다음 숫자 사이에 공백 하나를 추가합니다.
        s += ' '
    return s


# 세로줄(|) 1출 출력 함수
def write_vertical(digit, size, floor):
    # floor 값에 따라 윗부분과 아랫부분 중 무엇을 출력할지 결정합니다.
    # 1의 경우 BOTTOM_LEFT, BOTTOM_RIGHT 부분에 대한 작업
    # 2의 경우 TOP_LEFT, TOP_RIGHT 부분에 대한 작업
    data_l = (BOTTOM_LEFT, TOP_LEFT)[floor - 1]
    data_r = (BOTTOM_RIGHT, TOP_RIGHT)[floor - 1]
    s = str()

    # 입력받은 숫자 하나하나씩 순환합니다.
    for d in (int(x) for x in digit):
        # 첫 열 출력 여부 데이터를 확인 후 출력해야 하는 경우 첫 열에 '|'를 출력합니다.
        if data_l[d]:
            s += '|'
        # 출력하지 말아야 하는 경우 첫 열은 공백으로 남깁니다.
        else:
            s += ' '
        # size 만큼의 공간에는 가로줄만 들어가게 되므로 띄웁니다.
        s += ' ' * size
        # 마찬가지로 끝 열(맨 오른쪽) 출력 여부 데이터 확인 후 출력합니다.
        if data_r[d]:
            s += '|'
        else:
            s += ' '
        # 지금 숫자와 다음 숫자 사이에 공백 하나를 추가합니다.
        s += ' '
    # size 만큼 같은 줄을 반복하여 리턴합니다. (size가 5인 경우 같은 줄이 5번 반복)
    return '\n'.join([s] * size)


# 변환 함수
def digitalize(size, digit):
    # list로 만들면 어떨까 싶었는데 느리고 메모리도 많이 먹을 것 같아서 str로 처리합니다.
    lcd = str()

    # 윗줄부터 순차적으로 처리(마치 잉크젯 프린터가 인쇄하듯이)
    lcd += write_horizontal(digit, size, 3) + '\n'
    lcd += write_vertical(digit, size, 2) + '\n'
    lcd += write_horizontal(digit, size, 2) + '\n'
    lcd += write_vertical(digit, size, 1) + '\n'
    lcd += write_horizontal(digit, size, 1)
    return lcd


# 데이터 입력 및 검증 함수
def data_in(message=''):
    data_list = input(message).split(" ")
    if len(data_list) == 2:
        # '0 0' 이 입력된 경우 예외 발생시켜서 처리하도록 합니다.
        assert data_list != ['0', '0']
        # 데이터 유효성 검사 단계
        size, digit = data_list
        for d in data_list:
            if not d.isnumeric():
                # 숫자가 아닌 값을 받은 경우 ValueError를 발생합니다.
                raise ValueError
            elif int(size) not in SIZE_RANGE or int(digit) not in DIGIT_RANGE:
                # 숫자가 범위 안에 있지 않은 경우 ValueError를 발생합니다.
                raise ValueError
            return (int(size), digit)
    # 's n' 형식으로 입력받지 않은 경우 IndexError를 발생합니다.
    else:
        raise IndexError


# 유효한 값이 입력될 때까지 반복
while True:
    try:
        (size, digit) = data_in('크기, 숫자 입력: ')
    # s, n의 값이 올바르지 않은 경우
    except ValueError:
        print('올바르지 멧한 값입니다.')
    # 1개의 띄어쓰기로 구분하지 않은 경우
    except IndexError:
        print('(크기) (숫자) 식으로 입력해주십시오. (예: 2 9394684)')
    # 0 0을 입력받을 경우 발생하는 예외의 처리(종료되게 함)
    except AssertionError:
        exit()
    else:
        break

print(digitalize(size, digit))
