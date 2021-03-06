# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 19:02:25 2020

@author: USUARIO
"""

'''Hoy vamos a conocer Pandas!'''
'''Para eso vamos a utilizar algunas tablas de datos'''

#%%
import pandas as pd
#%%
'''Tabla clientes: resumen de compras por cliente de un ecommerce de comida'''

'''Con esta parte del código importamos el excel a Python'''
path = "C:\\Users\\USUARIO\\Desktop\\AT\\Clases_Python\\Python_for_ML\\clase_2"
df = pd.read_excel(path + "\\inputs\\customers.xlsx")
#%%
print(type(df))
#%%
'''Conoce tu tabla!!!'''
df_head = df.head(20)
print(df_head, df.columns, df.shape)
print(df.index)
#%%

'''Conoce los valores en tu tabla'''
df_description = df.describe()
print(df_description)

#%%

'''Algunas funciones al toque'''
print("Suma: ", df.sum())
print("Conteo: ", df.count())
print("Promedio: ", df.mean())
print("Desviacion estandar: ", df.std())
#%%

'''Las funciones tambien se pueden aplicar a una columna o algunas columnas especificas'''
print(df["evening_purchases"].sum(), type(df["evening_purchases"].sum()))
print("\n")
print(df[["evening_purchases", "lunch_purchases"]].sum(), type(df[["evening_purchases", "lunch_purchases"]].sum()))

#%%
'''Tambien funcionan para aplicarse a las columnas'''
print(df[["evening_purchases", "lunch_purchases"]].sum(axis = 1))
print(df.mean(axis = 1))

#%%

'''Respondemos'''
'''1. ¿Cuantas veces en promedio ha comprado un cliente?'''
respuesta_1 = df["purchases"].mean()
print(respuesta_1)
#%%
'''2. ¿Cuantos clientes han comprado en total? (Recuerda que cada fila es un cliente)'''
respuesta_2 = df["ID_customer"].count()
print(respuesta_2)

respuesta_2 = df.shape[0]
print(respuesta_2)

#%%
'''3. ¿Cuantos clientes han comprado por el app?'''

#%%
'''4. ¿Que porcentaje del total de los pedidos fueron hechos entre viernes y domingo?'''
viernes_domingo = df["frid_sund_purchases"].sum()
lunes_jueves = df["mon_thur_purchases"].sum()

print(viernes_domingo / (viernes_domingo + lunes_jueves))


#%%
'''5. ¿Cuanto valor compra en total un cliente promedio'''
'''6. ¿Cual es el ticket promedio de los clientes?'''

#%%

'''Podemos usar operadores matematicos entre las columnas'''
ratio_inactividad = df["frequency"] / df["inactive_days"]
print("\n")
print(ratio_inactividad)

print("\n")
print(type(ratio_inactividad), type(df), type(df["inactive_days"]))

'''Creamos una nueva columna que es el resultado de la division de otras dos'''
df["ratio_inactividad"] = df["frequency"] / df["inactive_days"]
print("\n")
print(df["ratio_inactividad"])

#%%

'''Ahora pasamos a una nueva df'''
df_soccer = pd.read_excel(path + "\\inputs\\soccer_matches.xlsx", sheet_name = "data")

#%%

'''Conoce tu df!!!'''
print(df_soccer.head(), df_soccer.columns, df_soccer.shape)

df_soccer_description = df_soccer.describe()
print(df_soccer_description)
#%%

'''Algunas funciones mas:'''

print("\n")
print(df_soccer["league"].unique(), df_soccer["league"].nunique())

print("\n")
print(df_soccer["league"].replace("Bundesliga 1", "Hola").unique())

print("\n")
print(df_soccer.head()["datetime"], "\n",
      df_soccer.sort_values(by = "datetime", ascending = False).head()["datetime"])

#%%
'''Valores faltantes: na'''

print("\n")
print(df_soccer.isna())

print("\n")
print(df_soccer.isna().sum(axis = 1))

print("\n")
print(df_soccer["yellow_cards_away"].isna().sum())

print("\n")
print(df_soccer.fillna(0))

#%%

'''Respondemos'''
'''1. ¿Cuantos equipos locales diferentes hay?'''

local = df_soccer["home_team"].nunique()
print(local)

#%%
'''2. ¿Cuales son los 10 partidos mas antiguos de la base?'''
df_soccer = df_soccer.sort_values(by = "datetime", ascending = True)
antiguos_10 = df_soccer[["datetime", "home_team", "away_team"]].head(10)
print(antiguos_10)

#%%
'''3. ¿Cuantos partidos no tuvieron tarjetas amarillas para los locales?'''
no_amarillas = df_soccer["yellow_cards_home"].isna().sum()
print(no_amarillas)

#%%
'''4. ¿Cuantos partidos si tuvieron tarjetas rojas?'''




#%%

'''Filtrar dataframes y acceder a celdas: iloc y loc'''

print("\n")
print(df_soccer.iloc[0], type(df_soccer.iloc[0]))

print("\n")
print(df_soccer.iloc[0:5], type(df_soccer.iloc[0:5]))

print("\n")
print(df_soccer["home_team"].iloc[5], type(df_soccer["home_team"].iloc[5]))

print("\n")
print(df_soccer["home_team"].iloc[0:5], type(df_soccer["home_team"].iloc[0:5]))

#%%
print("\n")
print(df_soccer["home_team"] == "Bayern Munich")

print("\n")
print(df_soccer.loc[df_soccer["home_team"] == "Bayern Munich"])

print("\n")
print(df_soccer.loc[df_soccer["home_team"] == "Bayern Munich"].head()[["home_team", "away_team"]])

lista_equipos = ["Atletico Madrid", "Real Madrid", "Barcelona"]
print("\n")
print(df_soccer.loc[df_soccer["home_team"].isin(lista_equipos)].head()[["home_team", "away_team"]])

print("\n")
print(df_soccer.loc[df_soccer["home_team"].isin(lista_equipos)]["home_team"].unique())

#%%

print("\n")
print((df_soccer["home_team"] == "Bayern Munich") | (df_soccer["away_team"] == "Bayern Munich"))

print("\n")
print(df_soccer.loc[(df_soccer["home_team"] == "Bayern Munich") | (df_soccer["away_team"] == "Bayern Munich")][["home_team", "away_team"]])

print("\n")
condition = (df_soccer["home_team"] == "Bayern Munich") & (df_soccer["away_team"] == "Bayer Leverkusen")
df_condition = df_soccer.loc[condition]
print(df_condition[["home_team", "away_team"]])

#%%

'''Respondemos'''
'''1. ¿Contra quien es el partido mas antiguo del Bayer Leverkusen como local en la base? (herramientas: loc, sort_values, iloc)'''

leverkusen = df_soccer.loc[df_soccer["home_team"] == "Bayer Leverkusen"].sort_values(by = "datetime", ascending = True)["away_team"].iloc[0]
print(leverkusen)

#%%
'''2. ¿Cuantos goles metio el Barcelona de local?'''
'''3. ¿Cuanto goles recibio el Real Madrid como local?'''
'''4. ¿Cual es el ratio de conversion (tiros / goles) del Werder Bremen?'''
#%%
'''5. ¿Cual es el promedio de goles totales en la Bundesliga? (herramientas: loc, suma de columnas, promedio de fila)'''

df_bundesliga = df_soccer.loc[df_soccer["league"] == "Bundesliga 1"]
total_goles = df_bundesliga["match_home_goals"].sum() + df_bundesliga["match_away_goals"].sum()
total_partidos = df_bundesliga.shape[0]
promedio_goles = total_goles / total_partidos

print(promedio_goles)

