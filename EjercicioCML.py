# -*- coding: utf-8 -*-
"""
Created on Sat Jun  4 15:32:34 2022

@author: Adriana Suarez
"""

"""
email: adriana.suarezb@upb.edu.co
ID: 502197


"""

import pandas
from sklearn import linear_model



carsdf = pandas.read_excel(r'C:\Users\Adriana Suarez\my_python\Spyder\cars.xlsx', sheet_name='car')

#  HW - 
 
# A partir de los valores independientes (volumen, peso y producción de CO2)
# predecir el comportamiento de la variable dependiente (marca del carro.)


# Hacer una lista de las variables independientes
x = carsdf[['Weight', 'Volume', 'CO2']]


# Valores de la variable dependiente
# Se hizo un condicional para asignar un número a cada marca del carro

def funcion_car(marca):
    
    if marca == "Toyota":
        return 1
    
    elif marca == "Mitsubishi":
        return 2
        
    elif marca == "Skoda":
        return 3
        
    elif marca == "Fiat":
        return 4    
        
    elif marca == "Mini":
        return 5    
        
    elif marca == "VW":
        return 6

    elif marca == "Mercedes":
        return 7    
        
    elif marca == "Ford":
        return 8     

    elif marca == "Audi":
        return 9         
        
    elif marca == "Hyundai":
        return 10          

    elif marca == "Suzuki":
        return 11      

    elif marca == "Honda":
        return 12    
        
    elif marca == "Hundai":
        return 13       

    elif marca == "Opel":
        return 14      

    elif marca == "BMW":
        return 15   

    elif marca == "Mazda":
        return 16

    elif marca == "Volvo":
        return 17
    
y = carsdf['Car'].apply(funcion_car)   



# Regresion
reg_mod = linear_model.LinearRegression()
reg_mod.fit(x, y)


#Prediccion
predic_co = reg_mod.predict([[865, 900, 90]])
print(predic_co)


# Determine el valor de r de relación para evidenciar el funcionamiento optimo o no del modelo.

# >> Los tres valores separados de x, son para ver la relación de cada uno con 
# la variable dependiente y << Para esto se debe comentar la linea de código que
# guarda el valor de x,que esta más arriba e ir descomentando las siguientes, 
# una por una

# x = carsdf['Weight']
# x = carsdf['Volume']
# x = carsdf['CO2']


# slope, intercept, r, p, std_err = stats.linregress(x, y)
# print(r)
