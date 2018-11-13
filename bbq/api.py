from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):
    @abstractmethod
    def pay(self, money):
        pass


class AppPay(Payment):
    def pay(self, money):
        print("AppPay pay %d" % money)


class Alipay(Payment):
    def pay(self, money):
        print("AppPay pay %d" % money)


AppPay().pay(100)
Alipay().pay(100)
