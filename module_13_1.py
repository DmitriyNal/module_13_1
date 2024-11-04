import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соервнование')
    for ball in range(1, 6):
        print(f'Силач {name} поднял {ball} шар')
        await asyncio.sleep(1/power)
    print(f'Силач {name} закончил соервнование')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Артём', 7))
    task2 = asyncio.create_task(start_strongman('Вадим', 10))
    task3 = asyncio.create_task(start_strongman('Сергей', 15))
    await task1
    await task2
    await task3

asyncio.run(start_tournament())




