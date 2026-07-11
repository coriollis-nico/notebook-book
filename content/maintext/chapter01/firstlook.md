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


## Interacción básica

Los _notebooks_ consisten principalmente de código y prosa (Markdown). Hablemos de cada
una.


### Código

El contenido de los notebooks se dividen principalmente en *celdas*.
Pruébalo: abre un cuaderno en la interfaz de tu preferencia, y en la primera celda
escribe

```python
name = "Cecilia"  # o tu propio nombre
print("¡Hola, {}!".format(name))
```
y presiona `Ctrl+Enter`. Esto ejecutará el código que escribiste y mostrara la salida
abajo de la celda:

```
!Hola, Cecilia!
```

(Si en vez de ejecutar el código solo lo renderiza como Markdown, asegúrate que la
celda esté en modo Python o modo código.)

Observa debajo de la celda o a la derecha. Encontrarás un botón para crear una nueva
celda debajo. En esta escribe

```python
print("¿Qué letras en mi nombre son minúsculas? \n")
for char in name:
  print(char, "-", char.islower())
```

y presiona `Shift+Enter`.

```
¿Qué letras en mi nombre son minúsculas?

C - False
e - True
c - True
i - True
l - True
i - True
a - True
```

Te darás cuenta de que la variable `name` que definiste en la celda anterior *aún está
definida en la celda siguiente*. Cuando ejecutes un _notebook_ las variables y estados
que definas persistirán hasta que lo reinicies o lo cierres.
También nota que al usar `Shift+Enter`, o se seleccionó automaticamente la celda de abajo,
o se creo una nueva si no existía ya. Una atajo más: `Alt+Enter` ejecuta la celda
seleccionada y crea una celda debajo aunque ya exista otra.

Ahora regresa a la primera celda y cambia el nombre. Ejecuta esa celda.
Deberías ver algo como

```ipython
[3] name = "David"
    print("Hola, {}!".format(name))
```

```
Hola, David!
```

```ipython
[2] print("¿Qué letras en mi nombre son minúsculas? \n")
    for char in name:
      print(char, "-", char.islower())
```

```
¿Qué letras en mi nombre son minúsculas?

C - False
e - True
c - True
i - True
l - True
i - True
a - True
```

A pesar de que la primera celda ahora dice `David`, la segunda
(que en principio dependía de la primera) aun dice `Cecilia`.
El *núcleo* del _notebook_ ejecuta la primera celda editada *después* de haber
ejecutado el código en el que `name = "Cecilia"`. Para el núcleo, la primera celda
editada es un tercer bloque de código; no importa en qué posición del cuaderno
esté colocado, sólo importa en qué orden lo ejecutemos nosotrxs.

Recapitulemos:

- el código en el _notebook_ se divide en celdas,

- el código en celdas puede depender de código ejecutado previamente en otras celdas,

- el orden visual de las celdas no importa; solo importa en qué orden lo ejecutemos.

Este nos permite escribir y probar nuestro código por partes, en lugar de tener que
probarlo incrementalmente o todo a la vez.
Te invito a que experimentes para que internalizes estas reglas.

Por supuesto, esto puede resultar en errores cuando se pierde el hilo de qué se ha
ejecutado y cuántas veces. La solución es sencilla; hay botones en todos los editores
para reiniciar el núcleo del cuaderno y para ejecutar todas las celdas en orden.
Estos botones son fáciles de encontrar en todas las interfaces; búsca dónde están
en tu editor y pruébalos también.

Esta no-linealidad es útil al prototipar; sin embargo, tengamos el siguiente tip en
mente:

:::{tip} Lección de programación
Para verificar y confiar en tus tus resultados, reinicia y ejecuta tu _notebook_ en
orden.
:::

Sería vergonzoso creer que ha demostrado que un algoritmo funciona, cuando en realidad
no te diste cuenta que lo ejecutaste quince veces en lugar de una sola. También sería
terrible sufrir buscando un _bug_ en tu trabajo, solo para darte cuenta que tu código
está bien pero realizaste una división cinco veces en vez de una vez.


### Markdown

Otra de las grandes conveniencias de usar _notebooks_ es poder combinar código con
prosa y el formato de esta prosa es el estandar Markdown[^md].
Prueba crear una celda hasta arriba de tu cuaderno y escribe

```markdown
# Mi primer cuaderno

## Preámbulo

En esta celda pruebo las funciones Markdown
```

y ejecuta con `Ctrl+Enter`. Este texto ahora aparecerá más bonito. La sintaxis
básica es

| Sintaxis | Descripción |
|---|---|
| `# Texto` | Encabezado 1 |
| `## Texto` | Encabezado 2 |
| `**texto**` | Negrita |
| `*texto*` | Cursiva |
| `~~texto~~` | Tachado |
| `` `código` `` | Código en línea |
| `> texto` | Cita en bloque |
| `- item` | Lista no ordenada |
| `1. item` | Lista ordenada |
| `[texto](url)` | Enlace |
| `![alt](url)` | Imagen |
| `` ``` `` | Bloque de código |
| `---` | Línea horizontal |
| `\| a \| b \|` | Tabla |
| `- [ ] tarea` | Checkbox |

<!-- Tabla generada con Claude -->

Adicionalmente, puedes insertar ecuaciones matemáticas con sintaxis de $\LaTeX$.
Crea una nueva celda al final de tu cuaderno y conviértela a formato Markdown.
Busca cómo hacerlo en tu interface, y en cualquier caso, puedes presionar
`Ctrl+m` para convertirla. En esta escribe

```markdown
Para finalizar, una ecuación (aunque el código no lo necesite):

$$
  a^2 + b^2 = c^2
$$
```

y ejecútala. Debería renderizarse algo como

Para finalizar, una ecuación (aunque el código no lo necesite):

$$
\begin{equation*}
  a^2 + b^2 = c^2
\end{equation*}
$$

También puedes tener ecuaciones en la prosa: `$\pi$` se vuelve $\pi$, etc.

Puedes observar el cuaderno renderizado [aquí](first). Inmediatamente vemos que
el formato de _notebook_ se adapta muy bien a presentaciones en linea.

[^md]: Encuentra una guía rápida en https://www.markdownguide.org/.


_Et voilà_, conocemos el funcionamiento básico de cuadernos Jupyter.
Podemos juntar prosa, matemáticas y código en un formato legible por humanos
y que incluye  el código utilizado. Estos cuadernos se pueden distrubir en una variedad
de formatos---estáticos y ejecutables---pero veremos cómo hacerlo después.
