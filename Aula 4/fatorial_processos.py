import multiprocessing

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    return n * fatorial(n - 1)

def calcular_fatorial(numero):
    resultado = fatorial(numero)
    print(f"Fatorial de {numero} é {resultado}")

if __name__ == "__main__":
    numeros = [5, 6, 7, 8]  
    processos = []

    for n in numeros:
        p = multiprocessing.Process(target=calcular_fatorial, args=(n,))
        processos.append(p)
        p.start() 

    for p in processos:
        p.join()

    print("Todos os cálculos de fatorial terminaram.")
