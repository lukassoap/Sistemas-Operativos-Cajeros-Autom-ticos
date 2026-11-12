import threading
import time

class CuentaCompleja:
    def __init__(self, id_cuenta, saldo_inicial):
        # Representación del recurso un poco más realista con un diccionario
        self.datos = {
            "id": id_cuenta,
            "saldo": int(saldo_inicial),
            "estado": "activa",
            "historial": []
        }
        self.lock = threading.Lock()

    def retirar_normal(self, cajero, monto):
        # --- Sección crítica expuesta ---
        # Consultamos múltiples cosas: estado y saldo
        if self.datos["estado"] == "activa" and self.datos["saldo"] >= monto:
            time.sleep(0.1)
            
            # Modificamos saldo e historial
            self.datos["saldo"] -= monto
            self.datos["historial"].append(f"{cajero} sacó ${monto}")
            print(f"[Error] {cajero} procesado. Saldo actual: ${self.datos['saldo']}")
        else:
            print(f"[Error] {cajero} rechazado.")
        # --------------------------------

    def retirar_seguro(self, cajero, monto):
        # Al usar 'with' nos ahorramos poner acquire() y release() a mano
        with self.lock:
            # --- Sección crítica segura ---
            if self.datos["estado"] == "activa" and self.datos["saldo"] >= monto:
                time.sleep(0.1)
                
                self.datos["saldo"] -= monto
                self.datos["historial"].append(f"{cajero} sacó ${monto}")
                print(f"[Ok] {cajero} procesado. Saldo actual: ${self.datos['saldo']}")
            else:
                print(f"[Ok] {cajero} rechazado.")
            # ------------------------------

if __name__ == "__main__":
    print("--- PRUEBA COMPLEJA 1: SIN SINCRONIZAR ---")
    cuenta = CuentaCompleja("CTA-123", 100)
    
    hilos = [threading.Thread(target=cuenta.retirar_normal, args=(f"Cajero {i+1}", 100)) for i in range(2)]
    for h in hilos: h.start()
    for h in hilos: h.join()
    
    print(f"Saldo final: ${cuenta.datos['saldo']} | Historial: {cuenta.datos['historial']}\n")

    print("--- PRUEBA COMPLEJA 2: CON MUTEX ---")
    cuenta2 = CuentaCompleja("CTA-999", 100)
    
    hilos2 = [threading.Thread(target=cuenta2.retirar_seguro, args=(f"Cajero {i+1}", 100)) for i in range(2)]
    for h in hilos2: h.start()
    for h in hilos2: h.join()
    
    print(f"Saldo final: ${cuenta2.datos['saldo']} | Historial: {cuenta2.datos['historial']}")