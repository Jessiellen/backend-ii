from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class ApplePay(PaymentMethod):
    def process_payment(self, amount: float):
        return f"Pagamento de {amount} realizado via Apple Pay."

class MBWay(PaymentMethod):
    def process_payment(self, amount: float):
        return f"Pagamento de {amount} realizado via MBWay."

class PayPal(PaymentMethod):
    def process_payment(self, amount: float):
        return f"Pagamento de {amount} realizado via PayPal."