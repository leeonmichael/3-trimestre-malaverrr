# Ejercicio 1
def func73(s):
    nieto = s[::-1]
    return nieto

# Ejercicio 2
def func74(n):
    michael_david = 1
    i = 1
    while i<=n:
        michael_david *= i
        i += 1
    return michael_david

# Ejercicio 3
def func75(s):
    david_moreno = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            david_moreno += 1
    return david_moreno


