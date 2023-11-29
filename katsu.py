def karatsuba(x, y):
  # Caso base para a multiplicação de números pequenos
  if x < 10 or y < 10:
      return x * y

  # Determina o número de dígitos dos números de entrada
  n = max(len(str(x)), len(str(y)))
  n2 = n // 2

  # Divide os números em duas metades
  a = x // 10 ** (n2)
  b = x % (10 ** (n2))
  c = y // 10 ** (n2)
  d = y % (10 ** (n2))

  # Calcula os produtos recursivamente
  ac = karatsuba(a, c)
  bd = karatsuba(b, d)
  ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

  # Retorna o resultado
  return ac * 10 ** (2 * n2) + (ad_plus_bc * 10 ** (n2)) + bd

# Teste
num1 = 123456789
num2 = 987654321

resultado = karatsuba(num1, num2)
print(f'O resultado da multiplicação é: {resultado}')
def karatsuba(x, y):
  # Caso base para a multiplicação de números pequenos
  if x < 10 or y < 10:
      return x * y

  # Determina o número de dígitos dos números de entrada
  n = max(len(str(x)), len(str(y)))
  n2 = n // 2

  # Divide os números em duas metades
  a = x // 10 ** (n2)
  b = x % (10 ** (n2))
  c = y // 10 ** (n2)
  d = y % (10 ** (n2))

  # Calcula os produtos recursivamente
  ac = karatsuba(a, c)
  bd = karatsuba(b, d)
  ad_plus_bc = karatsuba(a + b, c + d) - ac - bd

  # Retorna o resultado
  return ac * 10 ** (2 * n2) + (ad_plus_bc * 10 ** (n2)) + bd

# Teste
num1 = 123456789
num2 = 987654321

resultado = karatsuba(num1, num2)
print(f'O resultado da multiplicação é: {resultado}')
