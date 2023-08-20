library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
  dashboardHeader(title = "ALG DS"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Bisección", tabName = "Bisection"),
      menuItem("Newton - Raphson", tabName = "Derivacion")
    )
  ),
  dashboardBody(
    tabItems(
      tabItem("Bisection",
              h1("Algoritmo - Metodo de la Bisección"),
              box(textInput("ecuacion_bisection", "Ingrese la Ecuación"),
                  textInput("intervalo", "Intervalo a,b"),
                  textInput("iter_max", "No. de Iteraciones maximas"),
                  textInput("epsilon", "Tolerancia")),
              actionButton("bisection_solver", "Bisection Solver"),
              tableOutput("salidaTabla")),
      
      tabItem("Derivacion",
              h1("Diferencias Finitas"),
              box(textInput("difFinEcu", "Ingrese la Ecuación"),
                  textInput("valorX", "x"),
                  textInput("valorH", "h")),
              actionButton("diferFinEval", "Evaluar Derivada"),
              textOutput("difFinitOut"))
    )
  )
)
