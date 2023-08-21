library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
  dashboardHeader(title = "ALG DS"),
  dashboardSidebar(
    sidebarMenu(
      menuItem("Bisección", tabName = "Bisection"),
      menuItem("Newton - Raphson", tabName = "NewtonRaphson")
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
      
      tabItem("NewtonRaphson",
              h1("Newton Raphson"),
              box(textInput("ecuacion_newton", "Ingrese la Ecuación"),
                  textInput("val_init_newton", "Ingrese el valor inicial de X"),
                  textInput("val_intera_newton", "Ingrese la cantidad de iteraciones"),
                  textInput("epsilon_newton", "Ingrese el error minimo")),
              actionButton("newton_solver", "Newton Raphson evaluar"),
              tableOutput("newton_salida_tabla"))
    )
  )
)
