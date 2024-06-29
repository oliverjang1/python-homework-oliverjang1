def vending_machine(money): 
    n = 0
    while n <= money // 700:
        print('음료수 = {}개, 잔돈 = {}원'.format(n, money - n*700))
        n += 1
vending_machine(3000)

def get_average(marks):
    sum()
    return average

marks = {'국어': 90, '영어': 80, '수학': 85}
average = get_average(marks)
print('평균은 {}점입니다.'.format(average))