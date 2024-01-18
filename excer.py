M = 2023

def compute(n):
  residuo = n % M
  s = ''
  for i in range(residuo):
    s = s + str(residuo)
    mod = int(s) % M
  return int(mod)

numbers = [1, 2, 5, 10, 20, 827785024886475841]

for num in numbers:
    result = compute(num)
    print(f"{num}: {result}")