
# while True:
#     try:
#         edad=int(input("ingrese su edad"))
#         break
    
#     except ValueError as e:
#         print("solo se aceptan numero ")
#         print(e)

# print("su edad es", edad)


for i in range(10):
    n1=int(input("ingrese un numero: "))
    if n1%2!=0:
        break


num=0
while True:
    try:
        n1=int(input("ingrese un numero: "))
        num+=n1
        if n1==0:
            break
    except:
        print("solo numeros enteros")

op=0
total=0
while op!=4:
    print("1. radio stereo sony $70000")
    print("2. LGTV 55 pulgadas suoer gamer $500000")
    print("3. PS5 $500000")
    print("4. salir")
    print("seleccione una opcion")
    op=int(input())
    match op:
        case 1:
            print("el precio a pagar es ", 70000*1.19)
            total=70000*1.19
        case 2: 
            print("el precio a pagar es ", 500000*1.19)
            total=500000*1.19
        case 3:
            print("el precio a pagar es ", 500000*1.19)
            total=500000*1.19
        case 4:
            print("total a pagar es ", total)
        case _:
            print("opcion invalida")



porc=float(input("ingrese el porcentaje de rucos en su comuna: "))

if porc<100 and porc>0:
    print("porcentaje correcto")
else:
    print("porcentaje fuera de rango")