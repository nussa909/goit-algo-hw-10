"""
Завдання 1

У конспекті ми розглянули приклад про розбиття суми на монети. Маємо набір монет [50, 25, 10, 5, 2, 1]. Уявіть, що ви розробляєте систему для касового апарату, яка повинна визначити оптимальний спосіб видачі решти покупцеві.
Вам необхідно написати дві функції для касової системи, яка видає решту покупцеві:
1. Функція жадібного алгоритму find_coins_greedy. Ця функція повинна приймати суму, яку потрібно видати покупцеві, і повертати словник із кількістю монет кожного номіналу, що використовуються для формування цієї суми. 
Наприклад, для суми 113 це буде словник {50: 2, 10: 1, 2: 1, 1: 1}. Алгоритм повинен бути жадібним, тобто спочатку вибирати найбільш доступні номінали монет.

2. Функція динамічного програмування find_min_coins. Ця функція також повинна приймати суму для видачі решти, але використовувати метод динамічного програмування, щоб знайти мінімальну кількість монет, необхідних для формування цієї суми. Функція повинна повертати словник із номіналами монет та їх кількістю для досягнення заданої суми найефективнішим способом. Наприклад, для суми 113 це буде словник {1: 1, 2: 1, 10: 1, 50: 2}
Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, базуючись на часі їх виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах. 
Висвітліть, як вони справляються з великими сумами та чому один алгоритм може бути більш ефективним за інший у певних ситуаціях. Свої висновки додайте у файл readme.md домашнього завдання."""

import time as tm

def time_tracker(func):
    def inner(number, coins):
        start = tm.time()
        res = func(number, coins)
        end = tm.time()
        print(f"Execution time: {(end - start)*1000:.3f}ms")
        return res
    return inner

@time_tracker
def find_coins_greedy(amount:int, coins) -> dict:
    result = {}

    if amount <= 0:
        return result

    rest = amount

    for coin in coins:
        coin_count = rest // coin

        if coin_count > 0:
            result.update({coin:coin_count})

        rest = rest % coin
        if rest == 0:
            break
    
    return result

@time_tracker
def find_min_coins(amount:int,coins):
    result = {}
    min_coins_required = [0] + [float("inf")] * amount
    last_coin_used = [0] * (amount+1)

    for s in range(1, amount + 1):
        for coin in coins:
            if s >= coin and min_coins_required[s-coin]+1 < min_coins_required[s]:
                min_coins_required[s] = min_coins_required[s-coin] + 1
                last_coin_used[s] = coin

    #print(min_coins_required)
    #print(last_coin_used)

    current_amount = amount
    while current_amount > 0:
        coin = last_coin_used[current_amount]
        result[coin] = result.get(coin,0) + 1
        current_amount = current_amount - coin

    return result


coins_1 = [50,25,10,5,2,1]
print("Greedy algorithm:",find_coins_greedy(113, coins_1))
print("Dynamic algorithm:",find_min_coins(113, coins_1))

print("Greedy algorithm:",find_coins_greedy(11113, coins_1))
print("Dynamic algorithm:",find_min_coins(11113, coins_1))

coins_2 = [10,6,1] 
print("Greedy algorithm:",find_coins_greedy(113, coins_2))
print("Dynamic algorithm:",find_min_coins(113, coins_2))