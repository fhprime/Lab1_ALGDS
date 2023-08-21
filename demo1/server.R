
library(shiny)
library(reticulate)
library(ggplot2)


source_python("algoritmos.py")

#tableOut, soluc = newtonSolverX(-5, "2x^5 - 3", 0.0001)

shinyServer(function(input, output) {
  
  #Evento y evaluación de metodo de newton para ceros
  bisection_method<-eventReactive(input$bisection_solver, {
    inputEcStr<-input$ecuacion_bisection[1]
    print(inputEcStr)
    interval_bs<-input$intervalo[1]
    iter_bs_max<-input$iter_max[1]
    epsilon<-input$epsilon[1]
    #outs<-add(initVal, error)
    outs<-BisectionSolverX(inputEcStr, interval_bs,iter_bs_max,epsilon)
    outs
  })
  
  #Evento y evaluación de newton
  newton_calculate<-eventReactive(input$newton_solver, {
    ecuacion_newton_var<-input$ecuacion_newton[1]
    valor_init_var<-input$val_init_newton[1]
    valor_itera_newton_var<-input$val_intera_newton[1]
    epsilon_newton_var<-input$epsilon_newton[1]
    outs<-fun_newton_rap(ecuacion_newton_var, valor_init_var, valor_itera_newton_var, epsilon_newton_var)
    outs<-as.data.frame(outs)
    outs
  })
  
  
  #REnder metodo de Newton
  output$salidaTabla<-renderTable({
    bisection_method()
  })
  
  #Render newton
  output$newton_salida_tabla<-renderTable({
    newton_calculate()
  })
  
  
})
