"""
Лабораторная работа №1
Структуры данных
Тема: Поиск минимальной степени числа
"""

from collections import Counter

def factorize(x):
    """Разложение числа на простые множители"""
    factors = Counter()
    d = 2
    while d * d <= x:
        while x % d == 0:
            factors[d] += 1
            x //= d
        d += 1 if d == 2 else 2
    if x > 1:
        factors[x] += 1
    return factors

def solve():
    A, B = map(int, input().split())
    
    factors_A = factorize(A)
    factors_B = factorize(B)
    
    # Проверка возможности
    for p in factors_A:
        if p not in factors_B:
            return -1
    
    # Поиск минимальной степени
    max_n = 0
    for p, exp_a in factors_A.items():
        exp_b = factors_B[p]
        n = (exp_a + exp_b - 1) // exp_b  # ceil деление
        max_n = max(max_n, n)
    
    return max_n

if __name__ == "__main__":
    print(solve())
