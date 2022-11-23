import json
import validar_reglas

def get_pelea()->dict :

    try:
        data_json= {}
    
        with open("./Files/pelea.json") as file:
            data_json = json.load(file)
    
        return data_json


    except:
        print("Error al abrir el archivo de comandos")
