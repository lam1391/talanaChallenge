def lista_narracion(character)->dict:
    character_narracion:dict =  {}
    lista_narracion = {"player1":{"Arriba":"salta",
                      "Abajo":"se agacha ",
                      "Izquierda":"retrocede para evitar a Arnaldor",
                      "Derecha":"avanza hacia Arnaldor",
                      "Puño":"le da un puñetazo al pobre Arnaldor",
                      "Patada":"le da una patada al pobre Arnaldor",
                      "Taladoken": "conecta un Taladoken",
                      "Remuyuken":"conecta un Remuyuken"},
                      
                      "player2":{"Arriba":" salta",
                      "Abajo":"se agacha",
                      "Izquierda":"avanza hacia Tonyn",
                      "Derecha":"retrocede para evitar a Tonyn",
                      "Puño":"le da un puñetazo al pobre Tonyn",
                      "Patada":"le da una patada al pobre Tonyn",
                      "Remuyuken":"conecta un Remuyuken",
                      "Taladoken": "conecta un Taladoken "}}
    character_narracion = lista_narracion[character]
    return character_narracion