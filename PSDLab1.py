# -*- coding: utf-8 -*-
"""
Autoras:
    Mariana Garcia Trujillo
    Sara Mariana Pinzon Rodriguez
"""

#Librerias

import wfdb
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.stats import variation



"""Asegurese de que el los archivos .dat y .hea esten descargados y en
la misma carpeta en la que se encuentra este archivo
"""

#se usa el 'record' de la libreria wdfb para utilizar la senal que contiene
# el archivo
senal = wfdb.rdrecord('rec_1')

print("")

print("Cantidad de senales en el archivo:", senal.n_sig)

print("")

"""En este archivo hay 2 senales (columnas) por lo que solo vamos a seleccionar
la primera para trabajar con ella, y se guardara en la variable: valores """

valores = senal.p_signal[:,1]

#grafica de la señal seleccionada
plt.plot(valores)
plt.title(' Señal ECG filtrada paciente 1')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')
plt.tight_layout()
plt.show()


"""PUNTO 1"""

print("PUNTO 1")

print("A) MEDIA DE LA SEÑAL")

#usando parametro de Numpy
media1 = np.mean(valores)
print("Media de datos con Numpy:", media1, "mV")


#Programando la formula desde cero
suma = 0 
datos = len(valores) #dice la cantidad de datos 'n' de la senal

#se utiliza un for para que recorra los valores de la senal con el contador i
# por cada instante de tiempo, y se van acumulando en 'suma'

for i in valores:
    suma += i
    
media2 = suma / datos    

print("Media de datos programando desde 0:", media2 , "mv")


print(" ")
print("B) DESVIACION ESTANDAR")

# usando parametro de Numpy
desviacion1 = np.std(valores)
print("Desviacion estandar con Numpy: ", desviacion1)

# Programandola desde 0 
suma_dat = 0
n = len(valores)

#Se usa el for para e recorridode todos los datos usando el contador e, se hace
#la suma de cada uno de los datos restados al promedio y elevados al cuadrado, y
# se almacena en la variable 'suma_dat'

for e in valores:
    suma_dat += (e - media2)**2

varianza = suma_dat / n

desviacion2 = math.sqrt(varianza)
print("Desviacion estandar desde 0: ", desviacion2)

print(" ")
print("C) COEFICIENTE DE VARIACION")

#Usando parametro de Scipy.stats 
CoefVar1 = variation(valores)
CoefVar1 = abs(CoefVar1)
CoefVar1 =  CoefVar1 *100
print("Coeficiente de variacion con Scipy: ", CoefVar1 , "%")

#Programando desde 0 
CoefVar2 = np.abs(desviacion1 / media1)
CoefVar2 = CoefVar2 *100
print("Coeficiente de variacion desde 0: ", CoefVar2,"%")

print(" ")
print("D) HISTOGRAMAS")

#usando matplotlib
clase = 1 + (math.log(len(valores))/math.log(2))
int_clase = int (clase)

print ("Numero de clase (barras): ", clase)

n, bins, patches = plt.hist(valores, bins = int_clase , edgecolor='blue')
#En donde: 
#n: las frecuencias normalizadas
# bins: los bordes de los bins
# patches: los objetos gráficos del histograma representa elementos graficos (rectangulos)

plt.title('Histograma de senal')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()

""" E)FUNCION DE PROBABILIDAD")""" 

#calular el centro de los bints
bin_centers = (bins[:-1] + bins[1:]) / 2

#graficar funcion
plt.hist(valores, bins = int_clase , edgecolor='blue')
plt.plot(bin_centers, n, '-', color='r', label='Función de probabilidad')

plt.title('Histograma de senal con función de probabilidad')
plt.xlabel('Valor')
plt.ylabel('Frecuencia')
plt.tight_layout()
plt.show()




"""PUNTO 2"""





print(" ")
print("PUNTO 2")

print(" ")


print("a. RUIDO GAUSSIANO")


print("SNR 1: ruido gaussiano potencia de señal > potencia de ruido")
#SNR potencia de señal mayor a potencia de ruido
"""SE VA A GENERAR PRIMERO UNA POTENCIA DE RUIDO MENOR A LA POTENCIA DE LA SENAL
EN DONDE EL SNR DEBE DE SER UN VALOR POSITIVO"""

#generando la senal de ruido
sigma = 1
tamano = len(valores)

ruido_G_a = (np.random.normal(0, sigma , tamano))*0.01

#Superposicion de señal original con senal con ruido
senal_con_ruido = valores + ruido_G_a

# 1)Calcular potencia de la señal
sumadad = 0
n = len(valores) #tamaño del vector que contiene la señal original

for d in valores:
    sumadad += (d)**2

potencia_señal= sumadad / n

print("Potencia de la señal =", potencia_señal)

#2)Calculo potencia del ruido
suma_ruido1 = 0
n = len(ruido_G_a)

for d in ruido_G_a:
    suma_ruido1 += (d)**2

potencia_ruido1= suma_ruido1 / n

print("Potencia del ruido =", potencia_ruido1 )

#3) SNR
snr_1_a = 10*math.log10(potencia_señal / potencia_ruido1)
print("SNR 1  = ", snr_1_a, "dB")


"""GRAFICAS"""

#Subplot con señal original
plt.subplot(3,1,1)
plt.plot(valores)
plt.title(' Señal ECG filtrada paciente 1')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

#subplot con ruido Gaussiano
plt.subplot(3,1,2)
plt.plot(ruido_G_a)
plt.title('Señal de ruido Gaussiano')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')


#graficando la senal original con ruido
plt.subplot(3,1,3)
plt.plot(senal_con_ruido)
plt.title('Señal con ruido SNR POSITIVO')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')
plt.tight_layout()
plt.show()



print(" ")

print("SNR 2: ruido gaussiano potencia de señal < potencia de ruido")

#SNR potencia de señal menor a potencia de ruido
"""SE VA A GENERAR PRIMERO UNA POTENCIA DE RUIDO MAYOR A LA POTENCIA DE LA SENAL
EN DONDE EL SNR DEBE DE SER UN VALOR NEGATIVO"""

#generando la señal de ruido
ruido_G_b = (np.random.normal(0, sigma , tamano))*100

#Superposicion de señal original con senal con ruido
senal_con_ruido_b = valores + ruido_G_b


#2)Calculo potencia del ruido
suma_ruido1 = 0
n = len(ruido_G_b)

for d in ruido_G_b:
    suma_ruido1 += (d)**2

potencia_ruido1= suma_ruido1 / n

print("Potencia del ruido =", potencia_ruido1 )

# 3) SNR
snr_1_b = 10*math.log10(potencia_señal / potencia_ruido1)

print("SNR 2 = ", snr_1_b, "dB")

"""GRAFICAS """

#Subplot con señal original
plt.subplot(3,1,1)
plt.plot(valores)
plt.title(' Señal ECG filtrada paciente 1')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

#Subplot con nuevo ruido Gaussiano
plt.subplot(3,1,2)
plt.plot(ruido_G_b)
plt.title('Señal de rudio Gaussiano')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')

#Subplot de señal original con ruido Gaussiano
plt.subplot(3,1,3)
plt.plot(senal_con_ruido_b)
plt.title('Señal con rudio SNR NEGATIVO')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')

plt.tight_layout()
plt.show()


#b) Ruido tipo impulso
print(" ")
print("b) RUIDO TIPO IMPULSO")

print("")

print("SNR 1 = P. señal > P. ruido impulso")

#generacion de la señal  de ruido impulso

prob = 0.05 # 5% de probabilidad de que un punto sea impulso

ruido = np.random.choice([0,1], size = len(valores), p = [1-prob, prob])
amplitud = np.random.normal(0,1, size = len(valores))*0.01
senal_ruido_impulso_a = ruido * amplitud

#superpoicion con la senal original
senal_cont_impul1 = valores + senal_ruido_impulso_a


"""CALCULO DEL SNR 1"""

#calculo de la potencia del ruido impulso
suma_ruido2 = 0
n = len(senal_ruido_impulso_a)

for d in senal_ruido_impulso_a:
    suma_ruido2 += (d)**2

potencia_ruido2_a= suma_ruido2 / n

print("Potencia del ruido =", potencia_ruido2_a )
print("Potencia señal original =", potencia_señal )

#como la potencia de la señal original ya se calculo, no se vuelve a colocar

snr_2_a = 10*math.log10(potencia_señal / potencia_ruido2_a)

print("SNR 1 = ", snr_2_a, "dB")



"""GRAFICAS """

#Subplot con señal original
plt.subplot(3,1,1)
plt.plot(valores)
plt.title(' Señal ECG filtrada paciente 1')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

#Subplot señal con ruido
plt.subplot(3,1,2)
plt.plot(senal_ruido_impulso_a)
plt.title('Señal con ruido impulso')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')

#Señal original contaminada con ruido impulso
plt.subplot(3,1,3)
plt.plot(senal_cont_impul1)
plt.title('Señal ECG con SNR positivo')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')

plt.tight_layout()
plt.show()




print(" ")
print("SNR 2  = P. señal < P. ruido impulso")

#generacion de la señal  de ruido impulso
prob = 0.05 # 5% de pobabilidad de que un punto sea impulso

ruido = np.random.choice([0,1], size = len(valores), p = [1-prob, prob])
amplitud = np.random.normal(0,1, size = len(valores))*100
senal_ruido_impulso_b = ruido * amplitud


#superpoicion con la senal original
senal_cont_impul2 = valores + senal_ruido_impulso_b


"""CALCULO DEL SNR 2"""

#calculo de la potencia del ruido impulso
suma_ruido2 = 0
n = len(senal_ruido_impulso_b)

for d in senal_ruido_impulso_b:
    suma_ruido2 += (d)**2

potencia_ruido2_b= suma_ruido2 / n

print("Potencia del ruido =", potencia_ruido2_b )
print("Potencia señal original =", potencia_señal )

#como la potencia de la señal original ya se calculo, no se vuelve a colocar

snr_2_b = 10*math.log10(potencia_señal / potencia_ruido2_b)

print("SNR 2 = ", snr_2_b, "dB")


"""GRAFICAS """

#Subplot con señal original
plt.subplot(3,1,1)
plt.plot(valores)
plt.title(' Señal ECG filtrada paciente 1')
plt.xlabel('Tiempo (s)')
plt.ylabel('Voltaje (mV)')

#Subplot de la señal con ruido impulso
plt.subplot(3,1,2)
plt.plot(senal_ruido_impulso_b)
plt.title('Señal con ruido impulso')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')

#Subplot contaminada con ruido impulso
plt.subplot(3,1,3)
plt.plot(senal_cont_impul2)
plt.title('Señal ECG con SNR negativo')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV')

plt.tight_layout()
plt.show()

print(" ")

print("c. RUIDO TIPO ARTEFACTO")


print("SNR 1: potencia de señal > potencia de ruido")
#SNR potencia de señal mayor a potencia de ruido

"""SE VA A GENERAR PRIMERO UNA POTENCIA DE RUIDO MENOR A LA POTENCIA DE LA SENAL
EN DONDE EL SNR DEBE DE SER UN VALOR POSITIVO"""

# 1) frecuencia de muestreo
fs = 100
#segundos
duration = 100
#tiempo de muestreo desde 0 a 1 segundo 
t = np.linspace(0, duration, fs * duration)*0.01
#frecuenia de la señal Hz
f = 2

#cantidad de picos de ruido
num_impulses = 5
#Amplitud
impulse_amplitude = 0.001
#lea t y ubique los picos aleatoriamente
impulse_positions = np.random.choice(np.arange(len(t)), num_impulses, replace=False)

impulse_noise = np.zeros_like(t)
impulse_noise[impulse_positions] = impulse_amplitude

# Contaminar la señal con el ruido de impulsos
ruido_t_a = valores + impulse_noise

#2)Calculo potencia del ruido

suma_ruido3 = 0
n = len(ruido_t_a)

for p in ruido_t_a:
    suma_ruido3 += (p)**2

potencia_ruido3= suma_ruido3 / n

print("Potencia del ruido tipo artefacto =", potencia_ruido3 )

#3) SNR

snr_3_a = 10*math.log10(potencia_señal / potencia_ruido3)

print("SNR 1 = ", snr_3_a, "dB")

"GRAFICAS"

plt.subplot(3, 1, 1)
plt.plot(t, valores)
plt.title('Señal ECG filtrada paciente 1')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV)')

plt.subplot(3, 1, 2)
plt.stem(t, impulse_noise)
plt.title('Señal ruido tipo Artefacto')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV)')

plt.subplot(3, 1, 3)
plt.plot(t, ruido_t_a)
plt.title('Señal con ruido SNR positivo')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV)')

plt.tight_layout()
plt.show()


print("")

print("SNR 2: ruido tipo artefacto, potencia de señal < potencia de ruido")
#SNR potencia de señal mayor a potencia de ruido

"""AHORA SE VA A GENERAR UNA POTENCIA DE RUIDO MAYOR A LA POTENCIA DE LA SENAL
EN DONDE EL SNR DEBE DE SER UN VALOR NEGATIVO"""

# 1) frecuencia de muestreo
fs = 100
#segundos
duration = 100
#tiempo de muestreo desde 0 a 1 segundo 
t = np.linspace(0, duration, fs * duration)*0.01
#frecuenia de la señal Hz
f = 2

#cantidad de picos de ruido
num_impulses = 5
#Amplitud
impulse_amplitude = 5
#lea t y ubique los picos aleatoriamente
impulse_positions = np.random.choice(np.arange(len(t)), num_impulses, replace=False)

impulse_noise = np.zeros_like(t)
impulse_noise[impulse_positions] = impulse_amplitude

# Contaminar la señal con el ruido de impulsos
ruido_t_a2 = valores + impulse_noise


#2)Calculo potencia del ruido

suma_ruido3 = 0
n = len(ruido_t_a2)

for U in ruido_t_a2:
    suma_ruido3 += (U)**2

potencia_ruido3= suma_ruido3 / n

print("Potencia del ruido tipo artefacto =", potencia_ruido3 )

#3) SNR

snr_3_b = 10*math.log10(potencia_señal / potencia_ruido3)

print("SNR 2 = ", snr_3_b, "dB")


"GRAFICAS"

plt.subplot(3, 1, 1)
plt.plot(t, valores)
plt.title('Señal ECG filtrada paciente 1')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV)')

plt.subplot(3, 1, 2)
plt.stem(t, impulse_noise)
plt.title('Señal ruido tipo Artefacto')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV)')

plt.subplot(3, 1, 3)
plt.plot(t, ruido_t_a2)
plt.title('Señal con ruido SNR negativo')
plt.xlabel('tiempo (s)')
plt.ylabel('Voltaje (mV)')

plt.tight_layout()
plt.show()























