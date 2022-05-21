# Proyecto Integrador
#Python inicial [ID: PI-9-20220307]

__author__ = "Francisco Soler"
__email__ = "fsolerpowell@gmail.com"
__version__ = "1.01"

"""
El objetivo de este proyecto Python es el análisis de distintos activos financieros y permitirle al usuario realizar las siguientes consultas
El usuario ingresa por consola que analisis desea realizar. De acuerdo al parametro ingresado solicitara que ingrese otra informacion por consona. 
Esta pordra ser, informacion de la negociación bursátillos(trade) o bien recibe una lista con los distintos activos disponibles para analizar.  
El programa en caso que sea necesario selecciona el archivo "CSV" donde se encuentra la información historia del activo (fecha, apertura, cierre, máximo, mínimo).

"""

import interfaz
import graficos




if __name__ == '__main__':
     program_bool=True
     while program_bool:
          graficos.print_main_menu()
          respusta_menu=interfaz.seleccionar_menu()

          if respusta_menu==1:
               #Punto de liquidacion en una negociacion bursatillos(trade)
               interfaz.punto_liquidacion()
          elif respusta_menu==2:
               #Máximos y mínimos históricos
               interfaz.open_ticker()
          elif respusta_menu==3:
               #Analizar toma de ganancias basado en retrocesos de Fibonacci
               interfaz.fibonacci_levels()
          elif respusta_menu==4:
               #Cálculo de la ratio risk/reward para fijar puntos de stopploss/take profit
               interfaz.ris_rew_ratio()
          elif respusta_menu==5:
               interfaz.analis_datos()
          elif respusta_menu==0:
               interfaz.settings()     
          else:
               print("Error: pongase en contacto con el desarrollador")
               quit()
          print("\n\n----------------------------------------------------------------")
          continua=input("\n\nDesea realizar otro análisis? \nSi desea realizar otro análisis escriba:SI\n")
          if  str.upper(continua)!="SI":
               program_bool=False
               print("Programa finalizo.")




