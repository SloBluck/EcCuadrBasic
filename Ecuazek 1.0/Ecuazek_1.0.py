#-*- coding: utf-8 -*-
saludo=str("ECUAZEK")
print(saludo.center(50," "))
opcion = 1
while opcion!=2:
    print("Mediante este programa insertarás funciones de la forma 'Ax^2 + Bx + C'")
    opcion = int(input("""Seleccione:
1) Usar el programa
2) Salir\n"""))
    if opcion == 1:
        a=int(input("Ingresar valor de A: "))
        b=int(input("Ingresar valor de B: "))
        c=int(input("Ingresar valor de C: "))
        cadena=str(a)+"x^2 + "+str(b)+"x + "+str(c)+" = 0"
        disc=b**2-4*a*c
        print("Usted ha insertado una ecuación de la forma:\n",cadena)
        if a!=0:
            cadsa_1="x = ["+str(-b)+" ± √("+str(disc)+")] / 2("+str(a)+")"
            print(cadsa_1)
            print("")
            print("Discriminante:",disc)
            operacion_1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
            operacion_2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
            print("")
            print("Resultado:")
            if disc > 0:
                print("Raices=",operacion_1,"y",operacion_2)
            elif disc == 0:
                print("Raíz=",operacion_1)
            else:
                print("Raíces complejas e imaginarias")
            print("")
        elif a==0:
            cadsa_1=str(b)+"x = "+str(-c)
            cadsa_2= "x = "+str(-c)+"/"+str(b)
            print(cadsa_1)
            print(cadsa_2)
            if b!=0:
                operacion_3=-c/b
                print("El resultado es:",operacion_3)
            else:
                print("Indefinido")
            print("")
    elif opcion ==2:
        print("Gracias por usar el programa...")
    else:
        print("Opción incorrecta")
input()


    