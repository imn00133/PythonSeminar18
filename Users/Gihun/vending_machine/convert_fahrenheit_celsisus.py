inOndo = float(input("변환할 화씨온도를 입력하쇼: "))


outOndo = (float(inOndo) - 32) * (5/9)

outOndo = "%0.2f" % outOndo

print("{inO} °F 의 섭씨는 {out}°C 라고한다".format(inO=inOndo, out=outOndo))
