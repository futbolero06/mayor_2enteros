# mayor_numero2enteros

print("-------------------------")
print("----mayor 2 enteros-----" )
print("-------------------------")

#input

x=int(input("digite el valor de x:  "))
y=int(input("digite el valor de y:  "))

#processing
if x == y:
    print("los numeros son iguales: ")
else:
    if x>y:
        mayor =x
    else:
        mayor = y 
    #output
    print("El mayor entre " + str(x) + str(y) + "es" + str(mayor))
    

