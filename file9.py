import time
import random

pot = []
for i in range(1, 46):
    pot.append(i)

jackpot = []
count = 1
while count <= 6:
    random.shuffle(pot)
    jackpot.append(pot.pop())
    print(f'{count}번째 당첨번호는 {jackpot[count - 1]}입니다.')
    time.sleep(2)
    count += 1
jackpot.sort()

# 첫번째 append 때는 0: 12 -> jackpot[12]만 되니까 그 다음 print 실행할 때 {jackpot[count]}로 되면 1번째 인덱스부터 들어가므로 0번째부터 들어가게 설정해줘야 한다.
print(f'이번 당첨번호는 {jackpot} 입니다.')


import datetime
import math

print('UpDown게임을 시작합니다.')

n = random.randint(1, 100)
start = datetime.datetime.now()
while True:
    UpDown = int(input('어떤 값일까요? >>> '))

    if UpDown < n:
        print('Up')
    elif UpDown > n:
        print('Down')
    else:
        print('정답입니다.')
        break
end = datetime.datetime.now()

leadtime = (end - start).total_seconds()
leadtime = math.trunc(leadtime)
print(f'{leadtime}초 만에 성공했습니다.')