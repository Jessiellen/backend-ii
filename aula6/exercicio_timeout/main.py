import asyncio

async def tarefa(nome, tempo):
    print(f"{nome} iniciada, vai demorar {tempo} segundos.")
    await asyncio.sleep(tempo)
    print(f"{nome} finalizada.")
    return f"Resultado da {nome}"

async def executa_com_timeout(tarefas, timeout):
    tarefas_criadas = [asyncio.create_task(tarefa(nome, t)) for nome, t in tarefas]
    resultados = []

    for task in tarefas_criadas:
        try:
            resultado = await asyncio.wait_for(task, timeout=timeout)
            resultados.append(resultado)
        except asyncio.TimeoutError:
            task.cancel()
            print(f"Tarefa {task.get_coro().__name__} cancelada por timeout.")
            resultados.append(None)

    return resultados

async def main():
    tarefas = [
        ("Tarefa 1", 2),
        ("Tarefa 2", 5),
        ("Tarefa 3", 1),
    ]
    resultados = await executa_com_timeout(tarefas, timeout=3)
    print("Resultados:", resultados)

if __name__ == "__main__":
    asyncio.run(main())
