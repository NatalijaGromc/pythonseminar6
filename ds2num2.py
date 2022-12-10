# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

# *Пример:*
                                  
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def factorial(N):
    prod=1
    for i in range(1,N+1):
        prod=prod*i
    return prod

print('Введите число N: ')
N = int(input())
result = [factorial(i) for i in range(1,N+1)] # - применила list comprehension

print(result)