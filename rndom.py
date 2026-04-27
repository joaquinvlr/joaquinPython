


import time
import random


# num=random.randint(1, 10)
# print(num)


# num=random.randint(1, 10)
# for i in range(num):
#     print("hola padre")


# strike=random.randint(10, 70)

# if strike>50:
#     print("daño critico. daño ", strike)
# else:
#     print("no muy efectivo. daño", strike)


## 3 personas juegan golf
## cada persona tiene la posibilidad de golpear
## y la distancia varia entre 60 y 100
## mostrar al final, el golpe mas fuerte

# player1=random.randint(60, 100)
# player2=random.randint(60, 100)
# player3=random.randint(60, 100)

# print("la distancia del jugador 1 es de: ", player1)
# print("la distancia del jugador 2 es de: ", player2)
# print("la distancia del jugador 3 es de: ", player3)

# if player1>player2 and player1>player3:
#     print("el jugador 1 gano")
# elif player2>player3:
#         print("el jugador 2 gano")
# else:
#         print("el jugador 3 gano")

p1=input("ingrese el nombre del peleador 1 ")
p2=input("ingrese el nombre del peleador 2 ")
hp1=100
hp2=100
turno=random.randint(1,2)


while hp1>0 and hp2>0:
  if turno%2==0:
       print(f"turno de {p1}")
       atk=random.randint(7, 18)
       print(f"{p1} ataca con {atk}")
       hp2-=atk
       print(f"el hp de {p2} es de {hp2}")
       time.sleep(1)
  else:
       print(f"turno de {p2}")
       atk=random.randint(7, 18)
       print(f"{p2} ataca con {atk}")
       hp1-=atk
       print(f"el hp de {p1} es de {hp1}")
       time.sleep(1)

if hp1>hp2:
    print("el ganador es ", p1)
else:
    print("el ganador es ", p2)