import utils
import read_csv
import charts

def run():
    
    data=read_csv.read_csv('data.csv')# Lee la data convertida en diccionario por el metodo 
    data=list(filter(lambda item:item['Continent']=='South America',data))#Filtra por el continente de Sudamerica
    
    countries=list(map(lambda x: x['Country/Territory'],data)) # Se crea una lista de paises
    percentages=list(map(lambda x: x['World Population Percentage'],data))    # Se crea una lista de porcentajes
    charts.generate_pie_chart(countries,percentages)  # Se crea un grafico pastel con las listas anteriores
    
    country=input('Type country => ')
    print(country)
    result=utils.population_by_country(data,country)
    
    if len(result)>0:
        country=result[0]
        labels,values=utils.get_population(country)
        #Aca le damos como primer parametro el nombre del archivo, que en este caso q sea la variable country
        charts.generate_bar_chart(country['Country/Territory'],labels,values)
        
if __name__=='__main__':
    run()