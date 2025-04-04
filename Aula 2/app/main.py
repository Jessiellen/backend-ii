# from payment.payment_factory import payment_factory

# def main():
#     payment_method = payment_factory("applepay")
#     print(payment_method.process_payment(100.50))

#     payment_method = payment_factory("mbway")
#     print(payment_method.process_payment(50.75))

#     payment_method = payment_factory("paypal")
#     print(payment_method.process_payment(200.99))

# if __name__ == "__main__":
#     main()

from payment.payment_factory import payment_factory
from observer.subject import Subject
from observer.observer import ConcreteObserver

def main():
    payment_subject = Subject()
    observer = ConcreteObserver()
    payment_subject.add_observer(observer)
    
    payment_method = payment_factory("paypal")
    
    payment_result = payment_method.process_payment(200.99)
    payment_subject.set_state(payment_result)  
    
    payment_method = payment_factory("applepay")
    payment_result = payment_method.process_payment(150.00)
    payment_subject.set_state(payment_result)  

if __name__ == "__main__":
    main()
