# Proyecto Integrador Python_AnalisisFinanciero
Este proyecto integrador python tiene por objetivo  es poner en práctica los conocimientos obtenidos a lo largo de la cursada
de Python inicial [ID: PI-9-20220307] Inove

El objetivo de este proyecto Python es el análisis de distintos activos financieros y permitirle al usuario realizar las siguientes consultas

 

El usuario ingresa por consola que analisis desea realizar. De acuerdo al parametro ingresado solicitara que ingrese otra informacion por consona. Esta pordra ser, informacion de la negociación bursátillos(trade) o bien recibe una lista con los distintos activos disponibles para analizar.  El programa en caso que sea necesario selecciona el archivo "CSV" donde se encuentra la información historia del activo (fecha, apertura, cierre, máximo, mínimo).

 

Los análisis que podrá consultar el usuario son 

 

1.       Punto de liquidación en una negociación bursátillos(trade)

2.       Máximos y mínimos históricos

3.       Analizar toma de ganancias basado en retrocesos de Fibonacci

4.       Cálculo de la ratio risk/reward para fijar puntos de stopploss/take profit

5.       Análisis para un activo financiero de:

<h3 dir="auto"><strong>MENU INICIAL</strong>:</h3> 


![image](https://user-images.githubusercontent.com/101218360/169633530-c572059f-e21e-4b7a-ab40-a8c9484006b3.png)


El usuario ingresa por consola que opcion desea, una vez ingresado se verifica que la opcion sea valida, en caso que no lo sea,
se incremente un contador en uno, en caso de ingresar tres respuestas incorrectas el programa se finaliza.

![image](https://user-images.githubusercontent.com/101218360/169633057-362f5908-bcd3-45f9-930f-99dbd2986883.png)


<h3 dir="auto"><strong>Work Flow</strong>:</h3> 


![Untitled Diagram (2)](https://user-images.githubusercontent.com/101218360/169633937-06fb5bdf-6e69-4011-9180-51a497a425f6.jpg)


<h3 dir="auto"><strong>Detalle del procesos 2</strong>:</h3> 


![Proceso 2 drawio (1)](https://user-images.githubusercontent.com/101218360/169631264-c5dc2b8a-165a-4c5d-aeee-9e757ba842f9.jpg)


Podemos encontrar dos archivos principales. Main e Interfaz

En el archivo interfaz se encuentran todas las funciones y codigos para corre cada uno de los analisis:

Cada analisis tiene una funcion a la cual se llama, y esta imprime en la terminal la informacion de opcion.


![image](https://user-images.githubusercontent.com/101218360/169633298-04d8ca8c-c714-4250-8bb0-c80e872697f9.png)

 

![image](https://user-images.githubusercontent.com/101218360/169631300-62312569-b5cf-428f-8f25-344a441b4fa7.png)

<h3 dir="auto"><strong>ARCHIVO: ACTIVO.csv</strong>:</h3>


Se utilizaran archivos tipo CSV con información de acciones. Se identifican con el simbolo o ticker.
Estos contiene Fecha, precio de apertura, cierre, máximo y mínimo.

[AAPL.csv](https://github.com/FranksSPowell/ProyectoIntegradorPython_AnalisisFinanciero/files/8746875/AAPL.csv)


![image](https://user-images.githubusercontent.com/101218360/169631341-f8d7aed4-9ce7-4346-a293-c8b53c38a717.png)


Estos se amacenan en una carpeta ACTIVOS. Puedena ctualizarse los mismos.

<h3 dir="auto"><strong>ARCHIVO: settings.csv</strong>:</h3>



Aqui se encuentran almacenados variables que se utilizan para realizar los analisis.
Estas pueden ser modificadas para realizar analisis perzonalizados:

ejemplo: Es posible modificar la cantidad de sesiones(barras) que se toman para calcular la media.


![image](https://user-images.githubusercontent.com/101218360/169631423-631b29ed-efd5-41d9-830c-e5cf8b2696ad.png)



Adicionalmente podemos encontrar el archivo grafico. Donde encontraremos funciones para imprimir textos con estilo.


![image](https://user-images.githubusercontent.com/101218360/169634044-361ccd6f-6ce9-413d-b6ab-b5c9bb0b6c8a.png)







Detalles de aplicación de módulos vistos en clase: 

Módulo 2; Variables: Se utilizaran variables de tipo (str, int y Float) 

Módulo 3: Condicionales: se utilizaran condicionales de tipo if para verificar la información ingresada y análisis de datos

Módulo 4: Bucles: for y while para el análisis de la información y recorrer las listas para encontrar valores deseados

Módulo 5: se definirán funciones para el análisis de la información. Estas se almacenaran en un archivo de interfaz que se importara

Módulo 6: Lectura de archivos CSV. Lectura para obtener la información de los distintos activos financieros. Se podrá sobrescribir el archivo de configuración para guardar las distintas configuraciones de los análisis.



Cualquier duda o consulta no duden en realizarla.

Francisco Soler
mail: fsolerpowell@gmail.com


