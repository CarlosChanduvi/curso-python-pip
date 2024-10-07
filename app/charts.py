import matplotlib.pyplot as plt

# Vamos a generar una funcion para generar grafica
# name sera el nombre del archivo del grafico donde se guardara
def generate_bar_chart(name,labels,values):
    fig,ax=plt.subplots()
    ax.bar(labels,values)
    plt.savefig(f'./img/{name}.png')
    plt.close()
    
def generate_pie_chart(labels,values):
    fig,ax=plt.subplots()
    ax.pie(values,labels=labels,autopct='%1.1f%%')
    ax.axis('equal')
    plt.savefig('pie.png')
    plt.close()
    
#Ejecutar el modulo como un script
if __name__=='__main__':
    labels=['a','b','c']
    values=[10,40,800]
    #generate_bar_chart(labels,values)
    generate_pie_chart(labels,values)