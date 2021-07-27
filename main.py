import wikipedia

#Idioma de búsqueda
wikipedia.set_lang("es")

#Aqui pones las palabras de tu tarea
vocabulario = [
    'memoria ROM',
  	'Lionel Messi',
    'RAM'  
]

parrafos = 1

tarea = open("tarea.txt", "w+", encoding='utf-8')

print("Buscando tu fkn Tarea, No molestar...")

for i in range(len(vocabulario)):
    
    busqueda = wikipedia.search(vocabulario[i])

    if(len(busqueda) > 0):

        #Si encontró algo...
        result = wikipedia.summary(busqueda[0], sentences=parrafos)

        tarea.write(vocabulario[i] + ": " + result + "\n\n")

    else:

        #Si no se encuentra la palabra...
        tarea.write(vocabulario[i] + ": No se ha encontrado ninguna palabra, Posiblemente por mala escritura. Me descepcionas bro...\n\n")

else:
    #Cerramos el documento y brr!
    tarea.close()
    print("Tamos Ready Brr!")