import multiprocessing

# Função para verificar se um número é primo
def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Função que será chamada por cada processo
def verificar(numero):
    if eh_primo(numero):
        print(f"{numero} é primo.")
    else:
        print(f"{numero} não é primo.")

if __name__ == "__main__":
    numeros = [29, 97, 1234567, 104729, 999331]
    processos = []

    for n in numeros:
        p = multiprocessing.Process(target=verificar, args=(n,))
        processos.append(p)
        p.start()

    for p in processos:
        p.join()

    print("Verificação finalizada.")
