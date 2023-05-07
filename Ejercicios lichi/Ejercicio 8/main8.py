from conjunto8 import conjunto

if __name__ == '__main__':
    opc = None
    while(opc != '0'):
        opc = input('''--Menu--
        1) Crear conjuntos.
        2) Sumar dos conjuntos.
        3) Restar dos conjuntos.
        4) Comparar conjuntos.
        0) Terminar con el programa.
        ''')
        if opc == '1':
            conjunto1 = conjunto()
            conjunto1.agregarNumero()
            conjunto2 = conjunto()
            conjunto2.agregarNumero()
        elif opc == '2':
            print("la suma de ",conjunto1.getConjunto()," y ",conjunto2.getConjunto(),"es.",conjunto1+conjunto2)
        elif opc == '3':
            print("la resta de ",conjunto1.getConjunto()," y ",conjunto2.getConjunto(),"es",conjunto1-conjunto2)
        elif opc == '4':
            b = (conjunto1 == conjunto2)
            if(b == True):
                print("Los conjuntos son iguales.")
            else:
                print("Los conjuntos no son iguales.")