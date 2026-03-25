# Лабораторная работа №1
## Структуры данных

---

##  Задание

<img width="1112" height="600" alt="image" src="https://github.com/user-attachments/assets/443f9e88-2bc0-4f1b-975a-9ea36921f248" />


---

##  Листинг программы

```python
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
    
    # Проверка, что все простые множители A содержатся в B
    for p in factors_A:
        if p not in factors_B:
            return -1
    
    # Поиск минимальной степени n
    max_n = 0
    for p, exp_a in factors_A.items():
        exp_b = factors_B[p]
        n = (exp_a + exp_b - 1) // exp_b  # ceil(exp_a / exp_b)
        max_n = max(max_n, n)
    
    return max_n

if __name__ == "__main__":
    print(solve())

---
```
## ✅ Результат выполнения программы

### Входные данные:

<img width="712" height="65" alt="image" src="https://github.com/user-attachments/assets/b7de2d8f-6b7d-496e-95df-e0a1d7c943fd" />


```
```
### Ход решения:
```
- A = 54 = 2¹ × 3³
- B = 60 = 2² × 3¹ × 5¹
- Для p = 2: n = ceil(1/2) = 1
- Для p = 3: n = ceil(3/1) = 3
- Ответ: max(1, 3) = 3

```
### Выходные данные:

<img width="751" height="62" alt="image" src="https://github.com/user-attachments/assets/9e6eba3c-6a5b-4d14-bde9-67129e482b30" />

```

