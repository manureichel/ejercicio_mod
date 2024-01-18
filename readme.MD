## Consigna: 
¿Serías capaz de decirnos cuál sería la salida del siguiente pseudocódigo? (asumiendo que la máquina posee los recursos necesarios para llevar a cabo su ejecución). Te pedimos que no olvides compartir con nosotros tu razonamiento y los pasos que seguiste para llegar a tu respuesta.

```
const M = 2023

funcion compute(n)
string s = ""
para i desde 1 hasta n
s = s + n
fin para
return convertir_a_numero(s) % M
fin funcion

para cada n en 1, 2, 5, 10, 20, 827785024886475841
imprimir(n + ": " + compute(n))
fin para
```

Las salidas esperadas de este pseudocódigo son:

| **Entrada**          | **Salida** |
|-----------------------|------------|
| 1                     | 1          |
| 2                     | 22         |
| 5                     | 934        |
| 10                    | 738        |
| 20                    | 1481       |
| 827785024886475841   | **?**          |

### Interpretación
Observando el pseudocódigo, la función `compute` es la que realiza la operación de interés. Toma un número `n` como parámetro, lo concatena `n veces` como string en `s` y con ese valor, una vez convertido a número nuevamente, se calcula el módulo con `M` (que es una constante y vale `2023`).

Escribiendo esa función en Python tenemos:

```python
def compute(n):
    s = ""
    for i in range(1, n + 1):
        s += str(n)
    return int(s) % M
```

El principal problema del código presentado es el costo computacional que tiene la concatenación de números particularmente grandes como lo es el caso incógnita.

### Resolución

Para poder calcular el módulo del número incógnita podemos encarar el problema teniendo en cuenta que en lugar de primero concatenar el número y calcular finalmente el módulo, podemos inicialemente calcular el módulo del número, cuyo resultado llamaremos residuo, e ir concatenando este resíduo y calculando el módulo del mismo con `N`. De esta manera se converge hacia el valor deseado. 

Como el divisor es `M = 2023`, entonces el módulo `n % M` estará en un rango `0 <= n % M < 2023`. Esto reduce considerablemente el costo computacional.

Podemos escribir lo descrito en la siguiente función de Python junto con los números de prueba:

```python
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
```

Ejecutando el programa se obtienen los siguientes resultados:

```bash
1: 1
2: 22
5: 934
10: 738
20: 1481
827785024886475841: 1074
```

Con lo cual el valor buscado incógnita es **1074**.