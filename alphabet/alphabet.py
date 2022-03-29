import string

def count_letters(text):
    alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)
    return {j:text.count(j) for j in alphabet}




#"Practice python every day", P1, r2, a2, c2, t2, i1, e3, p1, y3, h1, o1, n1, v1, d1
