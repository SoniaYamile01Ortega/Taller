secret_number = 1000
numero = int(input("Ingrese un número:\n"))
while numero != secret_number :
    print("Jajaj atrapado en mi bucle")
    numero = int(input("Ingrese un número:\n"))

    if(numero == secret_number):
        print("Bien hecho, mugle eres libre ahora")
