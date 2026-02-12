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
    print("Su saldo actual es ${saldo}")


def depositar_dinero(saldo_actual):

    return saldo_actual


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