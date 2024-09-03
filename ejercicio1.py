#Imagina que eres un profesor y quieres calcular la media de las calificaciones de tus
#  estudiantes para una asignatura en particular. Debes pedir al usuario que ingrese las 
# calificaciones de cada estudiante y luego calcular la media. Además, mostrarás un mensaje
#  que indicará si la media es aprobatoria o no, considerando que una calificación 
# aprobatoria es 6 o superior.
'''
notas=[]
for i in range (0,6,2):
    nota=int(input("Ingrese la nota: "))
    notas.append(nota)
print(notas)
for n in notas:
    suma=0
    suma=n+suma
promedio=suma/6
print(promedio)

if (promedio>=6):
    print("Aprobado")
else:
    print("Desaprobado")
'''

def notas(*args):
    print
    suma=0
    for n in args:
        suma=suma+n




