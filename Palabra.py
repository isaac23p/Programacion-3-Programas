palabra_secreta = "carro"
intento = 1

print("Trata de adivinar la Palabra Secreta")
print("Tienes 3 oportunidades")

while intento < 4:
    print("\nTURNO: " + str(intento) + " DE 3")
    palabra = input("Palabra: ")
    if palabra.lower() == "carro":
        print("\n\nHAS GANADO!")
        break
    else:
        print("\nADIVINA DEVUELTA!")
        intento += 1

if intento == 4:
    print("PERDISTE!")