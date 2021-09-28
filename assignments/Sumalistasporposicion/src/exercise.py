def main():
    #escribe tu código abajo de esta línea
    n = int(input('Dame el total de datos de cada lista: '))

    if n > 0:
        lista1 = []
        for i in range(n):
            dato = int(input('>>>'))
            lista1.append(dato)

        lista2 = []
        for i in range(n):
            dato = int(input('>>>'))
            lista2.append(dato) 

        listaresultado = []

        for i in range(n):
            suma = lista1[i]+lista2[i] 
            listaresultado.append(suma) 

        print(listaresultado) 
    else:
        print('Error')

if __name__=='__main__':
    main()
