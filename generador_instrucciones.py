import distribucion_uniforme as df
import secrets

def instruccion():
    operacion = df.distribucion_uniforme(3)
    
    if operacion == 1:
        return "calc"
    
    elif operacion == 2:
        direccion = bin(df.distribucion_uniforme(8))
        return "read " + str(direccion[2:])
    
    elif operacion == 3:
        direccion = bin(df.distribucion_uniforme(8))
        number = secrets.token_hex(2)
        return "write " + str(direccion[2:]) + ";" + str(number)
