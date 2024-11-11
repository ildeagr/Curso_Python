# Calculo del dia de la semana de una fecha

semana = ("Sábado","Domingo","Lunes", "Martes","Miercoles","Jueves","Viernes")
print("Vamos a calcular el día de la semana de tu nacimiento, por favor:")
day = int(input("Introduce su día de nacimiento: "))
month = int(input("Introduce su mes de nacimiento: "))
year = int(input("Introduce su año de nacimiento: "))

#Ajuste de meses Enero y Febrero
if(month==1):
    month=13
    year-=1
elif(year==2):
    montn=14
    year -=1

#Calculo del día
temp1 =int(((month+1)*3)/5)
temp2 =int(year/4)
temp3 =int(year/100)
temp4 =int(year/400)
temp5 =int(day+(month*2)+year+temp1+temp2-temp3+temp4+2)
temp6 =int(temp5/7)
temp7 =int(temp5-(temp6*7))

print(f"El día de la semana de tu nacimiento fue: {semana[temp7]}")