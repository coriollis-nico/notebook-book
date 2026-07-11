# Un primer vistazo a Jupyter

Vamos a explorar brevemente cómo escribir y ejecutar cuadernos de Jupyter (`.ipynb`).
Primero hablaremos de los mecanismos para abrir y ejecutar cuadernos y luego hablaremos
de los cuadernos en sí.


## Interfaces para _notebooks_

### Jupyter Lab

Jupyter Lab es actualmente la herramienta desarrollada por el proyecto Jupyter
para interactuar con _notebooks_ localmente.
Jupyer Lab (igual que Jupyter Notebook, la herramienta ligeramente más vieja) funciona
abriéndose en un navegador de internet.

Para abrir Jupyter Lab, en la terminal (en tu ambiente de conda) ejecuta:

```{code} shell
(notebooks) nch@fedora:~/Escritorio/physnotebooks$ jupyter lab
```

:::{figure} ./01_images/01_firstlook.png
:label: fig:jhub

Interfaz de JupyterLab.
:::

Siéntete libre de
explorar la interfaz; el proyecto Jupyter ofrece muchas funciones en sus proyectos, y no
podemos cubrir todo aquí. Te recomiendo que en la pestaña `Settings` (o `Configuración`) selecciones
el idioma de tu preferencia (descargamos el paquete de español en la sección anterior)
y configures el aspecto visual como te sea cómodo.

En la pestaña izquierda podemos explorar los archivos en el directorio en que abrimos
Jupyter Lab. No es posible salir del directorio donde se activó
(en este caso, `~/Escritorio/physnotebooks`)
por lo que procura abrir Jupyter Lab en el lugar correcto.

En el centro hay atajos para crear cuadernos, abrir Python en una terminal,
abrir la terminal del sistema, o crear otros tipos de archivos. También podemos
abrir o crear archivos en la pestaña `Archivos`.


### Visual Studio Code

VSCode es un editor y ambiente de desarrollo muy popular. Microsoft ofrece una extensión
_first-party_ que permite crear y editar _notebooks_ directamente en VSCode. Esta es la
forma de trabajar que prefiero yo, porque estoy acostumbrado a las funciones de revisión
y autocompletado. Si ya estás familiarizadx con VS Code, esto podria ser util para ti también.

:::{figure} ./01_images/01_vscode.png
:label: fig:vscode

Cuaderno de Jupyter abierto en mi VSCode.
:::

### Google Colab

En 2017 Google lanzó [Google Colab](https://developers.google.com/colab),
una aplicación en linea que permite crear, subir, editar y ejecutar
cuadernos de Jupyter completamente en linea, en un entorno Linux preconfigurado.
En 2026 está lleno de notificaciones sobre funciones de IA, pero es posible apagarlas
si prefieres.

Colab permite compartir cuadernos reproducibles fácilmente. Google permite seleccionar
entre versiones (o _snapshots_) de su entorno; selecciona uno por cuaderno y no cambiará
a menos que tu lo actualizes manualmente.
Al trabajar en linea, solo necesitas mandar un vínculo a tu colega y podrá ver y
reproducir tu trabajo.
Estos entornos son particularmente útiles al hacer trabajo con bibliotecas de IA como
Keras.

Te advierto de las desventajas, de menos a más graves.
Los entornos predefinidos no permiten la misma flexibilidad que manejar un entorno local.
Lxs usuarios no tienen control sobre cuándo y a qué versión se actualizan las bibliotecas.
Finalmente, Google tiene fama de [matar proyectos](https://killedbygoogle.com/)
sin aviso previo, populares o no. Si usaras Colab, al menos debes saber cómo usar
_notebooks_ por tu cuenta por si acaso.
