# Sumador y Restador Binario de 4 Bits  
Lenguajes de Programación y Transducción

Implementación de un **sumador y un restador binario de 4 bits** utilizando exclusivamente puertas lógicas AND, OR y NOT simuladas en Python.

---

## Problema: Sumador y Restador Binario de 4 Bits

### Descripción

Este proyecto implementa operaciones aritméticas binarias simulando circuitos digitales reales.  
No se utilizan operadores aritméticos (`+`, `-`) ni operadores lógicos avanzados.  
Todas las operaciones se construyen a partir de puertas AND, OR y NOT.

La resta se implementa mediante **complemento a 2**, reutilizando el mismo sumador.

---

### Lógica general

- Cada número se representa como una lista de 4 bits `[b3, b2, b1, b0]`
- El bit menos significativo se encuentra al final
- El sumador de 4 bits se construye encadenando sumadores completos
- La resta se calcula como:

```
A − B = A + (NOT(B) + 1)
```

---

### Métodos

| Método | Descripción |
|--------|-------------|
| `AND(a, b)` | Puerta lógica AND |
| `OR(a, b)` | Puerta lógica OR |
| `NOT(a)` | Puerta lógica NOT |
| `XOR(a, b)` | XOR construido con AND, OR y NOT |
| `full_adder(a, b, cin)` | Sumador completo de un bit |
| `sumador_4_bits(A, B)` | Suma binaria de 4 bits |
| `restador_4_bits(A, B)` | Resta binaria de 4 bits |

---

### Uso

```python
from sumador_restador_4bits import sumador_4_bits, restador_4_bits

A = [0, 1, 1, 0]  # 6 en binario
B = [0, 0, 1, 1]  # 3 en binario

suma, carry_suma = sumador_4_bits(A, B)
resta, carry_resta = restador_4_bits(A, B)

print("Suma:", suma, "Carry:", carry_suma)
print("Resta:", resta, "Carry:", carry_resta)
```

---

### Salida esperada

```
Suma: [1, 0, 0, 1] Carry: 0
Resta: [0, 0, 1, 1] Carry: 1
```

---

### Consideraciones importantes

- No se utilizan operadores aritméticos
- XOR está construido únicamente con AND, OR y NOT
- El `carry` final indica overflow en la suma
- En la resta, el `carry` indica si hubo préstamo
- El diseño simula un circuito combinacional real

---

### Requisitos

- Python 3.7 o superior
- No se requieren librerías externas

---

### Cómo ejecutar el programa

```bash
python sumador_restador_4bits.py
```

---

### Ejecución de pruebas

Para probar distintos casos, modifica los valores de `A` y `B` dentro del archivo principal y vuelve a ejecutar el programa.

Se recomienda probar:

- Sumas con overflow
- Restas con préstamo
- Casos límite (`0000`, `1111`)

---
