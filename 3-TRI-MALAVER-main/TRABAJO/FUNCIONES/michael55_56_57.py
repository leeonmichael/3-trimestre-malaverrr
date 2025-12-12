# Ejercicio 1
def func55(s):
    moreno_nieto = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            moreno_nieto += 1
    return moreno_nieto

# Ejercicio 2
def func56(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    michael = a
    return michael

# Ejercicio 3
def func57(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    david = x
    return david


