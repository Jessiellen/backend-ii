######## EXEMPLO DA AULA #######

# import multiprocessing
# import time

# def compute_square(n):
#     time.sleep(1)  # Simulate a heavy computation
#     print(f"Square of {n} is {n*n}")

# if __name__ == "__main__":
#     numbers = [2, 3, 4, 5]
#     processes = []
#     for number in numbers:
#         p = multiprocessing.Process(target=compute_square, args=(number,))
#         processes.append(p)
#         p.start()
#     for p in processes:
#         p.join()



############# EXERCICIO ###################


# import multiprocessing

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# def calculate_factorial(n):
#     result = factorial(n)
#     print(f"The factorial of {n} is {result}")

# if __name__ == "__main__":
#     numbers = [5, 3, 7, 6]

    
#     processes = []

   
#     for number in numbers:
#         p = multiprocessing.Process(target=calculate_factorial, args=(number,))
#         processes.append(p)
#         p.start()  

    
#     for p in processes:
#         p.join()


# import multiprocessing


# def sum_of_squares(sublist):
#     return sum(x * x for x in sublist)

# if __name__ == "__main__":
    
#     numbers = [i for i in range(1, 21)]  

    
#     sublists = [numbers[i:i + 5] for i in range(0, len(numbers), 5)] 

    
#     with multiprocessing.Pool() as pool:
#         results = pool.map(sum_of_squares, sublists)

    
#     for i, result in enumerate(results):
#         print(f"Sum of squares of sublist {i + 1}: {result}")

######## USANDO URLS ########


# import multiprocessing
# import time

# def realizar_download(url):
#     print(f"Iniciando download de: {url}")
#     time.sleep(10)  
#     print(f"Download de {url} concluído!")

# urls = ["https://site1.com", "https://site2.com", "https://site3.com"]

# if __name__ == "__main__":
#     with multiprocessing.Pool() as pool:
#         pool.map(realizar_download, urls)  
#     print("Todos os downloads foram concluídos.")


####### USANDO O REQUEST #########

import requests

def acessar_site(url):
    print(f"Iniciando acesso ao site: {url}")
    response = requests.get(url)  
    if response.status_code == 200:
        print(f"Redirecionamento para {url} concluído! Status: OK")
    else:
        print(f"Falha ao acessar {url}. Status: {response.status_code}")

sites = ["https://www.google.com", "https://www.github.com", "https://www.stackoverflow.com"]

for site in sites:
    acessar_site(site)

