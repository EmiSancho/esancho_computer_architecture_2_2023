import time

# Toma el tiempo actual como semilla y lo mutiplica
# lo multiplica por la formula de la disctribucion uniforme 1/b-a
# y recorta el resultado para que este dentro del rango 1 < x < max
# max = el valor mas alto posible.
def distribucion_uniforme(max, id):
    seed = int(time.time())
    formula = seed * (1/max-1)
    resultado = formula * id
    return int(resultado % (max) + 1)
    

    