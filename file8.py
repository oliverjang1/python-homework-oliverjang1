def vending_machine(money): 
    n = 0
    while n <= money // 700:
        print('음료수 = {}개, 잔돈 = {}원'.format(n, money - n*700))
        n += 1
vending_machine(3000)

def get_average(marks):
    sum = 0

    for key in marks:
        score = marks[key]
        sum += score

    count = len(marks)

    average = sum/count
    return average

marks = {'국어': 90, '영어': 80, '수학': 85}
average = get_average(marks)
print('평균은 {}점입니다.'.format(average))

total = 0

def gift(dic, who, money):
    dic[who] = money
    global total
    total += money

wedding = {}
gift(wedding, '영희', 5)
gift(wedding, '철수', 3)
gift(wedding, '이모', 10)
print('축의금 명단: {}'.format(wedding))
print('전체 축의금: {}'.format(total))