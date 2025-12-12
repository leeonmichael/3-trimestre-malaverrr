def func28(lst):
    michael = []
    for x in lst:
        if x not in michael:
            michael.append(x)
    return michael

def func29(s):
    david = ''.join(ch for ch in s if ch.isalpha())
    return david

def func30(lst):
    moreno = sorted(lst)
    return moreno


