# Las herramientas del cómputo científico

Podemos categorizar las herramientas del cómputo científico en dos:
*implementaciones de algoritmos matemáticos y científicos* (incluyendo métodos numéricos,
estadísticos, de categorización, etc.) y de *visualización*.

Python incluye varios algoritmos comunes para manipulación de datos y un módulo
de funciones trascendentales básicas[^pytut]. Sin embargo, la mayor parte del tiempo
no usarás el modulo `math` incluido con Python sino una biblioteca que incorpora
arreglos matriciales, algoritmos comunes y mejoras de desempeño numérico
llamada *NumPy* [-@Harris2020]. NumPy te permite implementar algoritmos científicos más
rápidos que usando solo Python, pero no es necesario que lo hagas, pues los desarrolladores
de *SciPy* [-@Virtanen2020] ya lo han hecho por ti.

Python no incluye funciones de generacion de gráficos[^graf]. Para generar figuras
dependeremos por completo de bibliotecas externas, y la biblioteca estandar
para figuras científicas es *Matplotlib* [-@Hunter2007] (en parte por su integración con _notebooks_
de Jupyter).

Estas son las herramientas básicas del cómputo científico en Python
(y por lo tanto, en muchos departamentos de física). No es posible mostrar todo lo que
es posible hacer con estas herramientas en esta guía; todos estos proyectos han existido
por años, y han recibido mucha atención y mantenimiento. Afortunadamente, no necesitas
estudiar demasiado para hacer trabajo bastante bueno, y tal vez no necesites más de
lo que veremos aquí para completar tus proyectos profesionales.

La comunidad científica de nuestra generación es muy afortunada. Tras más de un
siglo de avances científicos y computacionales, hoy tenemos a nuestra disposición
herramientas avanzadas y de fácil uso. Podemos encontrar raíces e integrar
ecuaciones diferenciales
con rutinas que eligen automáticamente el mejor algoritmo, sin necesidad de saber
qué es el algoritmo de Brent o cómo implementar un Runge-Kutta sencillo. Me
encantaría presentar aquí los métodos numéricos básicos, pero ese no es el tema de
estas notas. Aún así, hablaré un poco de los algoritmos relevantes en el apéndice de
este trabajo.


[^pytut]: Ver la [documentación de Python](https://docs.python.org/3/tutorial/index.html)

[^graf]: Módulos como `turtle` no cuentan...
