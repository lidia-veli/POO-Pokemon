lista_1 = [1,2,3]
lista_2 = ['a', 'b', 'c']
i=1
while True:
    entrada1 = int(input('Elige un numero: '))
    
    if entrada1 %2 == 0:
        print('Has quitado el numero', lista_1[-1])
        lista_1.remove(lista_1[-1])
        print('La lista_1 tiene', len(lista_1), 'elementos')
    else:
        print('Has quitado la letra', lista_2[-1])
        lista_2.remove(lista_2[-1])
        print('La lista_2 tiene', len(lista_2), 'elementos')

    if len(lista_1)==0 or len(lista_2)== 0:
            break
    else:
         continue
