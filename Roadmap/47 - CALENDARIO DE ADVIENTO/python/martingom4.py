# EJERCICIO:
# ¡Cada año celebramos el aDEViento! 24 días, 24 regalos para
# developers. Del 1 al 24 de diciembre: https://adviento.dev
#
# Dibuja un calendario por terminal e implementa una
# funcionalidad para seleccionar días y mostrar regalos.
# - El calendario mostrará los días del 1 al 24 repartidos
#   en 6 columnas a modo de cuadrícula.
# - Cada cuadrícula correspondiente a un día tendrá un tamaño
#   de 4x3 caracteres, y sus bordes serán asteríscos.
# - Las cuadrículas dejarán un espacio entre ellas.
# - En el medio de cada cuadrícula aparecerá el día entre el
#   01 y el 24.
#
# Ejemplo de cuadrículas:
# **** **** ****
# *01* *02* *03* ...
# **** **** ****
#
# - El usuario seleccioná qué día quiere descubrir.
# - Si está sin descubrir, se le dirá que ha abierto ese día
#   y se mostrará de nuevo el calendario con esa cuadrícula
#   cubierta de asteríscos (sin mostrar el día).
#
# Ejemplo de selección del día 1
# **** **** ****
# **** *02* *03* ...
# **** **** ****
#
# - Si se selecciona un número ya descubierto, se le notifica
#   al usuario.





def calendar_box(dias,filas,columnas):
    contador = 1
    for i in range(filas):
        print("**** " * columnas)
        for j in range(columnas):
            print(f"*{contador:02}*", end=" ")
            contador += 1 # esto es excatamente lo mismo que decir contador = contador + 1
        print("\n", end="")

    print("**** " * columnas)


calendar_box(24,4,6)

def slect_day():
    
