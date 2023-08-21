# metodo de NEWTON-RAPHSON
# definir las variables como strings 

from sympy import *

import pandas as pd





def fun_newton_rap(funcion_string,x_init,dif_delta_init,iteraciones):


    try:

        x_init=float(x_init)

        print(x_init)

    except ValueError:

        print("Invalid input values provided.")

    try:

        dif_delta_init=float(dif_delta_init)

        print(dif_delta_init)

    except ValueError:

        print("Invalid input values provided.")


    try:

        iteraciones=float(iteraciones)

        print(iteraciones)

    except ValueError:

        print("Invalid input values provided.")

    print("todo bien 0")

    ##--------- inicio ----- convertir funcion en expresion para sympy ----------------

    funcion_string = funcion_string.lower()

    funcion_string_trans=""

    for cont, i in enumerate(funcion_string):

        if cont==0:

            funcion_string_trans+=i

        else:

            try:

                ant_1=funcion_string[cont-1]

                ant_1=int(ant_1)

            except:

                pass

            if type(ant_1)==int and i.isalpha():
            
                funcion_string_trans+="*"
                funcion_string_trans+=i

            else:

                try:

                    i=str(i)

                except:

                    pass      

                funcion_string_trans+=i

    print("todo bien 00")

    #funcion_string = funcion_string.replace("x", '*(x)')
    funcion_string = funcion_string_trans.replace("^", "**")
    funcion_string = funcion_string_trans.replace("e", "E")

    funcion_cadena_expr=sympify(funcion_string)

    funcion_cadena_expr=funcion_cadena_expr.subs(E, E.evalf())

    #print(f"f(x)={funcion_cadena_expr}")

    X = Symbol('x')

    ##--------- fin ----- convertir funcion en expresion para sympy ----------------

    print("todo bien 1")

    ##--------- inicio ----- derivar la funcion  ----------------

    dif_1=(funcion_cadena_expr.diff(X))

    #print(f"f'(x)={dif_1}")

    ##--------- fin ----- derivar la funcion  ----------------

    print("todo bien 2")

    ##--------- inicio ----- ciclo para evaluar la funcion  ----------------

    list_x=[]

    list_y=[]

    list_itera=[]

    df=pd.DataFrame()

    cont=1

    while True:

        x_init_1=x_init

        if cont>iteraciones:

            #print(f"Despues de {iteraciones} iteraciones no se logre alcanzar el objetivo")

            return df

        eval_xp=funcion_cadena_expr.subs(X, x_init_1)
        #print(eval_xp)
        eval_diff=dif_1.subs(X, x_init_1)
        #print(eval_diff)

        x_init=x_init_1-(eval_xp/eval_diff)
        #print(x_init)


        error_1=funcion_cadena_expr.subs(X, x_init)

        list_x.append(x_init_1)
        list_y.append(eval_xp)
        list_itera.append(cont)

        print("todo bien 3")

        if abs(error_1)<dif_delta_init:

            # Crear un diccionario a partir de las listas
            datos = {
                'itera': list_itera,
                'X': list_x,
                'error': list_y
                       
            }

            # Crear un DataFrame a partir del diccionario
            df = pd.DataFrame(datos)

            print(df)

            return df
            
        cont+=1
    

##--------- inicio ----- ingreso de variables ----------------

# funcion_string='2x-e^(-x)' # funcion inicial --- 10x^2+3e^(-5x) ----

# """x^3-2x+1"""

# x_init=-1 # valor inicial de x

# dif_delta_init=0.00000000001  # para finalizar el ciclo la diferencia entre el resultado anterior y el actual debe ser igual a dif_delta_init

# itera=1000

# ##--------- fin ----- ingreso de variables ----------------

# fun_newton_rap(funcion_string,x_init,dif_delta_init,itera)
