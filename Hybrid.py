# 다음과 같은 슈퍼 클래스 Car를 가진 서브클래스 Hybrid 구현

class Car:

    max_oil = 50 #최대 주유량

    def __init__(self, oil):
        self.oil = oil

    def add_oil(self, oil):
        if oil <= 0:  # 0 이하의 주유는 진행하지 않음
            return
        self.oil += oil
        if self.oil > Car.max_oil:
            self.oil = Car.max_oil

    def car_info(self):
        print('현재 주유상태: {}'.format(self.oil))

# 최대 배터리 충전량 30
# 배터리 충전 Charge() 메소드. 최대 충전량을 초과하도록 충전 불가. 0보다 작은 값으로 충전 불가.
# 현재 주유량과 충전량 모두 확인 가능한 hybrid_info() 메소드 있음.

class Hybrid(Car):

    max_charge = 30

    def __init__(self, oil, charge):
        super().__init__(oil)
        self.charge = charge

    def add_charge(self, charge):
        if charge <= 0:  # 0 이하의 주유는 진행하지 않음
            return
        self.charge += charge
        if self.charge > Hybrid.max_charge:
            self.charge = Hybrid.max_charge

    def hybrid_info(self):
        print(f'현재 주유상태: {self.oil}  현재 충전상태: {self.charge}')


# 다음과 같은 방식으로 전체 동작 확인 가능
car = Hybrid(0, 0)
car.add_oil(100)
car.charge(50)
car.hybrid_info() # 현재 주유상태: 50  # 현재 충전상태: 30 

# Hint. 서브 클래스의 생성자는 반드시 슈퍼 클래스의 생성자 먼저 호출. Super().메소드() 방식 사용하기.