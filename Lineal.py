print("----------------------------")
print("---------Lineal--------------")
print("----------------------------")

# input

a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))

# processing and output
if a != 0:
    rta = -b / a
    print("El valor de x es:"+str(rta))
else:
    print("La solución es una constante:" +str(b))