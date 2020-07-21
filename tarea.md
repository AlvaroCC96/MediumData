# Tarea Medium Data
## Autores

Alvaro Castillo

Patricio Araya

---

Link Del Proyecto:

https://github.com/AlvaroCC96/MediumData

---

### Item 1

**Utilize técnicas de compresión para cargar el archivo *books_data.csv* en memoria.**

 - a. ¿Cuántos MB ocupan los datos cargados en memoria luego de comprimirlos?
 - b. Explique las técnicas de compresión utilizadas
  
  Primeramente se tuvieron que preparar los datos para poder cargarlos dado que el csv no está ordenado correctamente y secciones de él presentan mas columnas que otras o en distinto orden. Para resolver esto se seccionó el .csv en distintas partes usando los comandos que se encuntran en **splitter.sh**. 
  
  El principal factor que contribuye al espacio utilizado al cargar el .cvs son las columnas utilizadas. De esta manera la mejor forma de ahorrar espacio al trabajar con los datos es solo cargar las columnas necesarias para trabajar , ver clase **Compressor.py**. 

  Otro posibilidad para reducir el uso de memoria al cargar los datos es utlizar tipos de datos, lo que permite reducir considerablemente el peso especialmente de las columnas de tipo númericas . En el script **type-compression.py** se demuestra este enfoque en donde se utilizó una muestra de 12 columnas del .csv y fueron cargadas sin y con tipos de datos de la libreria numpy. Se logró de esta manera una compresión de alrededor del 10%.

  |Sin compresión|Con compresión| % |
  |-|-|-|
  |226 MB|203 MB| 10%

### Item 2

**Desarrolle un script en python que genere un archivo con los datos de los libros que tengan un rating mayor o igual a 4,5. Dicho script debe tener bajo consumo de memoria (máximo 10 MB cargados a la vez).**

Una primera aproximación a resolver el ejercicio fue cargar los datos usando solo un subconjunto mínimo de columnas y cargandolos dentro de una BD y por medio de una query generar el archivo con las filas filtradas. Al reducir el número de columnas se logró obtener un tamaño en memoria menor al límite de 10 MB. Ver script **FileWritter.py**

También se probó utilizar un enfoque mas tradicional cargando el archivo .csv en *chunks* utilizando la librería **pandas** para realizar la operación de filtrado en cada bloque y luego continuar con el siguiente para no sobrepasar el limite de 10MB simultáneos en memoria. 
Para dividir un archivo de alrededor de 235MB se utilizaron 23 bloques de alrededor de 9MB y 1 de 5MB y un tiempo de 4.35 segundos. Este script se encuentra en el archivo **ratings-by-chunks.py**. Para este se método se utilizó una versión limpiada del csv original y una cantidad reducida pero representativa de las columnas originales (Más detalles en el script).

### Item 3

**Se conoce que en un futuro se estarán realizando constantemente consultas a los datos y conviene tener agrupados los libros según su año de publicación, ¿qué estrategia propone con este fin?**

- a. Halle el promedio de los ratings para los libros del año 2002 utilizando la estructura original y luego la propuesta por usted. ¿Qué conclusiones puede sacar de los resultados?
  
Dado que se conoce que se realizaran frecuentemente consultas por una columna en específico convendria guardar los datos en una base de datos e indexarlos por año de publicación.

Propuesta De Equipo : 
Se llevaron los datos a una db relacional **sqlite** y se indexaron en base al año de publicación, esta aproximación se encuentra en el script *FileAverage.py*.

También se realizó un script que se puede encontrar en **avg-rating-by-year.py** el cual realiza la misma tarea utilizando la estructura original. Se utilizó la libreria **pandas** y sus herramientas para trabajar con csv y dataframes.

Los resultados obtenidos con cada método fueron:
|Método|Promedio| Tiempo (s)|
|-|-|-|
|Indexación SQL|3.469|0.064|
|Pandas data frame|3.469|0.140|

Se comprueba que el método de indexado de SQL arroja mejores resultados en tiempo que el método de utilizar la estructura de datos original. Sin embargo se debe pagar el coste de realizar una unica vez el traspaso de datos a la bd y el indexado. Mientras el otro método logra un tiempo constante cada vez que es ejecutado.

En el contexto del enunciado el método propuesto resulta más eficiente (Dado que seria una consulta recurrente). Sin embargo es importante considerar (como en este caso) el caso de uso concreto para escoger las mejores herramientas para obtener los mejores resultados.
