## SISTEMA TUTOR INTELIGENTE PARA LA CONSTRUCCIÓN DEL PENSAMIENTO COMPUTACIONAL EN LOS ESTUDIANTES DE EDUCACIÓN MEDIA GENERAL DE VENEZUELA

En la actualidad, las habilidades de resolución de problemas son cada vez más importantes, conocer métodos y herramientas computacionales que faciliten la construcción de las soluciones es vital en esta nueva era.

Esto ha causado el avenimiento de la ciencia y la tecnología de la información y comunicación, provocando el crecimiento de áreas que buscan nuevas formas de comprender, analizar y resolver problemas, la Inteligencia Artificial (IA), el Aprendizaje Automático (ML, del inglés, Machine Learning), entre otras. Son áreas que están en continuo avance.

En el ámbito educativo, se ha iniciado un proceso de masificación de nuevos recursos e ideas novedosas, algunos autores tales como Jeannette Wing principal promotora del Pensamiento Computacional (PC), expresa la necesidad del fortalecimiento de las habilidades y procesos implicados en la formulación de problemas y la representación de sus soluciones, de manera que dichas soluciones pueden ser efectivamente ejecutadas por un agente de procesamiento de información (humano, computadora o una combinación de ambas).

Ante la necesidad de encontrar medios de aprendizaje más eficientes, centrados en principios tales como Aprender Haciendo, Aprender Creando y Aprender Emprendiendo y en pro de reivindicar el aprendizaje de aquellas habilidades y destrezas del pensamiento superior que parecen escapar de nuestras instituciones educativas; tales como: la resolución de problemas, la generalización, el análisis, la sintesis, la descomposición de operaciones, la construcción de algoritmos, etc.  

Ha nacido la iniciativa de la creación de un nuevo producto teniendo como base la [Enciclopedia Multimedia](http://www.uptbal.edu.ve/repositorio/index.php?option=com_phocadownload&view=category&id=19:pnfi&Itemid=232), un nuevo sistema de mayor alcance y de una naturaleza innovadora, que incluya aspectos tan preponderantes como la enseñanza asistida por computadora mediante las practicas más avanzadas de la Inteligencia Artificial.

Un nuevo producto, que funja en el papel de aliado de los estudiantes venezolanos, un sistema que les conozca, que sepa sus habilidades, destrezas, y conocimientos, pero que también tenga  en cuenta sus deficiencias y los obstáculos  que este debe atravesar en la aventura del aprendizaje, y que de manera autónoma y personal le ofrezca la más rica accesoria y acompañamiento. 

## LICENCIA

Este proyecto está bajo la Licencia (¡Por definir!) - consulta el archivo [LICENSE.md](LICENSE.md) para encontrar más detalles.

## COMENZANDO 

Este documento busca ofrecer a los miembros del Equipo de desarrollo un bosquejo con las consideraciones iniciales que debe tener en cuenta para obtener una copia del proyecto en funcionamiento, orientada tanto para ordenadores personales como para servidores bajo los siguientes propósitos: desarrollo, pruebas y despliegue.
Que herramientas necesitas instalar para correr el proyecto, esto dependera de la finalidad:

*  Si estas interesado en descargar los repositorios del proyecto y colaborar en el proceso desarrollo de software, entonces debes utilizar la instalación y la
configuración orientada a las estaciones de trabajos personales, que buscan dotar a los participante de un **'ambiente de desarrollo integrado'** (que incluya, codificación, depuración, pruebas, etc.)  

* Si tu objetivo final, es desplegar una versión del proyecto en un servidor (fisico) para la realización de pruebas pilotos (ampliar), entonces debes utilizar los pasos de instalación y configuración orientados a la contrucción
de un **'ambiente de pruebas'**. 

* Aun nos encontramos definiendo los aspectos inherentes al **'ambiente de producción'**.

## INSTALACIÓN Y CONFIGURACIÓN 

### 1.  Ambiente de Desarrollo Integrado

### 1.1 Backend
	
### 1.1.1. Python 3.4 (o Superior)
	
### Linux o Mac OS X
	
Si estás usando alguna distribuccion de los sistemas operativos antes citados probablemente ya tienes instalada alguna versión de python o dos (Python 2.7 y Python 3). Escribe python o python3 en una terminal.Si ves algo así, Python está instalado:
```bash
Python 3.4.0 (default, Apr 11 2014, 13:05:18)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```	

### Windows

Ahora bien, si se encontrase bajo software privativo, igualmente existe varias alternativas para la instalación de python, se sugiere la descarga del instalador, para ello, es importante que tenga en cuenta la versión de su sistema operativo en caso de tener Windows XP SP1, y en adelante hasta Windows 7 SP1, puede instalar la versión 3.4 de python, en caso de tener una versión superior de Windows, entonces podrá instalar versiones posteriores de python, de todas formas puede ampliar la información en la documentación oficial de python ().
	
Con respecto al instalador, si se cuenta con la versión indicada para su sistema operativo es sumamente sencillo instalarlo, no olvide anotar donde instalado el python, más adelante puede utilizar tal información.
	
Posterior a su instalación es importante que se compruebe que python haya sido agregado a las "Variables de Entono", del sistema:
	
Para ello, dirijase, a Mi PC o Equipo y mediante el click derecho acceda a las "Propiedades" en su sección "Configuración".
	
Luego, ingrese a las variables de entorno, a la path y dentro de la cadena de texto debe existir una lineas semejante:

C:\Python34\;C:\Python34\Scripts;

En caso, contrario utilice la ruta de instalación de python que se habia destacado anteriormente y agregala al final del path separado por ";".

Finalmente, abra una shell (Simbolo del sistema) y teclee python. Si ves algo así, Python está instalado:

```bash
Python 3.4.0 (default, Apr 11 2014, 13:05:18)
[GCC 4.8.2] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

### 1.1.2 Django 2.0.9 (o Superior)

### 1.1.2.1 Linux o Mac OS X

```bash
tar xzvf Django-2.0.tar.gz
```	

```bash
cd Django-*
```

```bash
python setup.py install
```

### 1.1.2.2 Windows 

La instalación de django se puede realizar tambien mediante un instalador offline (sin conexión a Internet) comprimido (.tar), el cual puede ser descargado desde el sitio oficial (),
Posterior, a la descarga, ubique donde desea instalarlo (Ej. C:\ ) y luego descomprimalo.
Luego, acceda a una consola y abra el directorio que fue comprimido, para ello puede utilizar el comando cd, en el caso de acceder a la unidad C:\Django-2.0.9.  
Si se encontrase al abrir la consola en siguiente directorio: C:\Users\PC, retroceda mediante la instrucción:

```bash	
cd .. 
```

	Y atraves del comando 

```bash
dir
```
	
Puede listar los directorios y archivos, para visualizar y ubicar la carpeta descomprimida.
	
Intente listar los archivos mediante el comando dir y asegurese que se encuentre un archivo llamado setup.py que contiene un script de instalación 
	
Para correr el script, teclee el siguiente comado:

```bash
python setup.py install
```

Espere uno minutos, y finalizada la instalación, de manera similar compruebe que se haya agregado django a las variable de entorno (Ej. C:\Django-2.0.9\django\bin).
	
Finalmente, verifique que haya instalado de forma satifactoria, abra una consola y acceda al interprete de python y luego importe las utilidades de django mediante la instrucción:

```python
import django
```
No deberia emitir ningun mensaje de error, y para verificar que haya importado django solicite que le muestre la versión del mismo:

```python
django.get_version()
```

Antes de empezar, deberías asegurarte de que tienes instalados algunos paquetes y utilidades adicionales necesarias para el desarrollo:
(*) pytz, descargue y descomprima el instalador offline comprimido (.tar) en el directorio donde instalo django y acceda a la carpecta que decomprimio y tecle:

```bash
python setup.py install
```

(*) pillow

**1.2. Frontend**
	
**2. Ambiente de Pruebas (Orientado a Servidores)**

**3. Ambiente de Producción** 

## CORRIENDO EL PROYECTO

Despues de haber preparado tu ambiente de trabajo, te invitamos a clonar los repositorios del proyecto, mediante la linea de comando del git o tambien  puedes descargarlo via http desde el navegador.

Entonces acceda al directorio del proyecto
Ejemplo:
/projects/sti-aurora-digit
  apps  
  db.sqlite3 
  manage.py 
  media  
  README.md
  sti-aurora-digital
 
Teclee el siguiente comando:
```bash
$ python manage.py runserver
```
La instrucción anterior, deberá desplegar el proyecto (iniciando el servidor), django por defecto incluye un servidor web ligero. 

Para iniciar el servidor, entra en el directorio que contiene tu proyecto (cd nombredelproyecto) si aún no lo has hecho y ejecuta el comando.

El comando runserver inicia el servidor de desarrollo en el puerto 8000, escuchando sólo conexiones locales. Ahora que el servidor está corriendo, visita  a dirección http://127.0.0.1:8000/ con tu navegador Web. 

Te invitamos a consultar un material inductivo que hemos dejado al final de un post de ayuda almacenado en el Trello: Instroducción al Desarrollo Web en Django [Guía de Comandos].


## CONTRIBUYENDO

Nos encantaria recibir tus aportes, por ello hemos preparado un humilde material donde podras conocer algunas consideraciones que debes tener en cuenta para iniciar en tu proceso de colaboración y acompañamiento.

Consulte el archivo [CONTRIBUTING.md](https://) alli encontrará los detalles sobre la Estrategia de Ramificación e Integración Continua, y algunas consideraciones sobre el proceso para enviarnos tus valiosos aportes.

