# Calculo letra DNI
#Aplicamos el uso de substring para obtener la letra del DNI de la posicion correspondiente
tablaLetra = "TRWAGMYFPDXBNJZSQVHLCKET"
DNI = int(input("Introduce DNI sin letra: "))
resto = DNI%23

Letra = tablaLetra[resto]

print("Su valor clave es:",resto,"\nSu letra es:",Letra , ", por lo tanto su DNI completo es:", DNI,Letra)
