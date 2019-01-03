a = {1, 3}
a.clear()
print(a)

'''
A = set([a, b, ...])
A = {a, b, ...}

공집합 선언 방법
A = set()
(A = {} 로 정의하면 공집합이 아닌 빈 딕셔너리가 된다.)

원소의 개수
N(A): len(A)

교집합 &
합집합 |
차집합 -

값 추가
A.add a >> a라는 원소를 추가
A.update([a, b, c]) >> a, b, c를 추가

값 제거
A.remove a
A.discard a
A.difference_update([a, b, c]) >> a, b, c를 제거(A와 {a, b, c}의 차집합이 됨)

?!
A.intersection_update([a, b, c]) >> a, b, c 만 남기고 모두 제거

[a, b, c] 대신 {a, b, c} 사용 가능

원소 포함 판별
a ∈ A >> a in A

부분집합 판별
A ⊂ B >> A.issubset(B)
A ⊃ B >> A.issuperset(A)
(A in B 는 A가 B의 원소라는 뜻)

서로소 판별
len(A & B) == 0
A.isdisjoint(B)
후자가 오히려 입력하기 편할 것 같다.

집합 복사
B = A.copy()
원소가 모두 같은 집합 B가 생성된다.

원소 전부 제거
A.clear()
객체를 새로 만들지 않는다는 것이 A = set() 과 차별화된 점인 것 같다.
'''
