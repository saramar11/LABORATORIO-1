*Autoras: Mariana Garcia & Sara Pinzón*

# LABORATORIO-1

El presente código es el informe respectivo al laboratorio 1 para la asignatura de Procesamiento Digital de Señales de sexto semestre de la Universidad Militar Nueva Granada. En este documento se estará describiendo el paso a paso de la ejecución que se tuvo en cuenta para la realización de cada punto solicitado para este laboratorio


## Librerías
Teniendo en cuenta lo anterior, se inició con la descarga y la implementación de las diferentes librerías que se utilizaron entre las cuales se encuentran: “*wfdb*"  la cual es utiliza para el manejo y almacenamiento de las señales biomédicas las cuales manejan este tipo de formato o por el contrario tomar una señal y reescribirla en este formato, la librería “numpy” la cual es usada para operaciones matemáticas, “*math*” esta brinda funciones matemáticas más avanzadas, finalmente “*scipy.stats*”  de la cual se usa “*variation*” diseñada para analisis y operaciones estadisticas.

##  Obtención de la señal fisiológica 
Mediante la base de datos Physionet.org se obtuvo una señal fisiológica, en este caso correspondiente al ECG filtrada de un paciente voluntario (de acuerdo con la descripción dada por la base de datos).  A partir de esta base, se descargaron los archivos con extensiones .hea y .dat y fueron guardados en la misma carpeta donde está el proyecto .py. En el caso de que no se encuentren dentro de la misma carpeta, no se reconocerá el archivo de datos fisiológicos que se quiere usar dentro del código.
Con esto dicho, se utilizó la librería wfdb con el archivo .rdrecord para guardar esta señal del archivo en una variable a la cual en este código se llamó  **'senal’**.

[![24.png](https://i.postimg.cc/HssV3LMY/24.png)](https://postimg.cc/142m3sM2)

De esta forma logro obtener una única señal para poder utilizarla a lo largo del código para así cumplir con los criterios que son solicitados dentro de este laboratorio.
Para visualizar la carpeta de donde se obtuvo la señal ECG del paciente haga click  [aquí]( https://physionet.org/content/ecgiddb/1.0.0/Person_01/#files-panel).

Grafica del ECG del paciente:

[![senal.png](https://i.postimg.cc/B6wC1f04/senal.png)](https://postimg.cc/sQ7Wt8xN)


##Punto 1: Estadísticos 
Para esta primera parte del código se procede con el análisis estadístico de la señal descargada, en donde se calculan datos como la media, desviación estándar, coeficiente de variación. Estos cálculos fueron realizados de dos formas distintas, una de ellas utiliza funciones de las librerías matemáticas de  Python mencionadas anteriormente las cuales facilitan los cálculos, así mismo se realizaron de forma manual con el fin de aprender a realizar este tipo de cálculos de ambas formas, seguido a esto se realiza el histograma y su función de probabilidad, para tener una idea más clara de los datos que se están trabajando, ya que en este tipo de archivos .dat y .hea suelen tener más de un grupo de datos.
Con lo anterior se procede con los cálculos estadísticos.

### a) Media:
Esta corresponde al promedio de los datos que se desean analizar, esto haciendo uso de su fórmula:

[![media3.png](https://i.postimg.cc/j2YkK9zc/media3.png)](https://postimg.cc/xJgP36pN)

La segunda forma de realizar esta ecuación fue de manera manual en donde se crean las variables. Primero la variable “suma” se inicializa en 0 ya que esta acumulara los datos del contador dentro del ciclo ** “ for”** de la señal que está en la variable **valores**, este se utiliza para que recorra los valores de la señal con el contador *“i”* por cada instante de tiempo. Visto de una forma más clara, **suma** representa a la sumatoria de los *“x_i”* de la ecuación anterior, es importante que este inicializada al inicia el ciclo. Después, se crea una nueva variable la cual es llamada **“datos”** y es igualada a la función **“len(valores)”**, esta variable es la  encargada de decir la cantidad exacta de valores presentes dentro de la formula anteriormente mostrada representa a      “n ” . Después de estos pasos se procede a iniciar con el “for” en donde se tendrá:

### Con función
Primero esta ecuación se realizó utilizando un parámetro de * Numpy * **“np.mean(valores)”** el cual es capaz de realizar la media de los datos que se desean, en este caso los datos utilizan el nombre de la variable **“valores”** que fue dado al llamar a los archivos que contiene los datos al inicio del programa, finalmente se utiliza la función **“print”** para mostrar el resultado de la media en la consola.

[![meana.png](https://i.postimg.cc/NMCfz6mQ/meana.png)](https://postimg.cc/WFrvDJ5y)

### Forma larga

La segunda forma de realizar esta ecuación fue de manera manual en donde se crean las variables. Primero la variable “suma” se inicializa en 0 ya que esta acumulara los datos del contador dentro del ciclo ** “ for”** de la señal que está en la variable **valores**, este se utiliza para que recorra los valores de la señal con el contador *“i”* por cada instante de tiempo. Visto de una forma más clara, **suma** representa a la sumatoria de los *“x_i”* de la ecuación anterior, es importante que este inicializada al inicia el ciclo. Después, se crea una nueva variable la cual es llamada **“datos”** y es igualada a la función **“len(valores)”**, esta variable es la  encargada de decir la cantidad exacta de valores presentes dentro de la formula anteriormente mostrada representa a      “n ” . Después de estos pasos se procede a iniciar con el **“for”** en donde se tendrá:

[![formean.png](https://i.postimg.cc/sg0M8Rrk/formean.png)](https://postimg.cc/LJL4YwhD)

Al salir del** for** se realiza la operación en donde se divide la suma de todos los valores entre la cantidad de valores totales **n**:

[![mean2.png](https://i.postimg.cc/nc3rjtCX/mean2.png)](https://postimg.cc/xcbnhhGQ)

Finalmente se muestra el resultado utilizando:

[![print1.png](https://i.postimg.cc/SNPqbQnf/print1.png)](https://postimg.cc/0b7hpsdz)

### b) Desviación estandar
Al obtener el valor de la media de los datos se prosigue con la desviación estándar:

[![dv.png](https://i.postimg.cc/1X4Tv6rh/dv.png)](https://postimg.cc/sGdwXMLw)

La desviación estándar que corresponde al cálculo mediante la función de numpy **“np.std(valores)”** encargado de dar como resultado la dispersión de los datos correspondientes a la señal del ECG escogida, para luego mostrar el resultado en consola con el **“print”**

####  Forma larga
Para la desviación estándar de forma manual, nuevamente se requieren las variables **“suma_dat” ** inicializada en cero y **“n = len(valores)”** cumpliendo la misma función que se mostró para la media. Así mismo, se utiliza el ** “for” **para recorrer todos los datos usando el contador e, se llama la variable suma para realizar la operación:

[![dvs.png](https://i.postimg.cc/gJwcZwLj/dvs.png)](https://postimg.cc/xJ2Sr1RV)

Esta representa la sumatoria de todos los valores recorridos por el contador **“e”** que de forma individual le restara la media y elevara ese resultado al cuadrado, al salir de for se realiza la operación que corresponde a la varianza la sumatoria realizada en** “suma_dat” **sobre la cantidad total de datos **“n ” **

[![var.png](https://i.postimg.cc/QxqDVgYS/var.png)](https://postimg.cc/kBDzpSmt)

Para finalizar la operación se obtiene la raíz cuadrada de la varianza mediante la función de la librería *math* y luego mostrar este resultado con la funcion **print”**:

[![dvs0.png](https://i.postimg.cc/y8WGB0MD/dvs0.png)](https://postimg.cc/0zRn0K2v)

### c) Coeficiente de variación

[![cv.png](https://i.postimg.cc/FHfTwNSc/cv.png)](https://postimg.cc/SnhLM0DN)

#### Con función
El primer cálculo de coeficiente de variación se realizó con el parámetro de *Scipy.stats*:
Para obtener el coeficiente de variación se usa: 

[![cv1.png](https://i.postimg.cc/D08GmynP/cv1.png)](https://postimg.cc/JHC028ys)

Para solo ver los valores positivos se le aplica la función de valor absoluto * “abs”*:

[![cv2.png](https://i.postimg.cc/jjcnXJjh/cv2.png)](https://postimg.cc/jWWjq2PW)

Multiplicar ese valor por 100 para obtener el resultado en porcentaje y mostrar el resultado final en consola: 

[![cv3.png](https://i.postimg.cc/KjkKxqD9/cv3.png)](https://postimg.cc/2LYjxxJv)

#### Forma larga
 De forma manual se toma el valor absoluto de la división de la desviación estándar entre la media de los datos y se multiplica el resultado por 100 igual que en la forma anterior para tener el resultado en porcentaje y con la función **”print”** se muestra el resultado en la consola:

[![cv4.png](https://i.postimg.cc/Kv1svRx4/cv4.png)](https://postimg.cc/HVCt6WJC)

### d) Histograma
Se realiza un histograma con el fin de representar de una forma gráfica la distribución de los datos visualizando la frecuencia que estos presentan.
#### Usando *matplotlib*:
Se plantea la fórmula de sturges la cual estima el número de clases necesarias para un histograma. Agrega 1 al logaritmo de base 2 del número de elementos en la lista y se redondean los decimales a números enteros para tener un número exacto de clases del histograma.

[![hist.png](https://i.postimg.cc/VLPD14GZ/hist.png)](https://postimg.cc/Lhvz3kMj)

Se muestra en consola la cantidad de clase o barras que va a tener el histograma y con la ayuda de la librería se muestra la gráfica en la consola teniendo en cuenta varias variables necesarias tales como las que se especifican en el código. Además, usando la misma librería *"matplotlib”* se nombró al histograma y ejes:

[![hist3.png](https://i.postimg.cc/XqsJ2spN/hist3.png)](https://postimg.cc/m1FBkNYK)

Resultado final:

[![histo.png](https://i.postimg.cc/qvPVyWpc/histo.png)](https://postimg.cc/0z0BqWMr)

### e) Función de probabilidad
La función de probabilidad proporciona una representación visual de cómo se distribuyen los datos. Para el calcular el centro de los bins (intervalos) se suman las dos esquinas de cada rectángulo o clase y se dividen en dos (promedio de la clase):

[![fprob.png](https://i.postimg.cc/VLcQTqjm/fprob.png)](https://postimg.cc/8sw0frK0)

Resultado final:

[![funciondeprob.png](https://i.postimg.cc/pTvw18hp/funciondeprob.png)](https://postimg.cc/LqyQJJVp)

## Punto 2: SNR
Para esto, se define al SNR (relación señal-ruido) como una medida la cual permite calcular y determinar en una señal si hay más ruido que información de la señal o viceversa, mediante la siguiente formula. 

[![snr1.png](https://i.postimg.cc/sxr6nJbL/snr1.png)](https://postimg.cc/FdTVz0rb)

Y para calcular la potencia de cada señal, se realizaba mediante:

[![snr2.png](https://i.postimg.cc/bY93yk7z/snr2.png)](https://postimg.cc/JttbKD7g)

*Donde:
P = Potencia 
n = es la longitud de la señal adquirida (la longitud del ruido debe ser igual a la de la señal original).*

A partir del resultado de SNR obtenido se determina que, si es un valor positivo, hay más información de la señal que ruido. Mientras que, si es un valor negativo, indica que hay mas ruido en la señal contaminada que información importante.

[![snr3.png](https://i.postimg.cc/BbmTxc3H/snr3.png)](https://postimg.cc/7JTJ4zfZ)

Con esto, para el laboratorio se contamino a la señal ECG con tres tipos de ruidos diferentes y a los ruidos se le variaron la amplitud para así obtener los dos tipos de resultados posibles para el SNR.

### Cálculo de la potencia de la señal original

Antes de comenzar con el código que se utilizó para contaminar la señal, es importante recalcar que debido a que la señal para contaminar con los tres tipos de ruido va a ser la misma que se escogió desde un principio, la potencia de señal será igual en los tres casos. Por lo tanto, se crea una variable llamada  **"sumad"** la cual es la que contendrá la suma de todos los datos dentro del arreglo de la señal, y así cumplir con lo estipulado en su ecuación.

[![senalori.png](https://i.postimg.cc/CLtDSKxh/senalori.png)](https://postimg.cc/9rdzBC9K)

Para realizar la sumatoria de estos datos, se utiliza un ciclo for con un contador en este caso llamado **"d"** que recorra todos los valores, los eleve al cuadrado y realice su sumatoria total, a este resultado final se divide por la cantidad de datos **"n"** y de esta forma se cumple con la ecuación planteada anteriormente para la potencia de la señal.

[![senalori2.png](https://i.postimg.cc/KY7gPrrj/senalori2.png)](https://postimg.cc/7C66DzRr)

### a) Ruido Gaussiano.

#### SNR positivo
 Para contaminar la señal del ECG con ruido gaussiano primero es necesario generar la señal del ruido gaussiano teniendo en cuenta que debe tener la misma cantidad de datos que tiene la variable **"valores"** que como se había mencionado anteriormente es la variable que contiene a la señal original del ECG. Para esto se utilizó otra variable llamada **"tamano"**.

[![gauss1.png](https://i.postimg.cc/VNzN8yns/gauss1.png)](https://postimg.cc/gxBpVTg1)

Teniendo en cuenta que es un ruido gaussiano se tomara el valor de desviación estándar como 1, se guarda este valor en la variable **sigma**. A partir de esto se utiliza una función de la librería *numpy* para poder generar un vector con números aleatorios con una distribución normal (datos que tengan una mayor probabilidad de agruparse a valores cercanos a la media) que tengan una media de 0, deviación estándar de 1 y que el tamaño sea igual al de la señal original. Además, a este inicialmente se le multiplico por una amplitud de 0.01 para obtener el primero tipo de respuesta que se espera para el SNR. Este arreglo se guardó en la variable **"ruido_G_a"**.

[![gauss2.png](https://i.postimg.cc/FR8dmWhP/gauss2.png)](https://postimg.cc/mz32ySzM)

Una vez teniendo el primer ruido generado se calcula su potencia siguiendo la misma lógica que se postulaba anteriormente para el ruido original, solo que esta vez se reemplaza con el vector recién creado para el primer ruido Gaussiano que se generó. Su resultado se guardó en la variable **“potencia_ruido1”**.

[![gauss31.png](https://i.postimg.cc/GtfZXDJT/gauss31.png)](https://postimg.cc/BPxY6XzJ)

Ya obteniendo los valores para cada potencia, en una línea de código en la cual se realizó la ecuación postulada anteriormente para obtener el valor del SNR.

[![gauss4.png](https://i.postimg.cc/nVdjHLhs/gauss4.png)](https://postimg.cc/w3mT2gJH)

Para realizar la contaminación de la señal del ECG se realiza una superposición de las dos señales:

[![gauss5.png](https://i.postimg.cc/R0Qh2SYZ/gauss5.png)](https://postimg.cc/kVG7bm90)

Teniendo en cuenta que la amplitud colocada para esta señal fue menor al de la amplitud de la señal original, el resultado obtenido fue un SNR positivo indicando que después de la contaminación, la señal tuviera más información que ruido en ella.
Para visualizar las gráficas de las tres señales generadas (ECG original, ruido, señal original contaminada) se utiliza la librería *”matplotlib”* y su función *“subplot”* para tener la comparación de las tres señales en una sola hoja generada en la consola. 

[![gauss6.png](https://i.postimg.cc/MT368vmq/gauss6.png)](https://postimg.cc/ftXncWPr)

Resultado final:

[![graf1.png](https://i.postimg.cc/130y3WrW/graf1.png)](https://postimg.cc/NK03NkVT)


#### SNR negativo
Para la obtención de un SNR negativo con este mismo tipo de ruido, se realizan los mismos pasos con la única diferencia en que se cambia el valor de la amplitud por un valor mayor al de la amplitud de la señal original, en este caso se utilizó un valor de 100.

[![gauss7.png](https://i.postimg.cc/fbBZxJFm/gauss7.png)](https://postimg.cc/McMhwKzp)

Resultado final:

[![graf2.png](https://i.postimg.cc/ZRQSMXJq/graf2.png)](https://postimg.cc/HcbRJZcG)

### b) Ruido de tipo impulso

#### SNR positivo

Para este tipo de ruido se tiene en cuenta una probabilidad estipulada en el código la cual describe que tan probable es que se genere un impulso con una determinada amplitud en la muestra de números aleatorios que conforman el vector del ruido.

Con esto, se decidió una probabilidad del 5% para que alcanzara a ser visible en las gráficas. Para generar este ruido se deben tener en cuenta dos parámetros, la probabilidad con el conjunto de valores posibles y la amplitud de los impulsos, generadas a partir de una distribución normal de la cual se hablaba anteriormente con el ruido Gaussiano, a esta variable se le multiplico por 0.01 para obtener el valor positivo de SNR para esta señal contaminada. Para obtener el ruido de tipo impulso se multiplican estos dos parámetros. Una vez con la señal de ruido realizada, se procedió a realizar los mismos pasos ya estipulados para calcular el SNR de la señal contaminada.

[![impulso1.png](https://i.postimg.cc/zfbZR0CZ/impulso1.png)](https://postimg.cc/kVmh0NYf)

Resultado final:

[![graf3.png](https://i.postimg.cc/vmFTTgnz/graf3.png)](https://postimg.cc/xX5nFdtJ)

#### SNR negativo
De igual forma, así como se multiplico a la variable de amplitud inicialmente por 0.01 para obtener un valor de SNR positivo (más información que ruido en la señal contaminada). Y por 100 para obtener un SNR negativo (más ruido que información en la señal ECG contaminada).

[![impulso3.png](https://i.postimg.cc/9X7WRFWg/impulso3.png)](https://postimg.cc/3W3Mzh02)

Para comparar estos dos resultados se mantuvo la misma probabilidad de 5% para este tipo de ruido por impulso. Desde esta parte en adelante se realizaron los mismos pasos postulados en el ruido gaussiano donde se calculó la potencia para la señal de ruido, se obtuvo el valor respecto del SNR y se graficaron los resultados para compararlos en torno a la gráfica con el ECG original, el ruido tipo impulso y finalmente la gráfica con la señal contaminada, tanto para SNR positivo como para SNR negativo. Estas instrucciones se encuentran entre las líneas de código 290 hasta la 421.

Resultado final:

[![graf4.png](https://i.postimg.cc/pdLWpfTK/graf4.png)](https://postimg.cc/XrtSPy9v)

### c) Ruido tipo artefacto

Para realizar este ruido se introdujeron picos o eventos aleatorios a la señal original con el fin de crear la distorsión deseada, para generar este ruido se tienen en cuenta diferentes datos tales como la frecuencia de muestreo, junto con la duración de la señal representa al intervalo de tiempo que se tomara en cuenta para contaminar la señal, con esto en cuenta se inicia el código para el ruido:

Se define la frecuencia de muestro en 100, duración en segundos:

[![artefacto1.png](https://i.postimg.cc/Wz6CGyYz/artefacto1.png)](https://postimg.cc/9w0LVLhH)

Se define el tiempo (t) de muestreo mediante:

[![artefacto2.png](https://i.postimg.cc/5thRZJZj/artefacto2.png)](https://postimg.cc/jWhc7pqr)

La frecuencia de muestro en Hz y la cantidad de picos de ruido aplicados:

[![artefacto3.png](https://i.postimg.cc/Jzg6km7K/artefacto3.png)](https://postimg.cc/rD1CBBrt)

#### SNR positivo

Para la primera parte que se desea evaluar la cual correspondía a un SNR positivo al igual que los ruidos anteriores, para esto la potencia de la señal debía ser mayor a la del ruido, con esto en mente se modificaron los valores de la amplitud de la señal del ruido de la forma:

[![artefacto4.png](https://i.postimg.cc/DZQBHXrY/artefacto4.png)](https://postimg.cc/qhRsCgZ8)

Seguido a esto se procede a generar los impulsos de ruido aleatoriamente para después graficarlos y se genera el ruido con todo lo anterior dentro de un vector:

[![artefacto5.png](https://i.postimg.cc/4366xTYY/artefacto5.png)](https://postimg.cc/5HtYsTqJ)

Se contamina la señal con el ruido tipo artefacto realizado:

[![artefacto6.png](https://i.postimg.cc/ZRqWzkpt/artefacto6.png)](https://postimg.cc/KKdGtH0J)

Resultado final:

[![graf5.png](https://i.postimg.cc/T2JdG2fz/graf5.png)](https://postimg.cc/c66yBSKh)

#### SNR Negativo
Seguido a esto se grafica al igual que en los puntos anteriores, finalmente esta misma acción de repite para SNR negativo diferencia de la amplitud de la señal de ruido la cual queda como:

[![artefacto8.png](https://i.postimg.cc/Hx4gp3Dw/artefacto8.png)](https://postimg.cc/PpxcyWqJ)

Finalmente, con este cambio ya se obtiene el SNR deseado en donde se muestra de forma más pronunciada la potencia del ruido que la potencia de la señal.

Resultado final:

[![graf6.png](https://i.postimg.cc/KjGy4Lxd/graf6.png)](https://postimg.cc/jwF1FDWX)

## Bibliografía
Clínica Universidad de Navarra (2023) Qué es señal-ruido. Diccionario Médico. Available at: https://www.cun.es/diccionario-medico/terminos/senal-ruido#:~:text=De%20manera%20general%2C%20la%20relaci%C3%B3n,de%20fondo%20(informaci%C3%B3n%20irrelevante). (Accessed: 06 August 2024). 

Ortega, C. (2023, 14 septiembre). ¿Qué es la media, la mediana y la moda? QuestionPro. https://www.questionpro.com/blog/es/la-media-la-mediana-y-la-moda/ 

Calcular la desviación estándar paso a paso (artículo) | Khan Academy. (n.d.). https://es.khanacademy.org/math/probability/data-distributions-a1/summarizing-spread-distributions/a/calculating-standard-deviation-step-by-step 
Sanjuán, F. J. M. (2024, February 22). Coeficiente de variación- Descubre qué es, sus usos y algunos ejemplos. Economipedia. https://economipedia.com/definiciones/coeficiente-de-variacion.html 
Histograma. (n.d.). Introducción a La Estadística | JMP. https://www.jmp.com/es_co/statistics-knowledge-portal/exploratory-data-analysis/histogram.html 
 funciones de probabilidad y distribución. (2024). Www.uv.es. https://www.uv.es/webgid/Descriptiva/3_funciones_de_probabilidad_y_distribucin.html 
 Isaacbaltanas. (2021, May 15). Artefacto - Isaac Baltanás. Isaac Baltanás. https://crearunpodcast.com/glosario/artefacto


