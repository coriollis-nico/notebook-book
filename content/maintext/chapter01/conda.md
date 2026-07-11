# Instalación con conda

Aquí comienzan los tutoriales en esta guía. Vamos a aprender a instalar Jupyter
localmente y a escribir _notebooks_ usando Python.

La primera lección[^lesson] que quisiera compartir con quien lee estas notas es la siguiente:
:::{tip} Lección de programación
  No debemos instalar globalmente herramientas científicas.
:::
Es decir, *no debemos de hacer* cosas como
```shell
$ sudo dnf install python3 python3-matplotlib python3-numpy
```
y no debemos usar `pip`.
Supongamos que queremos usar una biblioteca de Python específica para analizar datos
astronómicos fotométricos con un formato particular. Cuando estos
datos fueron capturados, la versión más nueva de Python era `2.7`, y por lo tanto esta
herramienta está escrita en Python `2.7`, y no funciona con Python `3`.
No será fácil para mí reemplazar la instalación de Python `3.y` ya instalada en mi
sistema operativo, y si hiciera esta sustitución a la fuerza las otras aplicaciones en
mi sistema dejarían de funcionar. El mismo problema puede ocurrir a la inversa: puedo
requerir una función de Python añadida en la versión más nueva, pero tomará un tiempo
para que los responsables del mantenimiento de mi sistema operativo validen que todas
las aplicaciones importantes aún funcionan correctamente. Lo mismo aplica para las
bibliotecas de Python utilizadas, para otros lenguajes interpretados, compiladores, y
más. Esto también permite asegurarnos de que cambios en versiones nos impidan reproducir
resultados pasados.

[^lesson]: Estas lecciones estarán compiladas (ja ja) en el [apéndice](hygene).

Clarifico que las herramientas usadas para *escribir* código no necesitan seguir
esta regla. Yo uso Visual Studio Code para escribir código y algunos complementos para
revisar y formatear mi código de Python y $\LaTeX$. En cambio, aquello que va a leer este
código para generar resultados sí debe obedecer esta regla.

Si no hemos de instalar herramientas globalmente, ¿qué hacemos?
:::{tip} Lección de programación
  Crear ambientes reproducibles para cada proyecto.
:::
Instalamos el _software_ que necesitamos para un proyecto en un *ambiente*, un rincón
especial de nuestra computadora, sin interactuar con el resto del sistema, y al iniciar
otro proyecto creamos *otro* ambiente independiente del primero. Cambios en un
proyecto no generarán problemas en otro.

## Instalar conda-forge

Conda[^con] es un *gestor de paquetes*; se encarga de descargar, instalar y actualizar
_software_, y se asegura que tengas las dependencias necesarias.
El proveedor de _software_ por defecto al usar conda es Anaconda[^Ana]
pero para trabajo científico será mejor usar el canal conda-forge[^forge].
El canal conda-forge distribuye más _software_, más reciente,
es liderado por su comunidad y sus licencias son más permisivas.

Sigue las instrucciones en el [sitio](https://conda-forge.org/download/)
para instalar la versión de Miniforge apropiada
para tu sistema. Asegúrate de seleccionar la versión adecuada para la arquitectura de
tu procesador. Para computadoras personales, tu arquitectura es casi seguramente
`x86_64 (amd64)`.

Descarga el instalador, bre el directorio (i.e. la carpeta) donde se encuentra la descarga
y ejecutala con `bash`:

```shell
$ bash Miniforge3-Linux-x86-64.sh
```

Aparecerá un breve acuerdo de licencia. Leelo y acéptalo (las condiciones son
sencillas y permisivas; nada de qué preocuparse).

El instalador te pedirá elegir dónde instalar.
El directorio por defecto (tu carpeta `home`) es un buen lugar;
realmente nunca tendrás que abrirla manualmente.

Al terminar encontrarás la siguiente notificación (aquí traducida):

```code {shell}
¿Deseas actualizar tu perfil de shell para inicializar conda automáticamente?
Esto activará conda al iniciar sesión y cambiará el prompt de comandos cuando esté activado.
Si prefieres que el entorno base de conda no se active al inicio,
ejecuta el siguiente comando cuando conda esté activado:

conda config --set auto_activate_base false

Nota: Puedes deshacer esto más tarde ejecutando conda init --reverse $SHELL
¿Proceder con la inicialización? [yes|no]
```

Debes escribir `yes`.

Abre otra terminal y verás que la cadena `(base)` precede a la linea del terminal:

```shell
(base) nch@localhost-live:~$
```

Esto indica, como advertía la notificación anterior, que por default tus terminales
usarán un ambiente de conda. No queremos esto, queremos que nuestros ambientes de conda
estén separados. En este nuevo terminal ejecuta la linea indicada por la notificación:

```shell
$ conda config --set auto_activate_base false
```

Las terminales que abras a partir de ahora no dirán `(base)`.
Sin embargo, ejecuta el comando

```shell
$ conda --version
```

y confirma que conda está instalado en tu sistema.

## Creación de ambientes en conda

En conda se distribuyen principalmente (pero no exclusivamente) versiones de Python
y de bibliotecas de Python que normalmente se descargarían, por ejemplo, usando
`pip`.
Crearemos un ambiente de conda donde instalaremos el _software_ que usaremos a lo largo
de esta guía:

```shell
$ conda create -n notebooks
$ conda activate notebooks
```

El prefijo `(notebooks)` aparecerá, indicando que estás dentro de tu ambiente
de conda llamado `notebooks`.
Ahora instalemos el _software_ básico que usaremos (por ahora):

```shell
(notebook) nch@localhost-live:~$ conda install python=3.14 numpy=2.5 matplotlib=3.11 jupyterlab=4.6 jupyterlab-language-pack-es-es
```

El _software_ se instalará. Comprobemos las versiones de Python y JupyterLab instaladas:
```shell
(notebook) nch@localhost-live:~$ python --version
Python 3.14.6
(notebook) nch@localhost-live:~$ jupyter-lab --version
4.6.1
```
Podría ser que no coincida con la instalada en nuestro sistema de manera global
(fuera de nuestro ambiente `notebook`).
Podemos trabajar con este _software_ sin que interfiera con el resto de nuestro sistema.

Recuerda que este ambiente solo está activo en este terminal. Al cerrarlo o al
abrir otro deberás volver a ejecutar `conda activate notebooks`
para volver a acceder.

Crea una carpeta en la que harás tu trabajo y abrela en tu terminal.
Al ejecutar

```shell
(notebook) nch@localhost-live:~$ conda export --format txt > environment.txt
```

se creará un archivo `environment.txt` con los paquetes y dependencias instaladas en
tu ambiente. Podria ser un archivo bastante grande; muchos de los elementos de esta lista
podrían no ser familiares para ti. Sin embargo, al incluirlos a todos en la lista,
te aseguras que tu ambiente sea *completamente* reproducible[^deps].

Este no es un tutorial de conda, y lo que he expuesto aquí solo toca la superficie,
pero es suficiente para que podamos seguir. Hemos instalado Python, las principales
bibliotecas numéricas y de visualización, y Jupyter Lab. Tenemos todo el software necesario
para comenzar a escribir cuadernos.
Cuando necesites aprender más sobre conda, revisa la documentación de conda y
conda-forge.

[^con]: https://conda.org/
[^Ana]: https://www.anaconda.com/
[^forge]: https://conda-forge.org/
[^deps]: Puedes generar un archivo más pequeño añadiendo la opción
  `--from-history`.
