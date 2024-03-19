def pertence_fibonacci(numero):
    a, b = 0, 1
    while a <= numero:
        if a == numero:
            return True
        a, b = b, a + b
    return False

numero = int(input("Informe um número: "))
if pertence_fibonacci(numero):
    print("O número informado pertence à sequência de Fibonacci.")
else:
    print("O número informado não pertence à sequência de Fibonacci.")
