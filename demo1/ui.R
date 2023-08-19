library(shiny)
library(shinydashboard)

# Define UI for application that draws a histogram
dashboardPage(
    dashboardHeader(title = "ALG DS"),
    dashboardSidebar(
        sidebarMenu(
            menuItem("Bisección", tabName = "Ceros"),
            menuItem("Newton - Raphson", tabName = "Derivacion")
        )
    ),
    dashboardBody(
        tabItems(
            tabItem("Ceros",
                    h1("Algoritmo - Metodo de la Bisección"),
                    box(textInput("ecuacion", "Ingrese la Ecuación"),
                        textInput("initVal", "Intervalor a,b"),
                        textInput("Error", "Número máximo de Iteraciones"),
                        textInput("epsilon", "Tolerancia")),
                    actionButton("nwtSolver", "Encontrar Solucion Bisección"),
                    tableOutput("salidaTabla")),
            
            tabItem("Derivacion",
                    h1("Algoritmo - Metodo de Newton-Raphson"),
                    box(textInput("difFinEcu", "Ingrese la Ecuación"),
                    textInput("valorX", "Solucion inicial X_0"),
                    textInput("valorH", "Numero Máximo de Iteraciones"),
                    textInput("valorH", "Tolerancia")),
                    actionButton("diferFinEval", "Encontrar solución Newton"),
                    textOutput("difFinitOut"))
        )
    )
)
