def example(pos, *args, kwd=None, **kwargs):
    print("pos: %s" % pos)
    if args:
        for value in args:
            print("args: %s" % value)
    if kwd is not None:
        print("kwd: %s" % kwd)
    if kwargs is not None:
        for key, value in kwargs.items():
            print("kwargs, key: %s, value: %s" % (key, value))


example(1)
example(1, 3, 4, 5)
example(1, kwd=23)
example(pos=1, kwd=23, test=4, this="this")
mydic = {'pos': 1, 'kwd': "kwd", 'this': "this"}
example(**mydic)
