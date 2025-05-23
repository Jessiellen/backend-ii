import threading
import urllib.request

def download_file(url, filename):
    print(f"Iniciando download de {filename}")
    urllib.request.urlretrieve(url, filename)
    print(f"Concluído: {filename}")

urls = [
    ("https://upload.wikimedia.org/wikipedia/commons/3/3f/Fronalpstock_big.jpg", "imagem1.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/6/6e/Golde33443.jpg", "imagem2.jpg"),
    ("https://upload.wikimedia.org/wikipedia/commons/a/ae/Nature-wildlife-dog.jpg", "imagem3.jpg"),
]

threads = []

for url, name in urls:
    t = threading.Thread(target=download_file, args=(url, name))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Todos os downloads foram finalizados.")
