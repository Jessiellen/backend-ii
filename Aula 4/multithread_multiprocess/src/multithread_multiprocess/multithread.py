######## EXEMPLO EM AULA ##############

# import 
# import

# class ImageProcessor:
#     def __init__(self, input_dir,output_dir,num_threads):
#         self.input_dir = input_dir
#         self.num_threads = num_threads
#         self.image_queue = image_queue
        


########### EXERCICIO EM AULA ##########

# import threading
# import math

# def calcular_fatorial(numero):
#     resultado = math.factorial(numero)
#     print(f"Fatorial de {numero} é {resultado}")

# numeros = [5, 7, 10, 12, 28]

# threads = []

# for numero in numeros:
#     thread = threading.Thread(target=calcular_fatorial, args=(numero,))
#     threads.append(thread)
#     thread.start()


# for thread in threads:
#     thread.join()

# print("Cálculos  fatoriais foram concluídos.")

import threading
import time

def ler_arquivo(nome_arquivo):
    print(f"Iniciando leitura do arquivo: {nome_arquivo}")
    time.sleep(2)  
    print(f"Leitura do arquivo {nome_arquivo} concluída!")

arquivos = ["arquivo1.txt", "arquivo2.txt", "arquivo3.txt"]

threads = []

for arquivo in arquivos:
    t = threading.Thread(target=ler_arquivo, args=(arquivo,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todas as leituras foram concluídas.")

######## USANDO URLS ######

import threading
import time

def realizar_download(url):
    print(f"Iniciando download de: {url}")
    time.sleep(10) 
    print(f"Download de {url} concluído!")

urls = ["https://site1.com", "https://site2.com", "https://site3.com"]

threads = []
for url in urls:
    thread = threading.Thread(target=realizar_download, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Todos os downloads foram concluídos.")


##### USANDO O REQUEST #########

import threading
import requests

def acessar_site(url):
    print(f"Iniciando acesso ao site: {url}")
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Redirecionamento para {url} concluído! Status: OK")
    else:
        print(f"Falha ao acessar {url}. Status: {response.status_code}")

sites = ["https://www.google.com", "https://www.github.com", "https://www.stackoverflow.com"]

threads = []
for site in sites:
    thread = threading.Thread(target=acessar_site, args=(site,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("Todos os acessos aos sites foram concluídos.")



