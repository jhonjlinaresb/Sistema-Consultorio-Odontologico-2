# Sistema de Consultorio Odontológico — Actividad 2

## Base del proyecto

Este repositorio parte de una copia del proyecto del [primer repositorio](https://github.com/jhonjlinaresb/Sistema-Consultorio-Odontologico). Se toma ese código como base para reutilizar y adaptar las clases, modelos y fragmentos que sean útiles para resolver esta segunda actividad. La aplicación se modificará para incorporar las estructuras de datos solicitadas: una **pila** para las urgencias de extracción y una **cola** para la atención diaria según la agenda.

El archivo `main.py` conserva la demostración previa. La solución de esta actividad se ejecuta por separado desde `main_actividad_2.py`.

## Orientaciones de desarrollo

El estudiante elegirá o emulará un consultorio odontológico; sobre este, adelantará un plan de contingencia para los clientes que tienen citas pendientes de extracción de piezas dentales y que además tienen carácter urgente. Por lo anterior es necesario diseñar un programa que genere una Pila de clientes para atender directamente en la clínica y los cuales van a ser llamados de acuerdo con los siguientes criterios:

- Solo serán llamados los clientes que vengan para extracciones dentales.
- Solo se atenderán además aquellos que tengan una prioridad de “Urgente”.
- La pila quedará en orden de fecha de la más cercana a la más lejana.
- Generar un informe de la Pila para que en la clínica puedan llamar a los clientes y atenderlos prioritariamente.

El consultorio odontológico atenderá diariamente los clientes que llegan, los cuales serán gestionados en el estricto orden que define la agenda. Generar la agenda e ir atendiendo los clientes a través de la implementación de una Cola de atención. El resultado de la actividad será subido a plataforma educativa.

## Criterios de evaluación

- Completitud en programa elaborado.
- Resolución de las actividades propuestas.
- Uso adecuado de las Estructuras de Pilas y Colas.
- Entrega de programas para la implementación de las Pilas.
- Entrega de programas para la implementación de las colas.

## Adaptación prevista

Se aprovecharán los componentes existentes del proyecto base que sean pertinentes —por ejemplo, los modelos de cliente y cita, la fecha, el tipo de atención y la prioridad— y se adaptarán o ampliarán para:

1. Crear e informar una pila que incluya únicamente citas urgentes de extracción, ordenadas por fecha próxima.
2. Crear la agenda diaria y gestionar la atención de sus clientes mediante una cola, respetando el orden establecido en la agenda.
3. Probar ambas estructuras con casos que permitan verificar sus filtros y el orden de atención.

## Requisitos trabajados

- Formar una pila únicamente con citas de **extracción** y prioridad **urgente**.
- Ordenar las citas de urgencia por fecha, desde la más cercana hasta la más lejana.
- Generar un informe para efectuar los llamados prioritarios.
- Crear la agenda de un día y atender sus citas en el orden establecido mediante una cola FIFO.

## Relación con las unidades del curso

- **Unidad 4 — Pilas (stack):** `PilaUrgencias` usa LIFO. La próxima extracción urgente queda en la cima y se retira primero.
- **Unidad 5 — Colas:** `ColaAtencion` usa FIFO. Se atiende primero la cita que se agregó antes a la agenda.

La pila y la cola se muestran como dos demostraciones de estructuras distintas. Por ello, una cita urgente puede aparecer en ambas salidas: el llamado prioritario de la pila no modifica automáticamente la agenda diaria usada en la demostración de la cola.

## Archivos principales

- `main_actividad_2.py`: crea los ejemplos, ejecuta la demostración de la pila y la cola, y captura la excepción cuando se intenta retirar de estructuras vacías.
- `src/estructuras/pila_urgencias.py`: aplica el filtro de extracción urgente y ofrece operaciones de pila e informe.
- `src/estructuras/cola_atencion.py`: gestiona la agenda con operaciones FIFO.
- `src/estructuras/ordenamiento_burbuja.py`: ordena las citas por fecha mediante burbuja.
- `src/excepciones/estructura_vacia_error.py`: define `EstructuraVaciaError`, compartida por la pila y la cola.
- `src/modelos/consultorio.py`: integra los modelos reutilizados con las estructuras.

## Excepción personalizada

`EstructuraVaciaError` se encuentra en `src/excepciones/estructura_vacia_error.py`. Se lanza cuando se intenta desapilar o consultar una pila vacía, o atender o consultar una cola vacía. El programa principal muestra ambos casos y captura la excepción para evitar que termine con un traceback.

## Ejecución

Desde la carpeta raíz del repositorio, en PowerShell:

```powershell
python main_actividad_2.py
```

## Referencias bibliográficas del curso

- Becerra Santamaria, Cesar. (2002). *Estructuras de Datos en C++*. Editorial Kimpres Ltda. Estructuras dinámicas de datos: listas en Java, concepto de lista.
- GeeksforGeeks. *Various Topics on Data Structures and Algorithms*.
- Goodrich, M. T., Tamassia, R., & Goldwasser, M. H. (2020). *Data Structures and Algorithms in Python*. John Wiley & Sons.
- Hernández Bejarano, M., & Baquero Rey, L. E. (2022). *Estructuras de Datos*. Madrid, España: Rama Editorial.
- Jaime Sisa, A. (2002). *Estructuras de datos y algoritmos con énfasis en programación orientada a objetos*. Bogotá, Colombia: Prentice-Hall.
- Joyanes, L. (2011). *Estructuras de datos en C++*. McGraw Hill.
- Joyanes Aguilar, L. (2020). *Fundamentos de programación: Algoritmos, estructura de datos y objetos*. Bogotá, Colombia: McGraw-Hill Interamericana.
- Lafore, R. (2002). *Data Structures & Algorithms in Java*. Sams Publishing.
- Moreno Pérez, J. C. (2011). *Programación*. Madrid, España: Rama Editorial.
- Sedgewick, R., & Wayne, K. (2011). *Algorithms, Part I*. Coursera.
- Skiena, S. S. (2020). *The Algorithm Design Manual*. Springer.
- Villalobos, F. (2008). *Estructuras de Datos en C++*. Alfaomega.
- Zorita, M. A. (2012). *Estructuras de datos en Java*. Alfaomega.

## Recursos para profundizar

- [Tutorial oficial de Python: estructuras de datos](https://docs.python.org/3/tutorial/datastructures.html), apartados “Using Lists as Stacks” y “Using Lists as Queues”.
- [Documentación oficial de `collections.deque`](https://docs.python.org/3/library/collections.html#collections.deque), usada por la cola del proyecto.
- [OpenDSA: Stacks and Queues](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3S26notes/html/StackQueue.html), explicación y visualizaciones de las dos estructuras.
- [OpenDSA: Queues](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/Queue.html), definición y funcionamiento FIFO.
- [OpenDSA: Bubble Sort](https://opendsa-server.cs.vt.edu/ODSA/StandaloneModules/20260113154638/html/BubbleSort.html), explicación y animación del ordenamiento burbuja.