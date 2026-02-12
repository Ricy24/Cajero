Pin = "1234"
saldo = 1200

def verificar_pin():
    print ("Verificacion")
    intento = input("ingrese su pin ")
    if intento == Pin:
        print("su pin es verdadero, bienvenido")
        return True
    else:
        print("su pin es incorrecto")
        return False

def consultar_saldo(saldo_actual):
    print("Consultar saldo")
    print(f"Su saldo actual es: ${saldo_actual}" )


def depositar_dinero(saldo_actual):

    print("Realizar Deposito")
    monto = float(input("Cuanto Dinero Quiere Depositar? $"))
    if monto > 0:
        nuevo_saldo = saldo_actual + monto
        print(f"Exito En Transaccion De Monto {monto}")
        return nuevo_saldo
    else:
        print("Error en la transaccion, el monto debe ser mayor a 0.")
        return saldo_actual



def retirar_dinero(saldo_actual):
    print("Realizar el retiro")
    monto_Retirar= float (input("¿cuanto dinero desea retirar?"))
    if monto_Retirar>saldo:
        print("error: saldo insuficiente.")
        return saldo
    elif monto_Retirar <=0:
        print("error: Ingrese un monto valido.")
        return saldo
    else:
        nuevo_saldo = saldo - monto_Retirar
        print(f"se ha realizado correctamente el $ {monto_Retirar}.")
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