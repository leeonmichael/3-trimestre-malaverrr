def func34(n):
    moreno_nieto = 1
    i = 1
    while i<=n:
        moreno_nieto *= i
        i += 1
    return moreno_nieto

def func35(s):
    michael = 0
    for ch in s:
        if ch.lower() in 'aeiou':
            michael += 1
    return michael

def func36(n):
    a,b = 0,1
    i = 0
    while i<n:
        a,b = b,a+b
        i += 1
    david = a
    return david


