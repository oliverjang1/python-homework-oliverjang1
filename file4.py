score = int(input('점수를 입력하세요 >>> '))
if score <= 100 and score >= 90:
    print(f'점수는 {score}점이고, 학점은 {'A'}학점입니다.')
elif score < 90 and score >= 80:
    print(f'점수는 {score}점이고, 학점은 {'B'}학점입니다.')
elif score < 80 and score >= 70:
    print(f'점수는 {score}점이고, 학점은 {'C'}학점입니다.')
elif score < 70 and score >= 60:
    print(f'점수는 {score}점이고, 학점은 {'D'}학점입니다.')
else:
    print(f'점수는 {score}점이고, 학점은 {'F'}학점입니다.')

number = int(input('정수를 입력하세요 >>> '))
if number % 3 == 0:
   print(f'{number}는 3의 배수입니다.')
else: print(f'{number}는 3의 배수가 아닙니다.')
print(f'o-------------o')

noone = int(input('정수1 입력 >>> '))
notwo = int(input('정수2 입력 >>> '))
nothr = int(input('정수3 입력 >>> '))
if noone > notwo > nothr or noone > nothr > notwo:
    print(f'가장 큰 수는 {noone}입니다.')
elif notwo > noone > nothr or notwo > nothr > noone:
    print(f'가장 큰 수는 {notwo}입니다.')
elif nothr > noone > notwo or nothr > notwo > noone:
    print(f'가장 큰 수는 {nothr}입니다.')

car = input('차량번호를 입력하세요 >>> ')
result = ('운행가능') if (int(car[-2]) % 2 == 0) else ('운행불가')
print(f'차량번호 {car}는 오늘 {result}입니다.')