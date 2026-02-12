
def verificar_pin():

    return True


def consultar_saldo(saldo_actual):

    print(f"Lógica de consulta pendiente...")



def depositar_dinero(saldo_actual):

    print("Realizar Deposito")
    monto = float(input("Cuanto Dinero Quiere Depositar? $"))
    if monto >0:
        nuevo_saldo = saldo + monto
        print("Exito En Transaccion De Monto{monto}")
        return nuevo_saldo
    else: 
        print("error en la transaccion el monto 0.")
        return saldo


def retirar_dinero(saldo_actual):

    return saldo_actual


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