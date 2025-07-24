#importacion de librerias
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#lectura de datos
data = pd.read_csv("Datos_maquinaria.csv")
#verifico el tamaño de set de datos (15747 filas,20 columnas)
print(data.shape)
#imprimo las primeras5 filas para darme una idea de la informacion
print(data.head())


#elimo filas no relevantes para el analis
data =  data.drop(columns=["M.O MEM","No.OC","OT","Observaciones","Falta servicio","Jefe de Taller","SN / Placa","Analista","Fecha de programación"])
#borramos todas las filas que no tenga maquina 
data = data[data["No. Economico"].astype(str).str.strip() != ""] 
#astype(str): asegura que los valores se traten como texto
# .str.strip(): elimina espacios en blanco.
#!= "": mantiene solo las filas que no están vacías.

data["No.OMP"] = pd.to_numeric(data["No.OMP"],errors = "coerce").astype("Int32")#convierto de objeto a numero 
#errors="coerce" convierte los valores no numéricos a NaN.
#utilzo Int 32 porque las ordenes de sap no son mayores de 8 digitos 

data = data.dropna(subset=["No.OMP"])# elimino valores vacios
data = data.drop_duplicates(subset=["No.OMP"])#elimino valores repetidos
# se puede resumir con la linea data = data.dropna(subset=["No.OMP"]).drop_duplicates(subset=["No.OMP"])
data["Horas Reales"] = pd.to_numeric(data["Horas Reales"], errors = "coerce").astype("Float64")#convierto de objeto a numero 
data["Horas Teoricas"] = pd.to_numeric(data["Horas Teoricas"], errors = "coerce").astype("Float64")#convierto de objeto a numero 

data = data[(data["Horas Reales"].notna()) & (data["Horas Reales"] != 0)] #quito valores vacios y 0
data["Fecha de servicio"] = pd.to_datetime(data["Fecha de servicio"],dayfirst=True, errors='coerce')#convierto de objeto a fecha 

categorias_columnas = ["CeCo","No. Economico","No.OMP","Fecha de servicio","Horas Reales","Propietario Del equipo","Maquina","Marca","Modelo"]

#verirficamos tipos de dato por columna y sus registros 
print(data.info())

for categoria in categorias_columnas:
    print(f"Columna {categoria}: {data[categoria].nunique()} subniveles")#si el subnivel es 1 se puede eliminar la columna
    if categoria == "CeCo":
        print(data[categoria].value_counts())#verificando los CeCo correctos
        print('-'*20)#separador

#Creo listas con valores unicos de no de equipo y tipo de maquina
numero_economico = list(set(data["No. Economico"].tolist()))
tipo_maquina = list(set(data["Maquina"].tolist()))


intervalo_mantenimiento = 250 #varia en algunas maquinas
analisis = []

for equipo in numero_economico:
    filtro = data[data["No. Economico"] == equipo ]
    horas_trabajadas = int (filtro["Horas Reales"].max() - filtro["Horas Reales"].min())
    if horas_trabajadas == 0 :
        horas_trabajadas = int (filtro["Horas Reales"].max() - filtro["Horas Teoricas"].min())
    numero_de_mantenimientos = int((data["No. Economico"] == equipo).sum())
    promedio_horas_entre_mantenimiento = horas_trabajadas / numero_de_mantenimientos
    porcentaje_desvio = 100*((promedio_horas_entre_mantenimiento - intervalo_mantenimiento)/intervalo_mantenimiento)
    if porcentaje_desvio < 0:
        porcentaje_desvio = 0
    analisis.append([equipo,horas_trabajadas,numero_de_mantenimientos,round(porcentaje_desvio,1)])

df_analisis = pd.DataFrame(analisis,columns = ["No.Economico","Hr Trabajadas","No.de Mttos","Desvio"])
df_analisis.to_csv('reporte_resultado.csv', index= False)