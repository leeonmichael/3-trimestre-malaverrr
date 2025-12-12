# Ejercicio 1
def func58(lst):
    moreno = []
    for x in lst:
        if x not in moreno:
            moreno.append(x)
    return moreno

# Ejercicio 2
def func59(s):
    nieto = ''.join(ch for ch in s if ch.isalpha())
    return nieto

# Ejercicio 3
def func60(lst):
    michael_david = sorted(lst)
    return michael_david


