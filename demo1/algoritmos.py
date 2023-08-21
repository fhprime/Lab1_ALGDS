import pandas as pd
import re
from sympy import *




#Evaluación REGREX
def evaluate_Fx(str_equ, valX):
  x = valX
  #strOut = str_equ
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  out = eval(strOut)
  print(strOut)
  return out

#Deferencias finitas para derivadas
def evaluate_derivate_fx(str_equ, x, h):
  strOut = str_equ.replace("x", '*(x + h)')
  strOut = strOut.replace("^", "**")
  strOut = "-4*(" + strOut + ")"
  out = eval(strOut)
  
  strOut = str_equ.replace("x", '*(x + 2*h)')
  strOut = strOut.replace("^", "**")
  out = out + eval(strOut)
  
  strOut = str_equ.replace("x", '*(x)')
  strOut = strOut.replace("^", "**")
  strOut = "3*(" + strOut + ")"
  out = out + eval(strOut)
  
  out = -out/(2*h)
  print(out)
  return out

#Resolverdor de Newton
def BisectionSolverX(funcion,intervalo,max_iteraciones,tolerancia):
  function_changed = funcion.replace('^','**')
  interval_separated = intervalo.split(',')
  interval_separated = [float(element) for element in interval_separated]
  max_iteraciones = float(max_iteraciones)
  tolerancia = float(tolerancia)
  e = 2.71828
  k = 0
  a = interval_separated[0]
  b = interval_separated[1]
  x_k = (a + b)/2
  x = x_k
  list_data = []
  n_iter = 0
  while (k<max_iteraciones) and abs(eval(function_changed)):
      x = a
      F_a = eval(function_changed)
      x = x_k
      F_xk = eval(function_changed)
      if F_a*F_xk < 0 :
          b = x_k
      else:
          a = x_k
      k = k + 1
      x_k = (a + b)/2
      n_iter = n_iter + 1
      iter_values = list_data.append([n_iter,round(x_k,4),round(abs(F_xk),4)])
  df = pd.DataFrame(list_data, columns=['Iter','x_k','|F(x_k)|'])
  return df

def add(a, b):
  a = int(a)
  b = int(b)
  resultado = a + b
  return "El resultado es: " + str(resultado)




def fun_newton_rap(funcion_string,x_init,iteraciones,dif_delta_init):


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

        list_x.append(float(round(x_init_1,5)))
        list_y.append(float(abs(round(eval_xp,5))))
        list_itera.append(float(round(cont,5)))

        print("todo bien 3")


        if abs(error_1)<dif_delta_init:
          
          lista = [[list_itera[i], list_x[i], list_y[i]] for i in range(len(list_itera))]
      
          df = pd.DataFrame(lista, columns=['Iter','x_k','|F(x_k)|'])
      
          #print(df)
      
          return df


        cont+=1


    # Crear un diccionario a partir de las listas
    #datos = {
    #    'itera': list_itera,
    #    'X': list_x,
    #    'error': list_y
    #           
    #}

    # Crear un DataFrame a partir del diccionario
    #df = pd.DataFrame(datos)


# funcion_string='2x-e^(-x)' # funcion inicial --- 10x^2+3e^(-5x) ----

# """x^3-2x+1"""

# x_init=-1 # valor inicial de x

# dif_delta_init=0.00000000001  # para finalizar el ciclo la diferencia entre el resultado anterior y el actual debe ser igual a dif_delta_init

# itera=1000

# ##--------- fin ----- ingreso de variables ----------------

# print(fun_newton_rap(funcion_string,x_init,itera,dif_delta_init))


# funcion = '2*x-e^(-x)' # Derivada de la funcion del laboratorio 
# intervalo = '0,1'
# max_iteraciones = '20'
# tolerancia = '0.000000000001'


# datos = BisectionSolverX(funcion,intervalo,max_iteraciones,tolerancia)
# print(datos)
    
