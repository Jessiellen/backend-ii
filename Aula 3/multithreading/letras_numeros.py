import threading
import time

def print_letters():
    for letter in ['A', 'B', 'C', 'D', 'E']:
        print(f"Letra: {letter}")
        time.sleep(0.5)

def print_numbers():
    for number in range(1, 6):
        print(f"Número: {number}")
        time.sleep(0.5)

t1 = threading.Thread(target=print_letters)
t2 = threading.Thread(target=print_numbers)

t1.start()
t2.start()

t1.join()
t2.join()

print("Execução concluída.")
