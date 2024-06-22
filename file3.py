a = int(input('10 ~ 99 사이의 정수를 입력하세요 >>> '))
print('십의 자리: {}'.format(a // 10))
print('일의 자리: {}'.format(a % 10))

t = int(input('초를 입력하세요 >>> '))
h = t // 3600
m = t % 3600 // 60
s = (t % 3600) % 60
print(f'변환 결과는 {h}시간 {m}분 {s}초입니다.')

e = int(input('4자리 사원번호를 입력하세요 >>> '))
result = ('오전') if (e % 10 >= 5) else ('오후')
print('근무 시간은 {}입니다.'.format(result))

print('한 박스에 20개의 라면을 담을 수 있습니다.')
print('라면의 개수를 입력하시면 필요한 박스 수를 알려드립니다.')
f = int(input('라면의 개수를 입력하세요 >>> '))
result = (f // 20 + 1) if (f % 20 > 0) else (f // 20)
print('{}개 라면을 담으려면 {}박스가 필요합니다.'.format(f, result))

k = int(input('국어 점수를 입력하세요 >>> '))
e = int(input('영어 점수를 입력하세요 >>> '))
ma = int(input('수학 점수를 입력하세요 >>> '))
result = ('합격') if ((k + e + ma) / 3 >= 80) else ('불합격')
print(f'평균은 {(k + e + ma) / 3}점이고, 결과는 {result}입니다.')