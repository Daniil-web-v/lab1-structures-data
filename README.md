# lab1-structures-data
# Лабораторная работа №1
## Структуры данных

---

## 📌 Задание

Даны два натуральных числа \( A \) и \( B \) (\( 2 \leq A, B \leq 2 \times 10^9 \)).  
Найдите такое минимальное натуральное \( n \), что \( B^n \) делится на \( A \).

**Входные данные:**  
Программа получает на вход два числа \( A \) и \( B \).

**Выходные данные:**  
Программа выводит одно значение \( n \). Если никакая степень числа \( B \) не делится на \( A \), то выведите число -1.

---

## 📷 Условие задачи

![Условие задачи](https://github.com/Danil-web-v/lab1-structures-data/blob/main/task.png)

*Если скриншот условия отсутствует, текст условия приведен выше*

---

## 💻 Реализация

### Листинг программы

```python
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
        n = (exp_a + exp_b - 1) // exp_b
        max_n = max(max_n, n)
    
    return max_n

if __name__ == "__main__":
    print(solve())
