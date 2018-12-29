short_slogan = '멧또찐'
long_slogan = '멧됒따리멧됒따'
mood = '신나는'
singer = '나'

print('''{lyrics} {mood} 노래
{singer}도 한 번 불러본다~
{chooimsae}'''.format(lyrics=' '.join([short_slogan, short_slogan]),
                      mood=mood, singer=singer, chooimsae=long_slogan))
