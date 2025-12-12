# Ejercicio 1
def func4(n):
    michael_david = 1
    i = 1
    while i<=n:
        michael_david *= i
        i += 1
    return michael_david

# Ejercicio 2
def func5(s):
    david_moreno = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            david_moreno += 1
    return david_moreno

# Ejercicio 3
def func6(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    moreno_nieto = a
    return moreno_nieto


