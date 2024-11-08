#Declaración de variables e impresion por terminal

#Por defecto no hace falta indicar el tipo de dato adquiere el tipo según la entrada del mismo
#En este caso se le indica dado que al introducirlo por teclado, por defecto lo guarda como String
print("**Promedio de varios números**")
num1=int(input("Primer numero: "))
num2=int(input("Segundo numero: "))
num3=int(input("Tercer numero: "))
resultado = (num1 + num2 + num3)/3

#Si redondeamos un número entero lo guarda con decimales por lo tanto lo almacena como float
print("El promedio es: ",round(resultado,2))
