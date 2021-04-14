import random

#Devuelve palabra random de un txt

def getNewWord()-> str:
    word: str = ""
    wrapper = open("texto.txt","r")
    texto = wrapper.read()
    texto = str.split(texto)
    word = random.choice(texto)
    return word


#Transforma palabra en diccionario por letra del tipo [letra]=bool con primera letra en true


def transfEnDic(word:str):
    letrasEstados = {}
    count = 0
    for l in word:
        if count == 0:
            letrasEstados[count]= [l,True]
        else:
            letrasEstados[count]= [l,False]
        count+=1
    return letrasEstados

#Muestra la palabra solo las letras visibles y las que no, muestra un guion bajo

def mostrarLetras(letras:dict)->str:
    outPut:str = ""
    for letra in letras.values():
        if letra[1]:
            outPut += " "+str.upper(letra[0])
        else:
            outPut += " _"
    return outPut

def contieneLetra(letras:dict, l:str):
    posiciones: list = []
    for key in letras.keys():
        if(letras[key][0]==l):
            posiciones.append(key)
    return posiciones


def juego():
    
    #Intentos Fallidos Permitidos

    vidas: int = 8

    #Inicializa 

    palabra: str = getNewWord()

    letras: dict = transfEnDic(palabra)

    print("INICIO DEL AHORCADO")

    winFlag = False
    
    while(vidas > 0 and winFlag == False):
        print("-------------------")
        print("Tienes "+str(vidas)+" errores permitidos")
        print(mostrarLetras(letras))

        nuevaLetra: str = input("Adivino letra: ")
        
        if(len(nuevaLetra)!= 1):
            print("Debe ingresar solo una letra.")
            continue
        elif(len(nuevaLetra) == 1):
            posiciones = contieneLetra(letras,nuevaLetra)
            if(len(posiciones)>=1):
                for i in posiciones:
                    letras[i][1]=True
                print("ACERTASTE!!")
            elif(len(posiciones) == 0):
                vidas -= 1
                print("ERRASTE!!, Pierdes 1 vida")
        var = True
        for v in letras.values():
            if v[1] == False:
                var = False
        winFlag = var
    if(vidas>0 and winFlag):
        print("¡GANASTE!, La palabra es "+palabra)
    if(vidas == 0):
        print("Perdiste, La palabra es "+palabra)