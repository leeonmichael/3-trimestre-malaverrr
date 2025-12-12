def func67(a,b):
    x = a
    y = b
    while y:
        x,y = y,x%y
    michael_david = x
    return michael_david

def func68(lst):
    david_moreno = []
    for x in lst:
        if x not in david_moreno:
            david_moreno.append(x)
    return david_moreno

def func69(s):
    moreno_nieto = ''.join(ch for ch in s if ch.isalpha())
    return moreno_nieto


