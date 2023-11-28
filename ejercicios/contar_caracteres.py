def main():
    print("Contar el número de caracteres en un texto ignorando los espacios")
    texto = input("Ingrese el texto: ")
    caracteres = 0
    for x in texto:
        if x == ' ':
            continue
#continue ingnora la siguiente linea de codigo y continua en este caso el for
        caracteres += 1
    print(f"El número de caracteres es {caracteres}")

if __name__ == '__main__':
    main()