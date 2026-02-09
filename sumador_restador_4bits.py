
# Puertas lógicas permitidas

def AND(a, b):
    return a & b

def OR(a, b):
    return a | b

def NOT(a):
    return 1 - a
# XOR construido solo con AND, OR, NOT
# XOR = (A OR B) AND NOT(A AND B)

def XOR(a, b):
    return AND(OR(a, b), NOT(AND(a, b)))
# Sumador completo (Full Adder)
def full_adder(a, b, cin):
    s1 = XOR(a, b)
    suma = XOR(s1, cin)

    c1 = AND(a, b)
    c2 = AND(s1, cin)
    carry = OR(c1, c2)

    return suma, carry

# Sumador de 4 bits

def sumador_4_bits(A, B):
    resultado = [0, 0, 0, 0]
    carry = 0

    for i in range(3, -1, -1):
        resultado[i], carry = full_adder(A[i], B[i], carry)

    return resultado, carry


# Restador de 4 bits (A - B)
# Usando complemento a 2


def restador_4_bits(A, B):
    B_invertido = [NOT(b) for b in B]
    uno = [0, 0, 0, 1]

    B_complemento, _ = sumador_4_bits(B_invertido, uno)
    resultado, carry = sumador_4_bits(A, B_complemento)

    return resultado, carry

# Ejemplo de prueba

A = [0, 1, 1, 0]  # 6 en binario
B = [0, 0, 1, 1]  # 3 en binario

suma, carry_suma = sumador_4_bits(A, B)
resta, carry_resta = restador_4_bits(A, B)

print("A =", A)
print("B =", B)
print("Suma =", suma, "Carry =", carry_suma)
print("Resta =", resta, "Carry =", carry_resta)
