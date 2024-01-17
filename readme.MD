## Pseudocódigo a interpretar

### Consigna: 
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

Resultado parcial de la ejecución
1: 1
2: 22
5: 934
10: 738
20: 1481
827785024886475841: ???
```

