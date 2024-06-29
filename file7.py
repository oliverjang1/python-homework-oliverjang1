balance = 10000

while True:
    use_amount = int(input('사용할 금액 입력 >>> '))
    if balance == 0:
        print('현재 0원이 있습니다.')
        break
    else:
        if use_amount <= 0:
            print('0 이하의 금액은 사용할 수 없습니다.')
        elif balance < use_amount:
            print(f'{use_amount - balance}원이 부족합니다.')
        else:
            balance -= use_amount
            print(f'현재 {balance}원이 있습니다.')



while True:
    score = int(input('이번 영화의 평점을 입력하세요 >>> '))
    if 1 <= score <= 5:
        print(f'평점: {'⭐' * score}')
        break
    else:
        print('평점은 1~5 사이만 입력할 수 있습니다.')
