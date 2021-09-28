def main():
    #escribe tu código abajo de esta línea
    n = int(input('total de datos a capturar: '))

    lista =[]

    for i in range(n):
        dato=int(input('>>>'))

        lista.append(dato)

    print(lista) 

    listaCuadrados = [] 

    for i in range(n):
        listaCuadrados.append(lista[i] ** 2)

    print(listaCuadrados) 

if __name__=='__main__':
    main()
