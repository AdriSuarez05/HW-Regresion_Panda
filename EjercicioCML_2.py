# -*- coding: utf-8 -*-
"""
Created on Tue Jun  7 18:31:36 2022

@author: Adriana Suarez
"""

"""
email: adriana.suarezb@upb.edu.co
ID: 502197

"""

import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
from sklearn.metrics import r2_score 
import numpy


df = pd.read_excel(r'C:\Users\Adriana Suarez\my_python\Spyder\AirQualityUCI.xlsx', sheet_name='AirQualityUCI')

#2. https://archive.ics.uci.edu/ml/datasets/Air+Quality#
#Realizar una regresión lineal, polinomial y múltiple con los datos asociados. 
#Las variables escogidas son libres.

# Humedad relativa (%)
x = df['RH'][0 : 5001]
# AH Humedad absoluta
y = df['AH'][0 : 5001]



# REGRESION LINEAL

slope, intercept, r, p, std_err = stats.linregress(x, y)
print(r)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

# Diagrama de dispersión
plt.scatter(x, y)
plt.xlabel('Humedad relativa (%)')
plt.ylabel('AH Humedad absoluta')
plt.title('AH vs RH')

#Línea de regresión lineal
plt.plot(x, mymodel)
plt.show()

# Predecir valor de AH Humedad absoluta
ha_pred = myfunc(50)
print(ha_pred)



# # REGRESION POLINOMIAL
# mymodel = numpy.poly1d(numpy.polyfit(x, y, 3))

# # R cuadrado
# print(r2_score(y, mymodel(x)))

# # Cómo se mostrará la línea
# myline = numpy.linspace(-200, 200, 50)

# # Diagrama de dispersión
# plt.scatter(x, y)
# plt.xlabel('Humedad relativa (%)')
# plt.ylabel('AH Humedad absoluta')
# plt.title('AH vs RH')

# # Línea de regresión polinomial

# plt.plot(myline, mymodel(myline))
# plt.show()

# # Predecir valor de AH Humedad absoluta
# ha_pred = mymodel(60)
# print(ha_pred)



