from time import sleep
for i in range(100):
    msg = '\r%d%%' % (i+1)
    # print('.'*len(msg), end='')
    print(msg, end='')
    sleep(0.1)
sleep(0.3)
