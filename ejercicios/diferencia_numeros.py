def main():
    print("Diferencia (resta) entre dos números")
    numero1 = float(input("Dígame un número: "))
    numero2 = float(input(f"Dígame un número mayor que {numero1}: "))
    if numero2 > numero1:
        print(f"La diferencia entre ellos es {numero2 - numero1}.")
    else:
        print(f'{numero2} es menor que {numero1}, por tanto la direfencia sera negativa')
        print(numero2-numero1)

if __name__ == '__main__':
    main()