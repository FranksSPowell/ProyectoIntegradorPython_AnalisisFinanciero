
from os import listdir
from os.path import isfile, join
import graficos
import os
import csv
import math
import shutil

def fun_decimales(numero):
    #Esta funcion toma el numero y acorde a su valor establece el numero de decimales
    "Requiere como parametro un valor"
    numero=abs(numero)
    if 0.0001<=numero<3: 
        return 4
    elif 3<=numero<10:
        return 2
    elif numero<=0.0001:
        return 9    
    else:
        return 0

def redondear_numero(numero):
    #Esta funcion toma el numero y acorde a su valor redondea el numero de decimales
    "Requiere como parametro un valor"
    numero=abs(numero)
    if 0.0001<=numero<3: 
        return round(numero,4)
    elif 3<=numero<10:
        return round(numero,2)
    elif numero<0.0001:
        return round(numero,9)    
    else:
        return round(numero,0)

def error_copy_def(A):
    #Remplaza el archivo settings por el default donde se encuentran los valores predefinidos
    "En caso de que se utilice en excent se puede pasar el parámetro (Error) para que imprima texto de que hubo un error "
    if A=="Error":print("Error 0001: Los valores se reiniciaron a su valor original")
    original = __file__.replace(os.path.basename(__file__),"default.csv")
    target = __file__.replace(os.path.basename(__file__),"settings.csv")
    shutil.copyfile(original, target)

#Aqui se asignan los valores predefinidos en el archivo CSV settings
try:
    directorio=__file__.replace(os.path.basename(__file__),"settings.csv")
    with open(directorio,"r",encoding='utf8') as file:
        settings= list(csv.DictReader(file))
    
    liq_rat     =float(settings[0]["Valor"])
    opcion_media=int(settings[1]["Valor"])
    x_factor=int(settings[3]["Valor"])
    valor_ref=str(settings[4]["Valor"])
    
#En caso de error corre funcion para restablecer todos los parametros
except:
    error_copy_def("Error")
    quit()

    


def seleccionar_menu():
    
    #Esta funcion seleciona el anális que se desea realizar
    """
    Devuelve una respuesta correcta entre las opciones deseadas
    No toma ningun parametro
    Devuelve respuesta en formato Int

    No requiere parametros
    """
    respuesta_counter_menu=1
    respuesta_bool_menu=True
    while respuesta_bool_menu:
   
        try:
            respuesta_menu=int(input("¿Qué análisis quiere realizar?:"))
        except:
            respuesta_menu=-1
        
        print("\n")
        if 0 <=respuesta_menu <6:
            return respuesta_menu
        elif respuesta_menu==9 or respuesta_counter_menu==3:
            print("Programa finalizo.")
            quit()
        else:
            print("La respuesta ingresada es incorrecta. Ingrese un nunero entre 1 y 5 o 0:")

        respuesta_counter_menu+=1
    #FIN DE seleccionar_menu
    
def punto_liquidacion():
    #Esta funcion indica que el punto de liquidacion de un determinado entrada
    
    """
    El usuario debera ingresar 3 valores: Precio de ingreso//leverage//tipo de posicion
    Precio de ingreso: es el valor de entrada a la operacion
    Leverage o Apalancamiento: es el valor en el cual esta apalancado en su posicion
    Tipo de posicion: si se encuentra LONG(LARGA) o SHORT(CORTA)
    No requiere parametros

    Contiene un contador que limita el numero de respuestas incorrectas
    """

    print("La liquidación se produce cuando el precio de referencia alcanza el precio de liquidación\n",
            " de una posición. Se recomienda a los traders que presten mucha atención al movimiento del\n",
            " precio de referencia y del precio de liquidación para evitar que sean liquidados. \n")
    bool_trade_type=True
    counter_trade_type=0
    while bool_trade_type:
        trade_type=str(input("Ingrese si es una posicion:\n 1) LARGA(LONG)\n 2) CORTA(SHORT)\n\nSu respuestas: "))
        """Considera valida todas las opciones en caso de que seleccione por el numero de lista
           o ponga la palabra tanto en ingles como español de su posicion     
        
        """

        if str.upper(str(trade_type))=="1" or str.upper(str(trade_type))=="LONG": trade_type="LARGA/LONG" 
        if str.upper(str(trade_type))=="2" or str.upper(str(trade_type))=="SHORT": trade_type="CORTA/SHORT"
        if trade_type=="LARGA/LONG" or trade_type=="CORTA/SHORT":
            bool_trade_type=False
            #print("CHECK OK FORMULA")
        else:
            if counter_trade_type==2: print("\nExcedio el numero de respuesas invalidas"),quit()
            print("\nRespuesta incorrecta\nRespuestas validas (1,2)\n----------------------------\n")
            counter_trade_type+=1
    
    
    counter_leverage=0
    bool_leverage=True
    
    while bool_leverage:
        if counter_leverage==3:
            print("\nExcedio el numero de respuesas invalidas")
            quit()
        try:
            trade_leverage=int(input("\nIngrese el nivel de apalancamiento: "))
    
        except:
            trade_leverage=0
        if 0 < trade_leverage <201:
            bool_leverage=False
           #print("CHECK OK FORMULA")
        else:
            counter_leverage+=1
            print("\nRespuesta incorrecta\nRespuestas validas (1 a 200)\n----------------------------\n")

    counter_price=0
    bool_price=True

    while bool_price:
        try:
            trade_price=float(input("Ingrese el precio de entrada: "))
        except:
            print("El valor ingresado es incorrecto: ingrese un valor positivo, mayor a 0")
            trade_price=0

        if 0 < trade_price:
            bool_price=False
            #print("CHECK OK FORMULA")
        else:
            if counter_price==3: print("\nExcedio el numero de respuesas invalidas"),quit()
            print("\nRespuesta incorrecta\nRespuestas valor positivo mayor a 0\n----------------------------\n")
            counter_price+=1

    
    
    punto_de_liquidacion=0
    if trade_type=="LARGA/LONG":
        #punto_de_liquidacion=trade_price/(trade_leverage/(trade_leverage-1))
        punto_de_liquidacion=(trade_price*trade_leverage)/((trade_leverage+1)-(liq_rat*trade_leverage))
    elif trade_type=="CORTA/SHORT":
        #punto_de_liquidacion=trade_price*(trade_leverage+1/(trade_leverage))
        punto_de_liquidacion=(trade_price*trade_leverage)/((trade_leverage-1)+(liq_rat*trade_leverage))
    
    
    graficos.print_word_PDL()
    
    print("-------------------------------")
    print("Tipo de entrada: ", trade_type)
    print("Para un precio de ingreso de :         ","{}".format(redondear_numero(trade_price)))
    print("Con un nivel de apalancamiento de :    ",trade_leverage)
    print("El punto de liquidacion aproximado es: ", "{}".format(redondear_numero(punto_de_liquidacion)))
   
    return punto_de_liquidacion
#FIN DE punto_liquidacion


# OPCION 2 #


def open_ticker():
    #Esta funcion nos brinda parametros de maximos, minimos y medias
    
    """
    El usuario selecciona de la lista de ACTIVOS cual desea analizar
    Puede realizar la seleccion por medio de el numero en la lista o
    poniendo el TICKER o siglas del activo

    Es posible agregar mas activos. Esto se hace dentro de la carpeta ACTIVOS
    debe realizarce con archivos CSV exportados de tradingview(tiempo DIAS)

    No requiere parametros

    Contiene un contador que limita el numero de respuestas incorrectas
    """

    try:
        counter_ticker=0
        bool_ticker=True
        while bool_ticker:
            if str.upper((input("Desea ver la lista de tickers disponibles(SI/NO):")))=="SI":
                directorio_file=__file__.replace(os.path.basename(__file__),"\\activos")
                onlyfiles = [f for f in listdir(directorio_file) if isfile(join(directorio_file, f))]
                for i in range(len(onlyfiles)):
                    print(i+1,") ",onlyfiles[i].replace(".csv",""))
            
                lista_tickers=onlyfiles
            else:
                lista_tickers=[]     
            ticker=input("Ingrese el ticker/código especifico del activo financiero (ej:BTCUSD, AAPL): ")
            print("\n")
            try:
                if ticker.isnumeric():
                    ticker= lista_tickers[int(ticker)-1]
                    directorio=__file__.replace(os.path.basename(__file__),"activos\\{}".format(ticker))
                else:
                    directorio=__file__.replace(os.path.basename(__file__),"activos\\{}.csv".format(ticker))
                with open(directorio,"r",encoding='utf8') as file:
                    activo= list(csv.DictReader(file))
                bool_ticker=False
            except:
                print("El ticker/código ingresado no se encuentra disponible ")   
                counter_ticker+=1
                if counter_ticker==3: 
                    print("Exedio el maximo de respuestas incorrectas.")
                    quit()     

        max_val        =max(activo, key=lambda x:x["high"])
        min_val        =min(activo, key=lambda x:x["low"])
        media_mobil_par=0
        hl2_par        =0
        hlc3_par       =0

        


        if len(activo)<opcion_media:
            media_valor= len(activo)
        else:
            media_valor=opcion_media

        
        for value in activo:
            apert=  float(value["open"])
            high =  float(value["high"])
            low  =  float(value["low"])
            close=  float(value["close"])
            
            ohlc =  (apert+high+low+close)/4
            hl2  =  (high+low)/2
            hlc3 =  (high+low+close)/3
            
            if (len(activo)-media_valor)<=activo.index(value): media_mobil_par +=ohlc
            if (len(activo)-media_valor)<=activo.index(value):hl2_par +=hl2
            if (len(activo)-media_valor)<=activo.index(value):hlc3_par +=hlc3


        media_mobil=media_mobil_par/media_valor
        media_hl2  =hl2_par/media_valor
        media_hlc3 =hlc3_par/media_valor
        
        decimals   =fun_decimales(media_mobil)
        
        graficos.print_word_analicis()

        print("EL ACTIVO: ",ticker.replace(".csv",""))
        print("----------------------------------------")
        print("MEDIA EN BASE A {} SESIONES".format(media_valor))

        print("El valor maximo alcanzado es de: {:.{}f}".format(float(max_val["high"]),decimals))
        print("El valor minimo alcanzado es de: {:.{}f}".format(float(min_val["low"]),decimals))
        print("El valor OHLC  medio es de:      {:.{}f}".format(media_mobil,decimals))
        print("El valor HL2  medio es de:       {:.{}f}".format(media_hl2,decimals))
        print("El valor hlc3  medio es de:      {:.{}f}".format(media_hlc3,decimals))

        list_activo_analisis=[max_val["high"],min_val["low"],media_mobil,media_hl2,media_hlc3]
        return list_activo_analisis

    except ValueError:
        print("Error: on reading file, please reach to support@generala.eth")

#FIN DE open_ticker()
    
    #OPCION 3

def fibonacci_levels():

    #Analisis de los niveles de Fibonacci    
    """
    Los retrocesos de Fibonacci son un método para determinar potenciales 
    niveles de resistencia o soporte en el precio de un instrumento financiero.

    Para realizar el analisis se deben ingresar dos variables, el MAXIMO y MINIMO
    luego determinar si estamos analizando un mercado BULL(TORO/Alcista) o un mercado
    BEAR(OSO/Bajista)
    La funcion nos devolvera los puntos de resistencia  
    
    No requiere parametros

    Contiene un contador que limita el numero de respuestas incorrectas
    """

    bool_fib=True
    counter_fib=0

    val_ret_fib_23=0.236
    val_ret_fib_38=0.382
    val_ret_fib_61=0.618
    val_ret_fib_78=0.786
    
    val_ext_fib_23=1.7860
    val_ext_fib_38=1.7640
    val_ext_fib_61=1.5000
    val_ext_fib_78=1.272

    mercado_fib=0
    max_fib=0.0
    min_fib=0.0

    while bool_fib:
        print("Indique si desea analizar un mercado\n 1) Alcista\n 2) Bajista:")
        while mercado_fib !=1 and mercado_fib !=2: 
            try:
                mercado_fib=int(input("Ingrese tipo de mercado:  "))
                if mercado_fib !=1 and mercado_fib !=2:
                    counter_fib+=1
                if counter_fib==3: 
                    print("Exedio el maximo de respuestas incorrectas.")
                    quit()
            except:
                print("Las variable ingresada es incorrecta")
                print("\nRespuestas validas 1 o 2\n")
                counter_fib+=1
                if counter_fib==3: 
                    print("Exedio el maximo de respuestas incorrectas.")
                    quit()


        counter_fib=0
        while max_fib<=min_fib or max_fib==0 and min_fib==0 :
            try:
                max_fib=float(input("Ingrese el valor Maximo: "))
                min_fib=float(input("Ingrese el valor Minimo: "))
                range_fib=max_fib-min_fib
                decimals=fun_decimales(max_fib)
                if  max_fib<=min_fib:
                    print("Alguna de las variables ingresadas es incorrecta")
                    print("El valor maximo siempre tiene que ser mayor al valor minimo")
                    counter_fib+=1
                if counter_fib==3: 
                    print("Exedio el maximo de respuestas incorrectas.")
                    quit()
            except:
                print("Alguna de las variables ingresadas es incorrecta")
                print("El valor maximo siempre tiene que ser mayor al valor minimo")
                counter_fib+=1
                if counter_fib==3: 
                    print("Exedio el maximo de respuestas incorrectas.")
                    quit()

        print("\n----------------------------\n")

        

        
        
        #Cada tipo de mercado tiene un calculo diferente
        "Aqui se realiza el calculo para el mercado Alcista "
        if  mercado_fib==1 and max_fib > min_fib :
            fib_23_ret=max_fib-(val_ret_fib_23*range_fib)
            fib_38_ret=max_fib-(val_ret_fib_38*range_fib)
            fib_61_ret=max_fib-(val_ret_fib_61*range_fib)
            fib_78_ret=max_fib-(val_ret_fib_78*range_fib)
            
            fib_23_ext=min_fib+(val_ext_fib_23*range_fib)
            fib_38_ext=min_fib+(val_ext_fib_38*range_fib)
            fib_61_ext=min_fib+(val_ext_fib_61*range_fib)
            fib_78_ext=min_fib+(val_ext_fib_78*range_fib)
            
            lista_fib=[[fib_23_ret,fib_38_ret,fib_61_ret,fib_78_ret],[fib_23_ext,fib_38_ext,fib_61_ext,fib_78_ext]]
            
            graficos.print_word_RDF()
            print("\n----------------------------------------------------------------\n")

            print("{:<10} {:<10} {:<10} {:<10}".format('RETROCESO','','EXTENSION',''))
            print("{:<10} {:<10} {:<10} {:<10}".format('%','Retroceso','%','Extension'))    
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_23,3,fib_23_ret,decimals,val_ext_fib_23,3,fib_23_ext,decimals))
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_38,3,fib_38_ret,decimals,val_ext_fib_38,3,fib_38_ext,decimals))
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_61,3,fib_61_ret,decimals,val_ext_fib_61,3,fib_61_ext,decimals))
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_78,3,fib_78_ret,decimals,val_ext_fib_78,3,fib_78_ext,decimals))
            
            
            bool_fib=False
            return lista_fib

            #Cada tipo de mercado tiene un calculo diferente
            "Aqui se realiza el calculo para el mercado Bajista "
        elif mercado_fib==2 and max_fib > min_fib:
            fib_78_ret=min_fib+(val_ret_fib_78*range_fib)
            fib_78_ret=min_fib+(val_ret_fib_61*range_fib)
            fib_38_ret=min_fib+(val_ret_fib_38*range_fib)
            fib_23_ret=min_fib+(val_ret_fib_23*range_fib)

            fib_78_ext=max_fib-(val_ext_fib_78*range_fib)
            fib_61_ext=max_fib-(val_ext_fib_61*range_fib)
            fib_38_ext=max_fib-(val_ext_fib_38*range_fib)
            fib_23_ext=max_fib-(val_ext_fib_23*range_fib)

            lista_fib=[[fib_78_ret,fib_78_ret,fib_38_ret,fib_23_ret],[fib_78_ext,fib_61_ext,fib_38_ext,fib_23_ext]]
            
            graficos.print_word_RDF()
            print("\n----------------------------------------------------------------\n")
            print("{:<10} {:<10} {:<10} {:<10}".format('RETROCESO','','EXTENSION',''))
            print("{:<10} {:<10} {:<10} {:<10}".format('%','Retroceso','%','Extension'))    
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_78,3,fib_78_ret,decimals,val_ext_fib_78,3,fib_78_ext,decimals))
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_61,3,fib_61_ret,decimals,val_ext_fib_61,3,fib_61_ext,decimals))
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_38,3,fib_38_ret,decimals,val_ext_fib_38,3,fib_38_ext,decimals))
            print("{:<10.{}f} {:<10.{}f} {:<10.{}f} {:<10.{}f}".format(val_ret_fib_23,3,fib_23_ret,decimals,val_ext_fib_23,3,fib_23_ext,decimals))
            bool_fib=False

            return lista_fib

        else:
            print("Alguna de las variables ingresadas es incorrecta")
            print("Respuestas validas (1,2):\n")
            if counter_fib==3: 
                print("Exedio el maximo de respuestas incorrectas.")
                quit()
            counter_fib+=1

    
    #FIN DE fibonacci_levels()   

    
    #OPCION 4
def ris_rew_ratio():
    #Analisis de indice de Retorno sobre el riego  
    """
    El riesgo es la distancia desde el precio de entrada hasta el stop loss 
    y representa el riesgo que está dispuesto a asumir en esta operación.


    No requiere parametros

    Contiene un contador que limita el numero de respuestas incorrectas
    """



    bool_ris_rew   =True
    counter_ris_rew=0
    countr_posicion=0
    while bool_ris_rew:
        try:
            trade_type=input("Indique si desea analizar posición\n 1) Larga/Long \n 2) Corta/Short\nSu posición es: ")
            if str.upper(str(trade_type))=="1" or str.upper(str(trade_type))=="LONG" or str.upper(str(trade_type))=="LARGA": trade_type="LARGA/LONG" 
            if str.upper(str(trade_type))=="2" or str.upper(str(trade_type))=="SHORT"or str.upper(str(trade_type))=="CORTA": trade_type="CORTA/SHORT"      
            
            'Breakeven Win rate = Risk Rate / (Risk Rate + Reward Rate)'
              #Risk/Reward Ratio = (Entry Price – Stop Loss Price) / (Take Profit Price – Entry Price)
              #Risk/Reward Ratio = (Entry Price – Stop Loss Price) / (Take Profit Price – Entry Price)   

            


            
            if trade_type=="LARGA/LONG":
                
                while bool_ris_rew: 
                    try:
                        entry_factor      =float(input("Ingrese el valor de entrada:"))
                        stopp_loss_factor =float(input("Ingrese el valor de Stop Loss/detener pérdidas:"))
                        take_profit_factor=float(input("Ingrese el valor de Take Profit/Tomar ganancia:"))

                        print("\n")
                        if stopp_loss_factor < entry_factor < take_profit_factor: 
                            bool_ris_rew=False
                        else:
                            print("El valor de ENTRADA tiene que ser mayor al STOPP LOSS y menor al TAKE PROFIT")
                            countr_posicion+=1
                            if countr_posicion>=3: 
                                print("Excedio el numero de respuesas invalidas")
                                quit()
                    except:
                        if countr_posicion>=3:  
                            exit()
                        print("La variable ingresada es incorrecta\n")
                        counter_ris_rew+=1                        



                rew_factor =(take_profit_factor - entry_factor)      
                risk_factor=(entry_factor - stopp_loss_factor)

                rew_avr_factor  =rew_factor/risk_factor
                breakeven_factor=(risk_factor/(risk_factor+rew_factor))*100

                
                factor_alto =x_factor/(take_profit_factor- stopp_loss_factor)                
                take_alto  =int(round(x_factor-(factor_alto*entry_factor),0))
                stopp_alto   =int(x_factor-take_alto)


                graficos.print_word_RRR()
                print("\n----------------------------\n")

                print(" _______ {} Take Profit".format(take_profit_factor))
                for i in range(take_alto):
                    print("|       |")
                print("|_______| {} Entrada".format(entry_factor))
                for i in range(stopp_alto):
                    print("|       |")
                print("|_______| {} Stopp Loss".format(stopp_loss_factor))


  

                print("\n\nRisk/Reward Ratio= 1:{}".format(redondear_numero(rew_avr_factor)))
                print("Breakeven Win Rate = {} %\n".format(redondear_numero(breakeven_factor)))

                print("Este resultado muestra:\nQue el {}% de todas las transacciones deben ser ganadoras para que sea rentable.".format(redondear_numero(breakeven_factor)))
                print("Por cada unidad monetaria arriesgada, espera ganar {} unidades.".format(redondear_numero(rew_avr_factor)))

                return rew_avr_factor, breakeven_factor

            elif trade_type=="CORTA/SHORT":

                while bool_ris_rew: 
                    try:
                        entry_factor=float(input("Ingrese el valor de entrada:"))
                        stopp_loss_factor=float(input("Ingrese el valor de Stop Loss/detener pérdidas:"))
                        take_profit_factor=float(input("Ingrese el valor de Take Profit/Tomar ganancia:"))

                        print("\n")
                        if stopp_loss_factor > entry_factor > take_profit_factor: 
                            bool_ris_rew=False
                        else:
                            print("El valor de ENTRADA tiene que ser mayor al TAKE PROFIT y menor al STOPP LOSS ")
                            countr_posicion+=1
                            if countr_posicion>=3: print("Excedio el numero de respuesas invalidas"),quit()
                    except:
                        if countr_posicion>=3:  
                            exit()
                        print("La variable ingresada es incorrecta\n")
                        counter_ris_rew+=1      

                rew_factor=(entry_factor - take_profit_factor)      
                risk_factor=(stopp_loss_factor - entry_factor)

                rew_avr_factor=rew_factor/risk_factor
                breakeven_factor=(risk_factor/(risk_factor+rew_factor))*100

                
                factor_alto =x_factor/(stopp_loss_factor-take_profit_factor )                
                take_alto   =int(round(x_factor-(factor_alto*entry_factor),0))
                stopp_alto  =int(x_factor-take_alto)


                graficos.print_word_RRR()

                print("\n----------------------------\n")

                print(" _______ {} Stopp Loss".format(stopp_loss_factor))
                for i in range(take_alto):
                    print("|       |")
                print("|_______| {} Entrada".format(entry_factor))
                for i in range(stopp_alto):
                    print("|       |")
                print("|_______| {} Take Profit".format(take_profit_factor))
                
                


                print("\n\nRisk/Reward Ratio= 1:{}".format(redondear_numero(rew_avr_factor)))
                print("Breakeven Win Rate = {} %\n".format(redondear_numero(breakeven_factor)))

                print("Este resultado muestra:\nQue el {}% de todas las transacciones deben ser ganadoras para que sea rentable.".format(redondear_numero(breakeven_factor)))
                print("\nPor cada unidad monetaria arriesgada, espera ganar {} unidades.".format(redondear_numero(rew_avr_factor)))

                return rew_avr_factor, breakeven_factor

            else:

                print("\nLa variable ingresada es incorrecta\n")
                counter_ris_rew+=1

        except:
            if counter_ris_rew>=2 or countr_posicion>=3:  
                print("El programa finalizara ahora.")
                exit()
            print("La variable ingresada es incorrecta\n")
            counter_ris_rew+=1

    #FIN DE ris_rew_ratio()

#OPCION 5---------------------------------------------------------------------------------

def analis_datos():
    #Esta funcion realiza un analisis de comparacion de dos activos financieros
    
    
    """
    El usuario selecciona de la lista de ACTIVOS cuale desea analizar
    Puede realizar la seleccion por medio de el numero en la lista o
    poniendo el TICKER o siglas del activo

    Es posible agregar mas activos. Esto se hace dentro de la carpeta ACTIVOS
    debe realizarce con archivos CSV exportados de tradingview(tiempo DIAS)

    No requiere parametros

    Contiene un contador que limita el numero de respuestas incorrectas
    """

    lista_activos_analisis=[]
    lista_tickers=[]

    try:
        counter_ticker=0
        bool_ticker=True
        numero_activos=2

        while bool_ticker:
            
            counter=0

            if str.upper((input("Desea ver la lista de tickers disponibles(SI/NO):")))=="SI":
                directorio_file=__file__.replace(os.path.basename(__file__),"\\activos")
                onlyfiles = [f for f in listdir(directorio_file) if isfile(join(directorio_file, f))]
                for i in range(len(onlyfiles)):
                    print(i+1,") ",onlyfiles[i].replace(".csv",""))
            
                lista_tickers_val=onlyfiles
            else:
                lista_tickers_val=[]     
            
            for i in range(numero_activos):
                ticker=input("Ingrese el ticker/código especifico del activo financiero (ej:BTCUSD, AAPL): ")
                #ticker="ADAUSD"
                print("\n")
                i={}
                try:
                    if ticker.isnumeric():
                        ticker= lista_tickers_val[int(ticker)-1]
                        directorio=__file__.replace(os.path.basename(__file__),"activos\\{}".format(ticker))
                        i["Ticker"]=ticker.replace(".csv","")
                        lista_tickers.append(i)
                    else:
                        directorio=__file__.replace(os.path.basename(__file__),"activos\\{}.csv".format(ticker))
                        i["Ticker"]=ticker
                        lista_tickers.append(i)
                    with open(directorio,"r",encoding='utf8') as file:
                        i= list(csv.DictReader(file))
                        lista_activos_analisis.append(i)
                        counter+=1


                except:
                    print("El ticker/código ingresado no se encuentra disponible ")   
                    counter_ticker+=1
                    if counter_ticker==3: 
                        print("Exedio el maximo de respuestas incorrectas.")
                        quit()
                    break
            
            if counter==numero_activos:bool_ticker=False
        
        
        y=0
        for x in range(len(lista_activos_analisis)):
            while y < len(lista_activos_analisis[x]):

                check=lista_activos_analisis[x][y]['time'][:10]

                for j in range(len(lista_activos_analisis)):
                    if lista_activos_analisis[x]!=lista_activos_analisis[j]:
                        for i in range(len(lista_activos_analisis[j])):
                            contador=0
                            if check==lista_activos_analisis[j][i]['time'][:10]:
                                contador+=1
                                break
                        if contador==0: 
                            del lista_activos_analisis[x][y]
                            y-=1
                y+=1
            y=0
    
        control=True
        for x in range(len(lista_activos_analisis)):
            for j in range(len(lista_activos_analisis)):
                for i in range(len(lista_activos_analisis[x])):
                    if lista_activos_analisis[x][i]['time'][:10]!=lista_activos_analisis[j][i]['time'][:10]: control=False

        temp_list =[]  
        temp_list2=[]  

        if len(lista_activos_analisis[0])==len(lista_activos_analisis[1]) and len(lista_activos_analisis[1])>25 and control==True:  

            for lista_activos in range(len(lista_activos_analisis)):
                temp_list_fecha=[]
                for i in range(len(lista_activos_analisis[0])):
                    temp_list_fecha.append(lista_activos_analisis[lista_activos][i]['time'][:10]) 
                        #lista_temporal=[lista_activos_analisis[0][i]['time'][:10]]
                        #lista_para_calculo.append(lista_temporal)
                lista_tickers[lista_activos]["FECHA"]=temp_list_fecha
                
                
                
                
                temp_list =[]
                temp_list2=[]
                for valores_activos in range(len(lista_activos_analisis[0])):
                    temp_list.append(float(lista_activos_analisis[lista_activos][valores_activos][valor_ref]))
                    if valores_activos>0:
                        temp_list2.append(((float(lista_activos_analisis[lista_activos][valores_activos][valor_ref])
                                        -float((lista_activos_analisis[lista_activos][valores_activos-1][valor_ref]))
                                        )/float(lista_activos_analisis[lista_activos][valores_activos-1][valor_ref])))
                    else:
                        temp_list2.append(0)
            
                #REALIZA EL CALCULO DEL RENDIMIENTO y OBTIENE EL RENDIMIENTO MEDIO

                lista_tickers[lista_activos][valor_ref]=temp_list
                lista_tickers[lista_activos]["ren"]=temp_list2
                lista_tickers[lista_activos]["Ren_Med"]=sum(temp_list2)/(len(temp_list2)-1)

                varianza=[]
                cal_covarianza=[]

                for i in range(len(temp_list2)):
                    varianza.append((temp_list2[i]- lista_tickers[lista_activos]["Ren_Med"])**2)
                
                for i in range(len(temp_list2)):
                    cal_covarianza.append((temp_list2[i]- lista_tickers[lista_activos]["Ren_Med"]))
                

                lista_tickers[lista_activos]["cal_covarianza"]=cal_covarianza
                lista_tickers[lista_activos]["varianza"]=varianza
                lista_tickers[lista_activos]["sum_varianza"]=sum(varianza)/(len(temp_list2)-1)
                
    
                lista_tickers[lista_activos]["desvio"]=math.sqrt(float(lista_tickers[lista_activos]["sum_varianza"]))
                


            

        else:
            print("Los activos seleccionados no cumplen las condiciones necesarias para realizar una comparacion.")
        

        covarianza = sum([x*y for x,y in zip(lista_tickers[0]["cal_covarianza"],lista_tickers[1]["cal_covarianza"])])/len(lista_tickers[0]["cal_covarianza"])
        correlacion=covarianza/(lista_tickers[0]["desvio"]*lista_tickers[1]["desvio"])

        graficos.print_word_analicis()

        for i in range(len(lista_tickers)):
            print("El activo a analizar es: ",lista_tickers[i]["Ticker"])
            print("Rendimiento medio es: {} %".format(redondear_numero(lista_tickers[i]["Ren_Med"]*100)))
            print("Su desvio es: ",redondear_numero(lista_tickers[i]["desvio"]*100)," %")
            print("Muestras analizadas: ",len(lista_tickers[i][valor_ref])-1)
            print("\n")
            

        print("Entre ambos activos ")
        print("La covarianza es de: ",redondear_numero(covarianza*100)," %")
        
        print("Existe una correlacion de: ",redondear_numero(correlacion*100)," %")


        return redondear_numero(correlacion*100)

        
    except ValueError:
        print("Error: on reading file, please reach to support@generala.eth")
        
    #FIN DE analis_datos()


def settings():
    #Esta funcion nos permite modificar el archivo settings
    
    
    """
    
    No requiere parametros

    """


    directorio=__file__.replace(os.path.basename(__file__),"settings.csv")
    with open(directorio,"r",encoding='utf8') as file:
        settings= list(csv.DictReader(file))
        dict_from_csv = dict(settings[0])
        header = list(dict_from_csv.keys())
        
    graficos.print_word_settings()

    bool_settings=True
    while bool_settings:
        for i in range(len(settings)):
            print("Opcion: {:<1}  {:<20} VALOR: {:<40}".format(i+1,settings[i]["NombreVariable"],settings[i]["Valor"]))

        print("Opcion: 0  SALIR")
        print("Opcion: D  Volver parametros a valores originales")
        
        respuesta_settings=input("\nIndique que opcion quiere modificar: ")
        

        if respuesta_settings  =="1":
            try:
                valor_opc1=float(input("Indique el valor del Ratio de Liquidacion(Valor sugerido=0.0059): "))
                if 1>=valor_opc1>0:
                    settings[int(respuesta_settings)-1]["Valor"]=valor_opc1
                else:
                    print("Valor invalido. Tiene que ser un numero menor a 1 y mayor a 0")
            except:
                print("Valor invalido. Tiene que ser un numero menor a 1 y mayor a 0")
        elif respuesta_settings=="2":
            try:
                valor_opc2=float(input("Indique la cantidad de sesiones que quiere considerar(mayor a 2): "))
                if valor_opc2>=2:
                    settings[int(respuesta_settings)-1]["Valor"]=valor_opc2
                else:
                    print("Valor invalido. Tiene que ser un mayor a 2")
            except:
                print("Valor invalido. Tiene que ser un mayor a 2")
            
        elif respuesta_settings=="3":
            ""
        elif respuesta_settings=="4":
            try:
                valor_opc4=float(input("Indique la cantidad de sesiones que quiere considerar(mayor a 2): "))
                if 20>=valor_opc4>2:
                    settings[int(respuesta_settings)-1]["Valor"]=valor_opc4
                else:
                    print("Valor invalido. Tiene que ser un numero menor a 20 y mayor a 2")
            except:
                print("Valor invalido. Tiene que ser un numero menor a 20 y mayor a 2")

        elif respuesta_settings=="5":
            print("\n Indique que variable quiere tomar para los indices: ")
            largo_opciones=str(settings[int(respuesta_settings)-1]).count("Valores")
            for i in range(largo_opciones):
                print(i+1,")",settings[int(respuesta_settings)-1]["Valores{}".format(i+1)])

            try:
                valor_opc5=int(input("Indique la variable: "))
                for i in range(largo_opciones):
                    if i+1==valor_opc5:settings[int(respuesta_settings)-1]["Valor"]=settings[int(respuesta_settings)-1]["Valores{}".format(i+1)]
            
            except: print("Valor invalido")
           
        elif respuesta_settings=="0":
            bool_settings=False
        elif respuesta_settings=="D" or respuesta_settings=="d":
            error_copy_def("OK")
        else:
            print("Respuesta invalida. Las respuestas validas son del 1 al 5, 0 o D\n")
        if str.upper(input("Quiere modificar alguna opcion (SI/NO): "))!="SI":bool_settings=False
    
    
    for i in range(len(settings)):
        print("{:<5}:  {:<20} VALOR: {:<40}".format(settings[i]["OPCION"],settings[i]["NombreVariable"],settings[i]["Valor"]))

    try:
        
        with open(directorio,"w", newline='',encoding='utf8') as file:
            
            writer = csv.DictWriter(file, fieldnames=header)
            writer.writeheader()
            writer.writerows(settings)
    except:
        error_copy_def("Error")