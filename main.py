import math
import numpy as np
import statistics as stats
from collections import Counter

# DATOS

data = [
    68,42,95,73,58,10,84,77,63,91,
    37,52,68,45,88,74,56,97,84,33,
    91,70,99,60,81,47,58,68,40,76,
    22,33,95,84,65,73,49,59,97,88,
    52,45,83,91,77,63,10,95,81,37,
    42,84,68,58,74,99,33,45,73,60
]

data_sorted = sorted(data)
n = len(data)
mean = sum(data)/n

# MEDIDAS DE CENTRALIZACIÓN

# mediana
median = (data_sorted[29] + data_sorted[30]) / 2

# moda(s)
counts = Counter(data)
maxfreq = max(counts.values())
modes = [k for k,v in counts.items() if v == maxfreq]

# MEDIDAS DE DISPERSIÓN

# varianzas y desviaciones estándar
pop_var = stats.pvariance(data)
samp_var = stats.variance(data)
std_pop = math.sqrt(pop_var)
std_samp = math.sqrt(samp_var)

# error estándar
se = std_samp / math.sqrt(n)

# coeficiente de variación
cv = std_samp / mean

# cuartiles e IQR
q1 = np.percentile(data, 25, interpolation='linear')
q2 = np.percentile(data, 50, interpolation='linear')
q3 = np.percentile(data, 75, interpolation='linear')
IQR = q3 - q1

# forma de la distribución

m2 = sum((x-mean)**2 for x in data) / n
m3 = sum((x-mean)**3 for x in data) / n
m4 = sum((x-mean)**4 for x in data) / n

skewness = m3 / (m2**1.5)
kurtosis_excess = m4 / (m2**2) - 3  # exceso de curtosis

# percentiles, deciles, cuartiles

percentiles = {p: float(np.percentile(data, p)) for p in [1,5,10,25,50,75,90,95,99]}
deciles = {d: float(np.percentile(data, d*10)) for d in range(1,10)}
quartiles = {1:q1, 2:q2, 3:q3}

# minimo y maximo

minv = min(data)
maxv = max(data)

# Resultados

print("Cantidad de datos:", n)
print("Media:", mean)
print("Mediana:", median)
print("Moda(s):", modes, "con frecuencia", maxfreq)

print("\n--- DISPERSIÓN ---")
print("Varianza poblacional:", pop_var)
print("Varianza muestral:", samp_var)
print("Desviación estándar:", std_samp)
print("Error estándar:", se)
print("Coeficiente de variación:", cv)

print("\n--- CUARTILES ---")
print("Q1:", q1)
print("Q2 (mediana):", q2)
print("Q3:", q3)
print("IQR:", IQR)

print("\n--- FORMA DE LA DISTRIBUCIÓN ---")
print("Asimetría (skewness):", skewness)
print("Curtosis (exceso):", kurtosis_excess)

print("\n--- PERCENTILES ---")
print(percentiles)

print("\n--- DECILES ---")
print(deciles)

print("\n--- MÍNIMO Y MÁXIMO ---")
print("Mínimo:", minv)
print("Máximo:", maxv)
