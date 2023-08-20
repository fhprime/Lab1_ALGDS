import pandas as pd
import re

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
