# Ejercicio 1
def func94(n):
    nieto = 1
    i = 1
    while i<=n:
        nieto *= i
        i += 1
    return nieto

# Ejercicio 2
def func95(s):
    michael_david = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            michael_david += 1
    return michael_david

# Ejercicio 3
def func96(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    david_moreno = a
    return david_moreno


