# --- DATOS INICIALES (Para que el programa funcione) ---
saldo = 1000  # Saldo inicial de prueba
pin_correcto = "1234"

# ==========================================
# ESTUDIANTE 1: Autenticación y Seguridad
# ==========================================
def verificar_pin():
    # TODO: Pedir al usuario su PIN y comparar con pin_correcto
    # Debería devolver True si es correcto, False si no.
    print("Lógica de PIN pendiente...")
    return True

# ==========================================
# ESTUDIANTE 2: Consultas y Saldo
# ==========================================
def consultar_saldo(saldo_actual):
    # TODO: Mostrar el saldo actual en pantalla con un mensaje amigable
    print(f"Lógica de consulta pendiente...")

# ==========================================
# ESTUDIANTE 3: Depósitos (Ingreso de dinero)
# ==========================================
def depositar_dinero(saldo_actual):
    # TODO: Pedir monto a ingresar, sumarlo al saldo y devolver el nuevo saldo
    print("Lógica de depósito pendiente...")
    return saldo_actual

# ==========================================
# ESTUDIANTE 4: Retiros (Salida de dinero)
# ==========================================
def retirar_dinero(saldo_actual):
    # TODO: Pedir monto, validar que tenga saldo suficiente y restar
    print("Lógica de retiro pendiente...")
    return saldo_actual

# --- FLUJO PRINCIPAL DEL PROGRAMA ---
def cajero():
    global saldo
    print("¡Bienvenido al Cajero Automático Estudiantil!")
    
    if verificar_pin():
        while True:
            print("\n--- MENÚ DE OPCIONES ---")
            print("1. Consultar Saldo")
            print("2. Depositar Dinero")
            print("3. Retirar Dinero")
            print("4. Salir")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                consultar_saldo(saldo)
            elif opcion == "2":
                saldo = depositar_dinero(saldo)
            elif opcion == "3":
                saldo = retirar_dinero(saldo)
            elif opcion == "4":
                print("Gracias por usar nuestro cajero. ¡Adiós!")
                break
            else:
                print("Opción no válida, intenta de nuevo.")

# Iniciar el programa
cajero()