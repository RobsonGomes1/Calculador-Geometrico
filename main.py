import util.area as ar

print('*'*10, 'Calculador para Áreas Geométricas' ,'*'*10 )

op = int(input('\n1-Quadrado\t2-Triângulo\n3-Retângulo\t4-Círculo\n5-Trapézio\n\nDigite -> '))

if op == 1:
    n = float(input('\nValor Lado(L): ').replace(',','.'))
    v = ar.quadrado(n)

if op == 2:  
    n1 = float(input('\nValor Base: ').replace(',', '.')) 
    n2 = float(input('Valor Altura: ').replace(',', '.'))
    v = ar.triangulo(n1,n2)

if op == 3:
    n1 = float(input('\nValor Base: ').replace(',', '.'))
    n2 = float(input('Valor Altura: ').replace(',', '.'))
    v = ar.retangulo(n1,n2)
if op == 4:
    n2 = float(input('\nRaio: ').replace(',', '.'))
    v = ar.circulo(n2)
if op == 5:
    bma = float(input('\nValor Base Maior: ').replace(',', '.'))
    bm = float(input('\nValor Base Menor: ').replace(',', '.'))
    h = float(input('Altura: ').replace(',', '.'))
    v = ar.trapezio(bma, bm, h)

