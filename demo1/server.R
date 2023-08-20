
library(shiny)
library(reticulate)

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
  
  #Evento y evaluación de diferencias finitas
  diferFinitCalculate<-eventReactive(input$diferFinEval, {
    inputEcStr<-input$difFinEcu[1]
    valX<-input$valorX[1]
    h<-input$valorH[1]
    outs<-evaluate_derivate_fx(inputEcStr, valX, h)
    as.character(outs)
  })
  
  
  #REnder metodo de Newton
  output$salidaTabla<-renderTable({
    bisection_method()
  })
  
  #Render Diferncias Finitas
  output$difFinitOut<-renderText({
    diferFinitCalculate()
  })
  
  
})
