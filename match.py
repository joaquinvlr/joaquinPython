

op=0
cantpersonas=0
total=0
while op!=4:
    print('''
          1. Niño (1-17) $1000
          2. Adulto (18-64) $3000
          3. Adulto mayor (65+) $1500
          4. Salir''')
    op=int(input("Seleccione una opcion:"))
    match op:
        case 1:
            print("Pagando el precio de niño")
            cantpersonas+=1
            total+=1000
        case 2:
            print("Pagando el precio de adulto")
            cantpersonas+=1
            total+=3000
        case 3:
            print("Pagando el precio de adulto mayor")
            cantpersonas+=1
            total+=1500
        case 4:
            print("Saliendo del programa")
            print(f"El total a pagar es: {total}")
            print(f"La cantidad de personas es {cantpersonas}")

        case _:
            print("Opcion invalida")




folio=int(input("ingrese su folio: "))
while folio<7000 or folio>21000:
    print("folio fuera de rango")
    folio=int(input("ingrese su folio: "))

cancha=int(input(''' Cual cancha es?
                 1. VIP
                 2. General
                 3. Trbuna'''))

match cancha:
    case 1:
        print(f"su total a pagar es: {40000*1.8}")
    case 2: 
        print(f"su total a pagar es: {40000*1.4}")
    case 3:
        print(f"su total a pagar es: {40000*1.2}")
    case _:
        print("Opcion invalida")
