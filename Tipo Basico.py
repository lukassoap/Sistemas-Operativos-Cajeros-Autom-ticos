import threading
import time

class CuentaBasica:
    def __init__(self, saldo_inicial):
        # El recurso compartido en su versión más simple (un entero)
        self.saldo = int(saldo_inicial)
        # Candado para cuando queramos sincronizar
        self.lock = threading.Lock() 

    def retirar_normal(self, cajero, monto):
        # Escenario sin sincronizar para comprobar que falla
        
        # --- Inicio de la sección crítica ---
        # Consultamos y validamos el saldo
        if self.saldo >= monto:
            time.sleep(0.1)  # Simulamos el tiempo que tarda la red
            
            # Actualizamos el recurso
            self.saldo -= monto
            print(f"[Falla] {cajero} sacó ${monto}. Quedan: ${self.saldo}")
        else:
            print(f"[Falla] {cajero} rebotado por fondos.")
        # --- Fin de la sección crítica ---

    def retirar_seguro(self, cajero, monto):
        # Bloqueamos el acceso para los demás hilos
        self.lock.acquire()
        try:
            # --- Inicio de la sección crítica protegida ---
            if self.saldo >= monto:
                time.sleep(0.1) 
                self.saldo -= monto
                print(f"[Seguro] {cajero} sacó ${monto}. Quedan: ${self.saldo}")
            else:
                print(f"[Seguro] {cajero} rebotado por fondos.")
            # --- Fin de la sección crítica protegida ---
        finally:
            # Soltamos el candado al terminar, incluso si hay algún error
            self.lock.release()

if __name__ == "__main__":
    print("--- PRUEBA 1: SIN SINCRONIZAR ---")
    cuenta = CuentaBasica(100)
    
    # Creamos dos hilos que intentan sacar 100 al mismo tiempo de la misma cuenta
    hilos = [threading.Thread(target=cuenta.retirar_normal, args=(f"Cajero {i+1}", 100)) for i in range(2)]
    for h in hilos: h.start()
    for h in hilos: h.join()
    
    print(f"Saldo arruinado: ${cuenta.saldo}\n")

    print("--- PRUEBA 2: CON MUTEX ---")
    cuenta2 = CuentaBasica(100)
    
    hilos2 = [threading.Thread(target=cuenta2.retirar_seguro, args=(f"Cajero {i+1}", 100)) for i in range(2)]
    for h in hilos2: h.start()
    for h in hilos2: h.join()
    
    print(f"Saldo correcto: ${cuenta2.saldo}")