def main():
    #escribe tu código abajo de esta línea
    n = -1

    while n <= 0:
        n=int(input('Número de valores a ingresar: '))

    l = []

    for i in range(n):
        dato = int(input(f'Dame el dato {i}: '))
        l.append(dato)

    for i in range(n):
        print(f'lista[{i}]={l[i]}')

if __name__=='__main__':
    main()
