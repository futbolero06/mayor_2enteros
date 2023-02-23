# mayor_numero2enteros

print("-------------------------")
print("----mayor 2 enteros-----" )
print("-------------------------")

#input

x=int(input("digite el valor de x:  "))
y=int(input("digite el valor de y:  "))

#processing
if x == y:
    print("los numeros son iguales... ")
else:
    if x>y:
        mayor =x
    else:
        mayor = y 
    #output
    print("----------------------------")
    print("-----el numero mayor es------")
    print("---------------------------")

    print("El mayor entre " + str(x) + " y " + str(y) + " es:  " + str(mayor))
    

