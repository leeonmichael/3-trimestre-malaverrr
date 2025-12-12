# Ejercicio 1
def func43(s):
    david = s[::-1]
    return david

# Ejercicio 2
def func44(n):
    moreno = 1
    i = 1
    while i<=n:
        moreno *= i
        i += 1
    return moreno

# Ejercicio 3
def func45(s):
    nieto = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            nieto += 1
    return nieto

