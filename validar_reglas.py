import functools

import movimientos,golpes
import players



def valida_movimientos_ilegales(movimientos_jugador:list,golpes_jugador:list)->bool:

    """validacion de movimientos ilegales los siguientes movimientos se consideran ilegal :
    1.Los movimientos pueden ser un string de largo máximo 5 (puede ser vacío)
    2.Los golpes pueden ser un solo botón maximo (puede ser vacío) 
    3. movimientos validos =  (W)Arriba, (S)Abajo, (A)Izquierda, (D)Derecha 
    4. golpes validos = (P)Puño, (K)Patada  
    si cualquier comando sale de estos parametros se regresa un TRUE = movimiento ilegal

    """

    movimientos_validos = movimientos.lista_movimientos().keys()
    golpes_validos = golpes.lista_golpes().keys()

    for comando in movimientos_jugador:
        lista_movimientos = []
        lista_movimientos[:0] = comando
        
        if len(comando) > 5:
            return True
        
        for x in lista_movimientos:
            if x not in movimientos_validos:
                return True



    for comando in golpes_jugador:
        lista_golpes = []
        lista_golpes[:0] = comando

        if len(comando) > 1:
            return True

        for x in lista_golpes:
            if x not in golpes_validos:
                return True

    return False

def inicio_pelea(player1:players,player2:players)->str:

    """Funcion que devuelve quien inicia la pelea
    regla: 
    Parte atacando el jugador que envió una combinación menor de botones (movimiento + golpes), 
    en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, 
    si hay empate de nuevo, inicia el player 1 
    """

    total_todos_movimientos_p1 = player1.numero_movimientos + player1.numero_golpes
    total_todos_movimientos_p2 = player2.numero_movimientos + player2.numero_golpes

    if total_todos_movimientos_p1 > total_todos_movimientos_p2:
        return str(player2)
    elif total_todos_movimientos_p2 > total_todos_movimientos_p1:
        return str(player1)
    elif total_todos_movimientos_p1 == total_todos_movimientos_p2:

        if player1.numero_movimientos > player2.numero_movimientos:
            return str(player1)
        elif player2.numero_movimientos > player2.numero_movimientos:
            return str(player2)
        elif player1.numero_movimientos == player2.numero_movimientos:

            if player1.numero_golpes > player2.numero_golpes:
                return str(player2)
            elif player2.numero_golpes > player1.numero_golpes:
                return str(player1)
            elif player2.numero_golpes == player1.numero_golpes:
                return str(player1)






     