class Display:
    # 가로줄(위, 중앙, 아래), 세로줄(좌측 상단, 우측 상단, 좌측 하단, 우측 하단)
    # 출력 여부를 이진 데이터로 저장
    TOP = [1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
    MIDDLE = [0, 0, 1, 1, 1, 1, 1, 0, 1, 1]
    BOTTOM = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1]
    TOP_LEFT = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1]
    TOP_RIGHT = [1, 1, 1, 1, 1, 0, 0, 1, 1, 1]
    BOTTOM_LEFT = [1, 0, 1, 0, 0, 0, 1, 0, 1, 0]
    BOTTOM_RIGHT = [1, 1, 0, 1, 1, 1, 1, 1, 1, 1]

    SIZE_RANGE = range(1, 10)
    DIGIT_RANGE = range(0, 10 ** 8)

    def __init__(self, size=1, digit=0):
        self._size = size
        self._digit = digit

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, s):
        if isinstance(s, int):
            self._size = s
        elif isinstance(s, str):
            if s.isnumeric():
                self._size = int(s)
            else:
                raise ValueError
        else:
            raise ValueError

        # 지정 범위 안에 값이 없으면 에러 발생
        assert self._size in self.SIZE_RANGE

    @property
    def digit(self):
        return self.digit

    @digit.setter
    def digit(self, n):
        if isinstance(n, int):
            self._digit = n
        elif isinstance(n, str):
            if n.isnumeric():
                self._digit = int(n)
            else:
                raise ValueError
        else:
            raise ValueError

        # 지정 범위 안에 값이 없으면 에러 발생
        assert self._digit in self.DIGIT_RANGE

    def _bit(a, b):
        return (a & b) // b

    def convert(self):
        digits = [int(x) for x in str(self._digit)]
        print(digits)
        lcd = str()
        if self._digit < 10:
            for d in digits:
                if TOP[d]:
                    lcd += ' ' + '-' * self._size + ' '
                else:
                    lcd += ' ' * (self._size + 2)
            # for~
            lcd += '\n'
            for d in digits:
                if TOP_LEFT[d]:
                    lcd += '|'
                else:
                    lcd += ' '

            # (DIGIT_DATA(self._digit) & 8) // 8
            # (DIGIT_DATA(self._digit) & 4) // 4


a = Display()
a.size = 9
a.digit = 5923
print((95 & 64) // 64)
