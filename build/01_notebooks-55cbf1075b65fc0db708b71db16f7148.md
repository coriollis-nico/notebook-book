# Cuadernos computacionales

La comunidad científica fue de los primeros grupos en adoptar el uso profesional y a
gran escala de computadoras electrónicas.
Desde simulaciones numéricas de miles de cuerpos, análisis estadístico de miles
o millones de datos e incluso cómputo algebraico, dudo que exista un área de investigación
en la que el cómputo no sea importante en el desarrollo de nuevos resultados.
Por lo tanto, toda persona dedicada a la ciencia haría bien en familiarizarse con
el uso correcto de computadoras y con cómputo científico básico.

Hoy en día, el cómputo científico se encuentra en una intersección particular, a veces
desafortunada.
Para escribir código científico se requiere tanto _conocimiento de desarrollo de software_
como _conocimiento de dominio científico_, para implementar y validar lo que se desea
obtener.
Una persona típica que desarrolla _software_ es experta en escribir código
utilizable, eficiente y mantenible.
Una persona que se dedica a la ciencia es experta en su dominio, y puede describir
con formalidad los objetos y modelos de su interés.
El conocimiento de ambas tiene _a priori_ una intersección vacía.[^pri]
Tal vez la persona científica esté familiarizada con herramientas computacionales de uso común
en su especialidad, pero hay una gran diferencia entre código que sirve para uso personal
y código apto para ser escrutinizado y reutilizado por otras personas (no se hable sobre
poder reproducir los resultados de otras personas).

[^pri]: Ver por ejemplo
  [_Can Mathematicians Code? The Intermediate Value Theorem_ (YouTube)](https://youtu.be/gWddFxOXefo?si=_hL469iAiF7LtahM)
  y
  [_Can programmers do math? What is a real number, really_ (YouTube)](https://youtu.be/6m6ZkafwGDs?si=KBR94UFrty_E30EY)
  para una discusión informal en el contexto de resultados matemáticos.

Pensemos además en las diferencias entre la forma tradicional de presentar un resultado
científico y de presentar un proyecto de _software_. Muchas veces, el estado del _software_
no es tan interesante para la comunidad---importan más los resultados obtenidos, su análisis
y su interpretación. Al mismo tiempo, como cualquier parte de la metodología de una
investigación, el código fuente de un proyecto debe ser escrutinizable.
Considerando todo esto, personalmente no me gustaría tener que revisar un archivo
`.c`, `.py` o `.f90` de 500 líneas de código y 2,000 líneas
de comentarios explicando cómo funciona el programa y cómo usarlo.

En contextos académicos, las formas por excelencia de presentar trabajo,
proyectos y resultados son el artículo y la tarea. En ambas, se debe encontrar un
equilibrio entre ser demasiado conciso y demasiado verboso.
En un artículo se motiva la investigación, se presenta el contexto en que se sitúa el
trabajo, se explica la metodología y se discuten los resultados.
En una tarea usualmente pueden presentarse únicamente las respuestas o los resultados,
pero estos deben estar acompañados de prosa que ilustre qué se necesita para encontrar
la solución y de evidencia de que se realizó y entendió el trabajo.

Sería ideal, entonces, un formato que permitiera combinar la claridad de la prosa
explicativa con la ejecución del código relevante, en la misma forma en que se combinan
prosa y ecuaciones en documentos científicos. Este es exactamente el formato del
cuaderno computacional.

Un cuaderno computacional (o _notebook_) es

> [...] un documento compartible que combina código informático,
> descripciones en prosa, datos, visualizaciones enriquecidas como modelos 3D,
> gráficos, diagramas y figuras, y controles interactivos.
> Un _notebook_, junto con un editor [...] proporciona un entorno interactivo rápido
> para construir prototipos y explicar código, explorar y visualizar datos, y compartir
> ideas con otros.
>
> -- [Documentación de Jupyter](https://docs.jupyter.org/en/latest/#what-is-a-notebook)

Hasta ahora he descrito estos _notebooks_ como si fueran una invención nueva,
pero probablemente ya has interactuado con algunos.
Probablemente has visto tutoriales en línea de programación escritos cuadernos de Jupyter.
Si alguna vez has resuelto alguna integral usando Wolfram Mathematica[^Wolf]
estás familiarizado con la idea general.

[^Wolf]: No confundir con Wolfram Alpha. En vez de un formato de _notebook_,
  Alpha usa una interfaz más parecida a la de un motor de búsqueda, procesando una
  petición a la vez.

Tal vez te preguntes cuál es la diferencia entre escribir código en la forma tradicional
y escribirlo en un _notebook_, o por qué se sigue escribiendo código en la forma tradicional
cuando existen los _notebooks_.

...
