from math import sqrt
 
def area_triangulo(a, b, c):
    s = (a + b + c) / 2.0
    return sqrt(s * (s-a) * (s-b) * (s-c))
  
lado1 = float(input('Ingresa lado a: '))
lado2 = float(input('Ingresa lado b: '))
lado3 = float(input('Ingresa lado c: '))
 
area = area_triangulo(lado1, lado2, lado3)
 
print ('')
print ('El área del triángulo es:', area)
