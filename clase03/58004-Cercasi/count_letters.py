def count_letters (palabra):

 diccionario={}

 for letra in palabra:
    
    if letra in diccionario:
        diccionario[letra]=+1
    else:
        diccionario[letra]=1