# Bucle While

i = 1
while i <=10:
    # Para incluir las variables dentro del texto entre comillas dobles
    # lo indicamos al principio con f de formateo y la variable entre llaves
    print(f"El valor de i es : {i}")
    i +=1
    if i ==5:
        break


i = 1
while i <=10:
    i +=1
    if i ==4:
        continue #Se salta el resto de código y vuelve al principio del bucle
    print(f"El valor de i es : {i}")