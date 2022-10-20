#Ejercicio10
print("Digite el numero de un mes")
a=int(input())
if 1<=a<=12:
    if a==1:
        nmes="enero"
    elif a==2:
        nmes="febrero"
    elif a==3:
        nmes="marzo"
    elif a==4:
        nmes="abril"
    elif a==5:
        nmes="mayo"
    elif a==6:
        nmes="junio"
    elif a==7:
        nmes="julio"
    elif a==8:
        nmes="agosto"
    elif a==9:
        nmes="septiembre"
    elif a==10:
        nmes="octubre"
    elif a==11:
        nmes="noviembre"
    else:
        nmes="diciembre"
    print(f"el mes que selecciono es: {nmes}")
else:
    print("Revise su entrada")