import numpy as np
from matplotlib import pyplot

def f(x):
    return 2 + np.sin(x) - x            ##defino la funcion f(x)

def g(x):
    return 2 + np.sin(x)                ##Defino la funcion g(x) despejando x de f(x)


tolerancia = 10**(-5)
n_iteraciones = 0

a = 0                                   ##inicializo las variables a y b en 0
b = 0

valores = []

errores = []

rango = range(-30,100)                     #Definimos un rango de numeros sobre los cuales el 
                                        #for va a iterar para encontrar el rango efectivo

for i in rango:     

    if(f(i) < 0 and a == 0):            #Si el valor de f(i) es negativo, se guarda y si es
                                        #positivo,se guarda como el otro extremo del intervalo
        a = i
    
    if(f(i) > 0 and b == 0):
        b = i


                                        ## una vez definino del intervalo efectivo (con cambio de signo)
                                        ## se procede a realizar el metodo de punto fijo iterando sobre g(x)



valores.append(a)
error = np.abs(g(a) - a)
errores.append(error)


while(error > tolerancia and n_iteraciones < 10000):
    
    n_iteraciones = n_iteraciones + 1

    a = g(a)
    valores.append(a)
    
    error = np.abs(g(a) - a)
    errores.append(error)

    
    

print("El resultado es ",a,"en ",n_iteraciones," Iteraciones")

pyplot.plot(range(1,64),errores)  
pyplot.show()

pyplot.plot(range(1,64),valores)
pyplot.show()

for i in range(63):
    print("| Valor ",valores[i],"| Error ",errores[i],"|","Iteracion ",i,"|")
