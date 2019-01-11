short_slogan = '멧또찐'
long_slogan = '멧됒따리멧됒따'
mood = '신나는'
singer = '나'

print('''{lyrics} {mood} 노래
{singer}도 한 번 불러본다~
{chooimsae}'''.format(lyrics=' '.join([short_slogan, short_slogan]),
                      mood=mood, singer=singer, chooimsae=long_slogan))

'''
줄이 넘어갈 때는 끝에 \ 을 붙이는 게 원칙이지만
매개 변수를 나열하다가 줄이 넘어가면 그런 게 필요없습니다.
오히려 붙이면 뭐라 합니다.
'''
