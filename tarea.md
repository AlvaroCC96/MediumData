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
  
  Primeramente se tuvieron que preparar los datos para poder cargarlos dado que el csv no está ordenado correctamente y secciones de el presentan mas columnas que otras o en distinto orden. Para resolver esto se seccionó el .csv en distintas partes usando los comandos que se encuntran en *splitter.sh*. 
  
  El principal factor que contribuye al espacio utilizado al cargar el .cvs son las columnas utilizadas. De esta manera la mejor forma de ahorrar espacio al trabajar con los datos es solo cargar las columnas necesarias para trabajar , ver clase *Compressor.py*. 

  Otro posibilidad para reducir el uso de memoria al cargar los datos es utlizar tipos de datos, lo que permite reducir considerablemente el peso especialmente de las columnas de tipo númericas . En el script type-compression.py se demuestra este enfoque en donde se utilizó una muestra de 12 columnas del .csv y fueron cargadas sin y con tipos de datos de la libreria numpy. Se logró de esta manera una compresión de alrededor del 10%.

  |Sin compresión|Con compresión| % |
  |-|-|-|
  |226 MB|203 MB| 10%

### Item 2

**Desarrolle un script en python que genere un archivo con los datos de los libros que tengan un rating mayor o igual a 4,5. Dicho script debe tener bajo consumo de memoria (máximo 10 MB cargados a la vez).**

Ver clase *FileWritter.py*

### Item 3

**Se conoce que en un futuro se estarán realizando constantemente consultas a los datos y conviene tener agrupados los libros según su año de publicación, ¿qué estrategia propone con este fin?**

- a. Halle el promedio de los ratings para los libros del año 2002 utilizando la estructura original y luego la propuesta por usted. ¿Qué conclusiones puede sacar de los resultados?
  

Propuesta De Equipo : *FileAverage.py* 

El uso de las herramientas de medium/big data, permite agilizar tiempos de respuesta , reducir el uso de recursos especialmente de memoria , esto al limpiar los archivos permite filtar los datos que son escenciales para la resolución del problema


