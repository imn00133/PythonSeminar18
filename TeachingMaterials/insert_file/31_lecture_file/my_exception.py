class MyExceptionError(Exception):
    def __init__(self):
        super().__init__("사용자 정의 예외 발생")
