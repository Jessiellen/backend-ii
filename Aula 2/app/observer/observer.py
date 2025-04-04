class Observer:
    def update(self, message: str):
        pass

class ConcreteObserver(Observer):
    def update(self, message: str):
        print(f"Observador: {message}")