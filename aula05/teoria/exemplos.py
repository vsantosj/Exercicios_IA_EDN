import random
import time

numero_aleatorios = random.randint(0,100)
print(f'Números aleatorios: {numero_aleatorios}')

inicio = time.time()
for _ in range (10000000):
    pass
fim = time.time()

print(f'tempo de execução: {fim - inicio:.6f} segundos')