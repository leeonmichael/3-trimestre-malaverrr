# Ejercicio 1
def func88(lst):
    michael_david = []
    for x in lst:
        if x not in michael_david:
            michael_david.append(x)
    return michael_david

# Ejercicio 2
def func89(s):
    david_moreno = ''.join(ch for ch in s if ch.isalpha())
    return david_moreno

# Ejercicio 3
def func90(lst):
    moreno_nieto = sorted(lst)
    return moreno_nieto


