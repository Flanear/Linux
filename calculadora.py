def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Error: división por cero"
    return a / b

def mostrar_menu():
    print("\n--- Calculadora Básica ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "5":
            print("¡Hasta luego!")
            break

        if opcion not in ("1", "2", "3", "4"):
            print("Opción no válida. Intenta de nuevo.")
            continue

        try:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: ingresa números válidos.")
            continue

        if opcion == "1":
            print(f"Resultado: {suma(a, b)}")
        elif opcion == "2":
            print(f"Resultado: {resta(a, b)}")
        elif opcion == "3":
            print(f"Resultado: {multiplicacion(a, b)}")
        elif opcion == "4":
            print(f"Resultado: {division(a, b)}")

if __name__ == "__main__":
    main()
