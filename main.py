import wikipedia

wikipedia.set_lang("es")

vocabulario = [
    'memoria ROM',
  	'Lionel Messi',
    'RAM'  
]

parrafos = 1

tarea = open("tarea.txt", "w+", encoding='utf-8')

print("Buscando ...")

for i in range(len(vocabulario)):
    
    busqueda = wikipedia.search(vocabulario[i])

    if(len(busqueda) > 0):

        #Si encontró algo...
        result = wikipedia.summary(busqueda[0], sentences=parrafos)

        tarea.write(vocabulario[i] + ": " + result + "\n\n")

    else:

        #Si no se encuentra la palabra...
        tarea.write(vocabulario[i] + ": No se ha encontrado ninguna palabra, Posiblemente por mala escritura.\n\n")

else:
    tarea.close()
    print("Bye!")