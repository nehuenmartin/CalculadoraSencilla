# Define las funciones de las operaciones
def suma(x, y):
    return x + y
def resta(x, y):
    return x - y
def multiplicacion(x, y):
    return x * y
def divicion(x, y):
    return x / y

while True:
    try:

        # Pregunta la operación a realizar
        operacion = input(f'selecciona la operación: \n a. Suma \n b. Resta \n c. Multiplicación \n d. División')

        # Pregunta los números a operar
        num_1 = int(input("Cual es el primer número: "))
        num_2 = int(input("Cual es el segundo número: "))

        # Realiza la operación
        if operacion == 'a':
            print(num_1,"+",num_2,"=", suma(num_1,num_2))
        elif operacion == 'b':
            print(num_1,"-",num_2,"=", resta(num_1,num_2))
        elif operacion == 'c':
            print(num_1,"*",num_2,"=", multiplicacion(num_1,num_2))
        elif operacion == 'd':
            print(num_1,"/",num_2,"=", divicion(num_1,num_2))
        repetir = input("¿Desea realizar otra operación? (s/n): ")
        if repetir == 's':
            continue
        else:
            break
    except ValueError:
        print("No se puede realizar la operación con letras")
        continue

