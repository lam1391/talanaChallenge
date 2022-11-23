import functools
import operator


class Player():

    def __init__(self,nombre:str,) -> None:
        self.__nombre:str = nombre
        self.__puntos_de_vida = 0
        self.__movimiento:list[str] = []
        self.__golpes:list[str] = []
        self.__numero_movimientos=0
        self.__numero_golpes=0
    

    @property
    def puntos_de_vida(self):
        return self.__puntos_de_vida
    
    @puntos_de_vida.setter
    def puntos_de_vida(self,puntos_de_vida:int):
        self.__puntos_de_vida = puntos_de_vida


    @property
    def movimientos(self):
        return self.__movimiento
    
    @movimientos.setter
    def movimientos(self,movimientos:list[str]):
        if len(movimientos) >0:
            self.__movimiento = movimientos
            self.__numero_movimientos = len(functools.reduce(operator.add,movimientos))
        else:
            raise ValueError("lista de movimientos no puede estar vacia")

    @property
    def golpes(self):
        return self.__golpes
    
    @golpes.setter
    def golpes(self,golpes:list[str]):
        if len(golpes) >0:
            self.__golpes = golpes
            self.__numero_golpes = len(functools.reduce(operator.add,golpes))
        else:
            raise ValueError("lista de golpes no puede estar vacia")

    @property
    def nombre(self):
        return self.__nombre

    @property
    def numero_movimientos(self):
        return self.__numero_movimientos

    @property
    def numero_golpes(self):
        return self.__numero_golpes


    def __str__(self) -> str:
        if  self.__nombre == "Tonyn Stallone":
            return "player1"
        else:
            return "player2"


    

    
    
    

