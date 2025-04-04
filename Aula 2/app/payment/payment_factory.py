from .payment_method import ApplePay, MBWay, PayPal

def payment_factory(payment_type: str) -> PaymentMethod:
    if payment_type == "applepay":
        return ApplePay()
    elif payment_type == "mbway":
        return MBWay()
    elif payment_type == "paypal":
        return PayPal()
    else:
        raise ValueError(f"Método de pagamento {payment_type} não reconhecido.")