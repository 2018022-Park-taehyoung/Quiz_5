class 붕어빵:
    def __init__(self, type, price):
        self.type = type
        self.price = price
        self.total = 0

    def sell(self):
        print(self.type + "을 " + self.price + "원에 팔았습니다.")
        self.total += int(self.price)

    def eat(self):
        print(self.type + "을 먹었습니다.")


슈크림 = 붕어빵("슈크림 붕어빵", "1000")
팥 = 붕어빵("팥 붕어빵", "1500")

팥.eat()
슈크림.eat()

팥.sell()
팥.sell()
팥.sell()
팥.sell()
print(팥.total)

슈크림.sell()
슈크림.sell()
슈크림.sell()
print(슈크림.total)
