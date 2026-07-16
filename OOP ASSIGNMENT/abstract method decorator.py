from abc import ABC, abstractmethod

class PaymentGateway(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def refund(self):
        pass

class CreditCardPayment(PaymentGateway):

    def pay(self):
        print("Payment made using Credit Card.")

    def refund(self):
        print("Refund processed to Credit Card.")

class PayPalPayment(PaymentGateway):

    def pay(self):
        print("Payment made using PayPal.")

    def refund(self):
        print("Refund processed to PayPal.")

c = CreditCardPayment()
p = PayPalPayment()

c.pay()
c.refund()

p.pay()
p.refund()