class Circle():
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return 2 * self. radius


circle = Circle(10)
print("반지름")
print(circle.radius)
# 속성처럼 사용할 수 있다.
print("지름")
print(circle.diameter)

# 바로 계산이 된다.
circle.radius = 5
print("반지름이 5일 때 지름")
print(circle.diameter)

# 오류
circle.diameter = 20
