import generador_instrucciones as gi
import time
import multiprocessing

class procesador:
    def __init__(self, identificador):
        self.identificador = identificador

    def __str__(self):
        return f"Procesador: {self.identificador}  --  "

def crearProcesador(id):
    proc = procesador(id)
    
    for i in range(3):
       print(str(proc) + gi.instruccion(id))
       time.sleep(2)
       
    

if __name__ == '__main__':
   hilos = []
   for i in range(1,5):
    hilo = multiprocessing.Process(target=crearProcesador, args=(i,))
    hilos.append(hilo)

   for hilo in hilos:
    hilo.start()

   for hilo in hilos:
    hilo.join()
    
    # for i in range(10):
    #    print(gi.instruccion())
    #    time.sleep(1)

