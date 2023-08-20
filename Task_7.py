# Напишите программу на Python, которая будет находить
# сумму элементов массива из 1000000 целых чисел.
# Пример массива: arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, ...]
# Массив должен быть заполнен случайными целыми числами
# от 1 до 100.
# При решении задачи нужно использовать многопоточность,
# многопроцессорность и асинхронность.
# В каждом решении нужно вывести время выполнения
# вычислений.

from random import randint
import asyncio
import time

start = time.time()

arr = [randint(1, 100) for _ in range(10**6)]

sum_num = 0

async def sum_num_arr(arr, start, end):
    global sum_num
    for i in range(start, end):
        sum_num += arr[i]

async def main():
    tasks = []
    for i in range(10):
        start_index = i*100_000
        end_index = start_index + 100_000
        task = asyncio.create_task(sum_num_arr(arr, start_index, end_index))
        tasks.append(task)

    await asyncio.gather(*tasks)

    print('Завершение выполнения потоков')
    print('Результат:', sum_num)

    end = time.time()
    print('Время выполнения:', end - start)

if __name__ == '__main__':
    asyncio.run(main())