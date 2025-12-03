import asyncio

async def tarefa1():
    print("Tarefa 1 começou")
    await asyncio.sleep(2)  # Simula I/O assíncrono (delay de 2s)
    print("Tarefa 1 terminou")

async def tarefa2():
    print("Tarefa 2 começou")
    await asyncio.sleep(1)
    print("Tarefa 2 terminou")

async def main():
    # Roda as tarefas em paralelo
    await asyncio.gather(tarefa1(), tarefa2())

# Roda o loop de eventos
asyncio.run(main())