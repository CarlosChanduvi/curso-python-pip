import matplotlib.pyplot as plt 

# Definir una funcion para generar un grafico
def generate_pie_chart():
    labels=['A','B','C']
    values=[200,34,120]
    # Para generar la grafica:
    #Obtenemos la figura(fig) y las coordenadas(ax)
    fig, ax=plt.subplots()
    ax.pie(values,labels=labels)
    plt.savefig('pie.png')
    plt.close()