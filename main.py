import numpy as np
import matplotlib.pyplot as plt

# Parámetros del sistema
R = 1.0
gamma2 = 1.0

# Configuración temporal
t_max = 5.0
dt = 0.001
t = np.arange(0, t_max + dt, dt)

# Arreglos para guardar las poblaciones
N2 = np.zeros(len(t))
N1 = np.zeros(len(t))
inversion = np.zeros(len(t))

# Condiciones iniciales
N2[0] = 0.0
N1[0] = 1.0
inversion[0] = N2[0] - N1[0]

# Integración numérica con método de Euler
for i in range(len(t) - 1):
    dN2_dt = R * (N1[i] - N2[i]) - gamma2 * N2[i]
    N2[i + 1] = N2[i] + dN2_dt * dt
    N1[i + 1] = 1.0 - N2[i + 1]
    inversion[i + 1] = N2[i + 1] - N1[i + 1]

# Graficar poblaciones
plt.figure(figsize=(8, 5))
plt.plot(t, N1, label=r"$N_1(t)$")
plt.plot(t, N2, label=r"$N_2(t)$")
plt.xlabel("Tiempo")
plt.ylabel("Población")
plt.title("Sistema de dos niveles")
plt.legend()
plt.grid(True)
plt.show()

# Graficar inversión de población
plt.figure(figsize=(8, 5))
plt.plot(t, inversion, label=r"$N_2 - N_1$")
plt.xlabel("Tiempo")
plt.ylabel("Inversión")
plt.title("Inversión de población en sistema de dos niveles")
plt.legend()
plt.grid(True)
plt.show()