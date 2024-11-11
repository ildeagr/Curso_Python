#Definir una funcion
#Sin parámetros
def calularIVA():
    importe = int(input("Precio del producto:"))
    total = importe*1.21
    print("Iva incluido (21%)", total)

calularIVA()

#Con parámetros
def calularIVA(importe):
    print("\nPrecio del producto:", importe)
    total = importe*1.21
    print("Iva incluido (21%)", total)

calularIVA(600)

#Con retorno de valores
def calularIVA(importe):
    print("\nPrecio del producto:", importe)
    total = importe*1.21
    return total

resultado = calularIVA(600)
print("Iva incluido (21%)", resultado)

#Con retorno de varios valores
def calularIVA(importe):
    total = importe*1.21
    return importe,total

precio,resultado = calularIVA(600)
print(f"\nEl precio sin IVA:", precio,"\nIva incluido (21%)", resultado)