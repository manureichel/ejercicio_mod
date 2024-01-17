M = 2023

def compute(n):
    s = ""
    for i in range(1, n + 1):
        s += str(n)
    return int(s) % M

n = 10
resultado = compute(n)

print(resultado)
