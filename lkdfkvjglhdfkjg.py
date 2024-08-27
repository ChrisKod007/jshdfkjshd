meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL" : "una respuesta a una broma"
            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")



if word in meme_dict.keys():
    print(meme_dict[word])
    # ¿Qué debemos hacer si se encuentra la palabra?
else:
    print("Lo lamento, esta palabra no se encuentra en nuestro diccionario")
    # ¿Qué hacer si no se encuentra la palabra?
