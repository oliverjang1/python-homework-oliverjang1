a = float(input('첫 번째 실수를 입력하세요>>>'))
b = float(input('두 번째 실수를 입력하세요>>>'))
print('두 실수의 합은 {}입니다.'.format(a + b))

month = int(input('1~12 사이의 월을 입력하세요>>>'))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
print(f'{month}월은 {days_in_month[month - 1]}일까지 있습니다.')

terminology = str(input('영어 단어를 입력하세요>>>'))
english_dict = {
    'flower': '꽃',
    'fly': '날다',
    'floor': '바닥'
}
print(f'{terminology}: {english_dict[terminology]}')

s = set()
a = str(input('희망하는 수학여행지를 입력하세요>>>'))
s.add(a)
b = str(input('희망하는 수학여행지를 입력하세요>>>'))
s.add(b)
c = str(input('희망하는 수학여행지를 입력하세요>>>'))
s.add(c)
print(f'조사된 수학여행지는 {s}입니다.')