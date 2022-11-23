
from cargar_pelea import get_pelea
from players import Player

import validar_reglas
import simulador
import banner


player1:Player = None
player2:Player = None

def inicializar()->True:

    """Funcion de inicializacion del proceso el cual se encarga de traer la informacion de la pelea de un archivo json,
    inicializa a los jugagores y carga la informacion de los json a los jugagores si la carga inicial es correcta se puede
    continuar con el juego """

    partida = get_pelea()
    
    global player1
    global player2

    if partida != None:

        player1 = Player("Tonyn Stallone")
        player1.puntos_de_vida = 6
        player2 = Player("Arnaldor Shuatseneguer")
        player2.puntos_de_vida = 6

        for player,movimientos in partida.items():
            if player == "player1":
                if validar_reglas.valida_movimientos_ilegales(movimientos["movimientos"],movimientos["golpes"]) == False:
                    player1.movimientos = movimientos["movimientos"]
                    player1.golpes = movimientos["golpes"]
                else:
                    raise ValueError(f"se detecto movimientos o golpes ilegales para {player}")
            elif player == "player2":
                if validar_reglas.valida_movimientos_ilegales(movimientos["movimientos"],movimientos["golpes"]) == False:
                    player2.movimientos = movimientos["movimientos"]
                    player2.golpes = movimientos["golpes"]
                else:
                     raise ValueError(f"se detecto movimientos o golpes ilegales para {player}")

                
        return True
    else:
        return False


def run():
    try:
        carga_inicial = inicializar()
    except ValueError as error:
        print(error)
    else:
        
        if carga_inicial == True:
            banner.print_banner()
            player_inicial = validar_reglas.inicio_pelea(player1,player2)
           
            if player_inicial == "player1":
                simulador.simular_combate(player1,player2)
            else:
                simulador.simular_combate(player2,player1)
  
        else:
            print("la carga inicial de parametros de juego no pudo realizarse de forma correcta favor volver a intentar")

if __name__ == "__main__":
    run()