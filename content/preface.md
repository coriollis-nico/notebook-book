::: {warning} Este sitio está en construcción
Esta guía está incompleta. Esta advertencia será removida cuando crea que está en un
estado útil, y aún después tomará un tiempo en alcanzar un estado "pulido".
:::

# Introducción

Mi objetivo con estas notas es enseñar a estudiantes de licenciatura en física a usar
las herramientas estándar de Python para escribir cuadernos computacionales para
presentar métodos y resultados de forma *letrada* y *visual*.[^help]

[^help]: Por supuesto, espero que esto pueda ser de ayuda a profesionales y a gente que
  no trabaja en física (tal vez incluso que no trabaja en ciencia), pero debo escribir
  sobre lo que conozco, y no conozco mucho afuera del mundo de la física.

En el primer capítulo motivaremos el uso de cuadernos computacionales, principalmente como
herramienta de exploración y de presentación de resultados, y presentaremos una breve guía
a los cuadernos de Jupyter.
En el segundo capítulo presentaremos herramientas y métodos de visualización.
Finalmente, en el tercer capítulo presentaremos varios ejemplos de presentación de resultados
en física.

## Requisitos

- **Un entorno de programación Unix** (i.e. Linux o MacOS[^unix])

  El trabajo científico debe ser compartible, reproducible y escrutinizable.
  El _software_ libre (o al menos que obedece estándares abiertos, como MacOS)
  prácticamente garantiza estas características.
  Nadie va a pagar una licencia para comprar la herramienta que le permita ver tu proyecto.
  El _software_ cerrado solo puede ser examinado y reparado por la desarrolladora, y
  la opacidad en el desarrollo de herramientas obstaculiza la reproducibilidad de
  resultados. Adicionalmente, mi código de Fortran funcionará si uso el compilador de GNU,
  Intel, Microsoft, Nvidia, LLVM, en macOS, Windows, Linux etc. porque Fortran sigue estándares
  abiertos.

  Si ya usas Linux o MacOS, perfecto.
  Si no sabes qué es Linux o cómo instalarlo, no te compliques la vida;
  usa [Linux Mint](https://linuxmint.com/)
  (después de ver [esta guía en español](https://youtu.be/F8fIfx5WDxQ?si=6BreSCtTqVl42_fm))
  o usa [WSL](https://learn.microsoft.com/es-mx/windows/wsl/).
  Si necesitas más ayuda, acércate a tu amigx o profesorx. Te ayudarán con
  entusiasmo.

- **Experiencia con Python** (al menos un poco)

  Creo que el estudiantado de física en la Facultad de Ciencias de la UNAM aprende programación,
  principalmente Python, "a chingadazos": viendo fragmentos de
  tutoriales y videos y siguiendo consejos de amistades y profesorado.
  Esto es entendible; no siempre se tiene tiempo para aprendizaje estructurado de herramientas
  fuera del salón de clases.
  Sin embargo, no todo lo que se ve en videos y foros es un buen consejo, y el
  conocimiento desorganizado no permite construir herramientas más complejas.
  Recomiendo a quien lee estas notas que antes de comenzar revise un breve tutorial
  sobre programación básica y Python[^py].
  También hay una introducción concisa en @EspejelMorales2019.
  Para gente que sabe lo básico de programación,
  el [tutorial oficial de Python](https://docs.python.org/3/tutorial/index.html)
  es maravilloso.

  No recomiendo más libros específicos porque no he leído ninguno y no recomiendo videos
  porque no me gustan, pero si quien lee este documento tiene una referencia preferida,
  probablemente le funcionará muy bien también.

- **Uso de la terminal** de tu sistema operativo

  Si usas Linux o WSL, recomiendo
  [el tutorial en la documentación de Ubuntu](https://ubuntu.com/desktop/docs/en/latest/tutorial/the-linux-command-line-for-beginners/).
  También debería funcionar, al menos un poco, para MacOS.
  También necesitarás una introducción rápida a la terminal de Windows si usas WSL.

- **Competencia en física y matemáticas**

  Esta guía es sobre herramientas numéricas y de visualización, por lo que asumiré que
  entiendes la física en los ejemplos. Citaré libros didácticos en cada ejemplo.

No puedo evitar que uses "inteligencia artificial"
en tus proyectos, pero puedo invitarte a que tú leas la documentación oficial y que
intentes hacer las cosas tú mismo **antes** de recurrir al _chatbot_.[^IA]

[^py]: Tal vez un curso de Codecademy, o un libro como
  [Python Crash Course (Matthes, 3a ed.)](https://nostarch.com/python-crash-course-3rd-edition)
  (_yo no lo he leído_, pero se ve bien).

[^IA]: El costo de usar _chatbots_ con demasiada frecuencia es llamado
  *deuda cognitiva*. Ver, por ejemplo, [el famoso estudio realizado por MIT](https://www.media.mit.edu/projects/your-brain-on-chatgpt/overview/)
  en contextos académicos y [esta discusión](https://youtu.be/HTUh0OO6Kmo?si=IZIKbP6Ri3nkkWWf) en contextos
  de programación.

## Manifiesto de paquetes

Como referencia, el ambiente local en el que escribí y probé el código en este libro es
- Fedora Linux `44 x86_64`
- Intel Core i5-10400F
- NVIDIA GeForce GTX 1660 SUPER
- Python `3.14.6`
- NumPy `2.5.0`
- Matplotlib `3.11.0`
- SciPy `1.18.0`
- SymPy `1.14.0`
- JupyterLab `4.6.1`
- Jupyter Book `2.1.6`
- SciencePlots `2.2.2`

Introduciremos estas herramientas a lo largo del texto.
Dependiendo de cuándo se lea esta guía, las versiones más recientes del _software_ pueden
ser otras. Normalmente, mientras la versión mayor (la `x` en `x.y.z`) no haya cambiado,
el contenido debería seguir siendo útil.

## Licencias

Esta obra está bajo una licencia Creative Commons Atribución 4.0 Internacional.
Para ver una copia de esta licencia,
visita [este sitio.](https://creativecommons.org/licenses/by/4.0/deed.es)

El código en esta guía y en el repositorio está bajo licencia `MIT`.
Lea `LICENSE.txt` en el repositorio de este proyecto.
En resumen, puedes usar, copiar, modificar, fusionar, publicar, distribuir,
sublicenciar y vender copias del _software_ libremente, con la única condición
de incluir el aviso de _copyright_ y esta licencia en las copias o partes
sustanciales del _software_. Se proporciona "tal cual", sin garantía de ningún tipo.



[^unix]: Si tu sistema favorito `UNIX` no está en esta lista, no necesitas mi ayuda.
