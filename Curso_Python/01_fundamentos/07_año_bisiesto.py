#Calculo de año bisiesto

fecha = int(input("Introduce año: "))
div100 =fecha%100

if fecha%4==0 and div100!=0:
    print("Año Bisiesto")
elif fecha%4==0 and div100==0 and fecha%400==0:
    print("Año Bisiesto")
else:
    print("Año no Bisiesto")
