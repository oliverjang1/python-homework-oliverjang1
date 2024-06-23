value = int(input('정수를 입력하세요 >>> '))
if value > 0:
    n = 1
    while n <= value: 
        print('{}번째 Hello'.format(n))
        n += 1
    print('o---------------o')
else:
    print('잘못된 입력입니다.')

m = 1
while m <= 14:
    f = 7
    print('{}'.format(m * f))
    m += 1

price = int(input('자판기에 얼마를 넣을까요? >>> '))
u_price = 300
n = 1
while price - (u_price * n) >= 0:
    print('커피 {}잔, 잔돈 {}원'.format(n, price - (u_price * n)))
    n += 1

my_list = set()

n = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
if 0 <= n <= 9:
    while len(my_list) < 5:
        my_list.add(n)
        n = int(input('0 ~ 9 사이 정수를 입력하세요 >>> '))
    print(my_list)

n = 1
print('{}    {}    {}    {}    {}    {}    {}    {}    {}    {}'.format(n, n + 1, n + 2, n + 3, n + 4, n + 5, n + 6, n + 7, n + 8, n + 9))
m = 11
while m <= 100:
    print('{}   {}   {}   {}   {}   {}   {}   {}   {}   {}'.format(m, m + 1, m + 2, m + 3, m + 4, m + 5, m + 6, m + 7, m + 8, m + 9))
    m += 10

dan = 2
n = 1
while n <= 9:
    print('{}x{}={}  {}x{}={}  {}x{}={}  {}x{}={}  {}x{}={}  {}x{}={}  {}x{}={}  {}x{}={}'.format(dan, n, dan * n, dan + 1, n, (dan + 1) * n, dan + 2, n, (dan + 2) * n, dan + 3, n, (dan + 3) * n, dan + 4, n, (dan + 4) * n, dan + 5, n, (dan + 5) * n, dan + 6, n, (dan + 6) * n, dan + 7, n, (dan + 7) * n))
    n += 1