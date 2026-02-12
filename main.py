
def verificar_pin():

    return True


def consultar_saldo(saldo_actual):

    print(f"Lógica de consulta pendiente...")



def depositar_dinero(saldo_actual):

    return saldo_actual


def retirar_dinero(saldo_actual):
    print("Realizar el retiro")
    monto= float (input("¿cuanto dinero desea retirar?"))
    if monto>saldo:
        print("error: saldo insuficiente.")
        return saldo
    elif monto <=0:
        print("error: Ingrese un monto valido.")
        return saldo
    else:
        nuevo_saldo = saldo - monto
        print("se ha realizado correctamente el $ {monto}.")
        return nuevo_saldo


   


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