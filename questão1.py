import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-1, 4, 400)


conjunto_fechado = (0 <= x) & (x <= 1) 
conjunto_aberto = (2 < x) & (x < 3) 

plt.figure(figsize=(8, 4))

plt.plot(x[conjunto_fechado], x[conjunto_fechado], 'go-', label='Conjunto Fechado [0, 1]', markersize=5)

plt.plot(x[conjunto_aberto], x[conjunto_aberto], 'bo', label='Conjunto Aberto (2, 3)', markersize=5)

plt.plot(2, 2, 'ro', label='Limite do Conjunto Aberto', markersize=8, fillstyle='none')
plt.plot(3, 3, 'ro', markersize=8, fillstyle='none')

plt.title('Representação de Conjuntos Abertos e Fechados no Eixo Real')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.xlim(-1, 4)
plt.ylim(-0.5, 3)
plt.legend()
plt.grid(True)

plt.show()
