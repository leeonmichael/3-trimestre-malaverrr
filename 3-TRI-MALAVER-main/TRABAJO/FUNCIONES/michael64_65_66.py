# Ejercicio 1
def func64(n):
    david = 1
    i = 1
    while i<=n:
        david *= i
        i += 1
    return david

# Ejercicio 2
def func65(s):
    moreno = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            moreno += 1
    return moreno

# Ejercicio 3
def func66(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    nieto = a
    return nieto

