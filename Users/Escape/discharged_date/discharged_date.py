import datetime


def read_data():
    with open('data.txt', mode='r', encoding='UTF-8') as f:
        lines = list(map(delete_enters, f.readlines()))
        columns = {x[0]:
                   (datetime.datetime.strptime(x[1], '%Y.%m.%d'),
                    datetime.datetime.strptime(x[2], '%Y.%m.%d'))
                   for x in map(split_columns, lines)
                   if x[0].isnumeric()}
        return columns


def split_columns(x):
    return x.split()


def delete_enters(x):
    return x.replace('\n', '')


def print_smart(dic, keys):
    if len(keys) == 0:
        raise IndexError
    elif len(keys) == 1:
        print_single(dic, keys[0])
    else:
        print_multi(dic, keys)


def print_single(dic, key):
    start, end = dic[key]
    gone = (today - start).days + 1
    remained = (end - today).days

    if today < start:
        print('입대 D-%s' % -gone)
    elif end < today:
        print('전역 D+%s' % -remained)
    else:
        print('현재 복무일수: %s일\n남은 복무일수: %s일' % (gone, remained))
        print('%0.2f%% 완료' % (100 * gone / (gone + remained)))


def print_multi(dic, keys):
    for k in keys:
        try:
            dic[k]
        except IndexError:
            pass
        else:
            print('%s기 정보' % k)
            print_single(dic, k)
            print('')
    print('짬어택하지 않는 착한 군바리가 됩시다 ^^')


dic = read_data()
today = datetime.datetime.combine(datetime.date.today(), datetime.time(0))
raw_d = input('기수를 입력하세요: ')
keys = raw_d.split()
try:
    print_smart(dic, keys)
except KeyError:
    print('기수를 잘못 입력하셨거나, 해당 기수에 해당하는 데이터가 없습니다.')
    exit()
except IndexError:
    print('데이터가 입력되지 않았습니다.')
