"""
convert_fahrenheit_celsisus
#화씨 온도를 섭씨온도로 변환하는 프로그램
"""

fah = float(input("변환할 화씨온도(˚F)를 입력하시오: "))
tmp = fah-32
cel = tmp*(5/9)
print("%0.2f˚F는 %0.2f˚C입니다." % (fah, cel))
