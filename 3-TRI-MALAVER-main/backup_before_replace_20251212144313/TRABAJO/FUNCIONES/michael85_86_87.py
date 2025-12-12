# Ejercicio 1
def func85(s):
    david = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            david += 1
    return david

# Ejercicio 2
def func86(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    moreno = a
    return moreno

# Ejercicio 3
def func87(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    nieto = x
    return nieto

