# Sumador-de-4-bits

Sumador y Restador Binario de 4 Bits en Python

Descripción general
Este proyecto implementa un sumador y un restador binario de 4 bits utilizando exclusivamente puertas lógicas AND, OR y NOT, simuladas en Python. No se emplean operadores aritméticos ni operadores lógicos avanzados. El objetivo es modelar el funcionamiento de circuitos digitales reales, tal como se hace en diseño de hardware.

El sistema reproduce un sumador completo, un sumador ripple-carry de 4 bits y una resta mediante complemento a 2.

Objetivo
Demostrar que las operaciones aritméticas binarias pueden construirse únicamente a partir de puertas lógicas básicas, replicando el comportamiento de circuitos combinacionales.

Objetivos específicos

* Implementar puertas AND, OR y NOT
* Construir XOR usando solo AND, OR y NOT
* Diseñar un sumador completo (Full Adder)
* Implementar un sumador de 4 bits encadenando sumadores completos
* Realizar la resta binaria usando complemento a 2

Finalidad
Proyecto orientado a fines académicos, especialmente en cursos de Lógica Digital, Arquitectura de Computadores y Sistemas Digitales. El enfoque es conceptual y educativo, no de optimización.

Fundamento teórico
El sumador completo recibe dos bits y un acarreo de entrada, y genera un bit de suma y un acarreo de salida.
Un sumador de 4 bits se construye encadenando cuatro sumadores completos.
La resta se implementa usando complemento a 2:

A − B = A + (NOT(B) + 1)

De esta forma, el mismo circuito del sumador puede utilizarse para restar.

Estructura del proyecto

.
├── sumador_restador_4bits.py
├── README.md

Requisitos

* Python 3.7 o superior
* No se requieren librerías externas

Cómo ejecutar el programa

1. Clonar el repositorio
   git clone https://github.com/JulioCesarFlorezGuarnizo/Sumador-de-4-bits/edit/main

2. Entrar al directorio
   cd sumador-restador-4bits

3. Ejecutar el programa
   python sumador_restador_4bits.py

Formato de entrada
Los números binarios se representan como listas de 4 bits:

A = [0, 1, 1, 0]
B = [0, 0, 1, 1]

Cada elemento debe ser 0 o 1.
El bit menos significativo se encuentra al final de la lista.

Salida del programa
El programa muestra:

* Resultado de la suma
* Carry final de la suma
* Resultado de la resta
* Carry final de la resta

Ejemplo de salida:

A = [0, 1, 1, 0]
B = [0, 0, 1, 1]
Suma = [1, 0, 0, 1] Carry = 0
Resta = [0, 0, 1, 1] Carry = 1

Ejecución de pruebas
El archivo incluye un bloque de prueba directa. Para probar otros casos, basta con modificar las listas A y B y volver a ejecutar el programa.

Se recomienda probar:

* Sumas con overflow
* Restas con préstamo
* Casos límite como 0000 y 1111

Consideraciones importantes

* No se utilizan operadores aritméticos
* XOR está implementado solo con AND, OR y NOT
* El carry final indica overflow en la suma o préstamo en la resta
* El diseño es equivalente a un circuito combinacional real

Posibles extensiones

* Ampliación a más bits
* Implementación de banderas (signo, overflow)
* Representación gráfica del circuito lógico


