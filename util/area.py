import math

def quadrado(x1):
    print(f'Valor área do Quadrado: {x1} = {x1**2} ')

def triangulo(x1,x2):
    print(f'Valor área Triângular: {x1} e {x2} = {((x1*x2)/2)} ')    

def retangulo(x1,x2):
    print(f'Valor área Retangular: {x1} e {x2} = {x1*x2} ') 

def circulo(raio):
    print(f'Valor área Circular: Pi(π) = {round(math.pi,2)} || Raio = {round(raio,2)}\nSerá = {round(math.pi*raio**2,2)}')

def trapezio(basemaior,basemenor,altura):
    print(f'Valor área Trapézio: Base Maior = {basemaior}\tBase Menor = {basemenor}\tAltura = {altura}\nResultado = {(((basemaior+basemenor)*altura)/2)}')