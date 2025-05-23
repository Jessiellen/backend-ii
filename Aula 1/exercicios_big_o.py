# Função fatorial recursiva
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Testes
if __name__ == "__main__":
    print("Fatorial de 0:", factorial(0))  # 1
    print("Fatorial de 1:", factorial(1))  # 1
    print("Fatorial de 5:", factorial(5))  # 120
    print("Fatorial de 10:", factorial(10))  # 3628800
