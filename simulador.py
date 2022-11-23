import time
import Archivos.combinaciones as combinaciones
import Archivos.movimientos as movimientos
import Archivos.golpes as golpes
import Archivos.narracion as narracion


def get_narracion(player,narraciones,movimiento,contador,tamanio_combinacion)->str:

    """funcion que recupera una narracion por movimiento y la de un orden segun su posicion para tratar de tener
      una narracion lo mas logica posible """

    narracion_player:str = ""

    if contador == 0:
        narracion_player = player.nombre +" "+ narraciones[movimiento["Nombre"]] + ""
    elif contador == tamanio_combinacion:
        narracion_player = narraciones[movimiento["Nombre"]] + "."
    else:
        narracion_player = "," + narraciones[movimiento["Nombre"]] 
    
    return narracion_player



def get_secuencia_pelea(player)->dict:

    """funcion que crea una secuencia de la pelea por cada jugador de manera individual 
       identificar los movimientos, golpes y comandos especiales y les da una secuencia ordenada y logica 
       segun los comandos introducidos en el json como resultado obtenemos un diccionario 
       que va de manera ordenada que es lo que el jugador hace en su turno 
       """
    
    movimientos_player = player.movimientos
    golpes_player = player.golpes
    movimientos_especiales = combinaciones.get_combinaciones()
    combinacion_player= movimientos_especiales[str(player)]

   
    lista_de_movimientos= movimientos.lista_movimientos()
    lista_de_golpes = golpes.lista_golpes()
    lista_de_movimientos_mas_golpes = lista_de_movimientos | lista_de_golpes
    lista_de_narraciones = narracion.lista_narracion(str(player))
    
    secuencia_player = []


    for m,g in zip(movimientos_player,golpes_player):
        combinacion = m+g
        narracion_player = ""
        energia_player = 0
        tamanio_combinacion = len(combinacion)
        movimiento_especial = {}
        contador = 0
       
        if combinacion != "":

            for x,y in combinacion_player.items() :
                fin = combinacion.find(x)
                if fin != -1:
                    movimiento_especial = y
                    break

            if fin != -1:
                if fin != 0:
                    for n in range(0,fin):
                        movimiento = lista_de_movimientos_mas_golpes.get(combinacion[n])
                        energia_player += int(movimiento["Energia"])
                        narracion_player += get_narracion(player,lista_de_narraciones,movimiento,contador,tamanio_combinacion)
                        contador+= 1
                   
            else:
                for n in range(0,tamanio_combinacion):
                    movimiento = lista_de_movimientos_mas_golpes.get(combinacion[n])
                    energia_player += int(movimiento["Energia"])
                    narracion_player += get_narracion(player,lista_de_narraciones,movimiento,contador,tamanio_combinacion)
                    contador+= 1
               
            
            if movimiento_especial != {}:
                energia_player += int(movimiento_especial["Energia"])
                narracion_player += get_narracion(player,lista_de_narraciones,movimiento_especial,contador,tamanio_combinacion)
                contador+= 1

        if narracion_player!="":
            secuencia_player.append({"Narracion":narracion_player, "Energia":energia_player })

    return secuencia_player



def simular_combate(p1,p2):

    """Funcion que permite recrear el combate segun los comandos cargados en cada jugador hasta que uno 
       de los dos jugadores llegue sus puntos de vida a cero , de igual form  
       generar la narracion que nos permite dar una idea de lo que esta pasando"""

    secuencia_p1 = get_secuencia_pelea(p1)
    secuencia_p2 = get_secuencia_pelea(p2)
    contador = 0

    while p1.puntos_de_vida >0 and p2.puntos_de_vida >0:

        if contador < len(secuencia_p1): 
            p2.puntos_de_vida -= secuencia_p1[contador]["Energia"]
            print(secuencia_p1[contador]["Narracion"])
        else:
            print(p1.nombre + "no hace nada")

        if p2.puntos_de_vida > 0:

            if contador < len(secuencia_p2):
                p1.puntos_de_vida -= secuencia_p2[contador]["Energia"]
                print(secuencia_p2[contador]["Narracion"])
            else:
                print(p2.nombre + "no hace nada")

            
            if p1.puntos_de_vida <= 0:
                print(p2.nombre + f" gana la pelea y aun le queda {p2.puntos_de_vida} puntos de vida")
                break

        else:
            print(p1.nombre + f" gana la pelea y aun le queda {p1.puntos_de_vida} puntos de vida")
            break

        if contador > len(secuencia_p1) and contador> len(secuencia_p2):
            print("Empate entre "+ p1.nombre +" y "+ p2.nombre)
            break

        contador+= 1
        time.sleep(3)





  


        