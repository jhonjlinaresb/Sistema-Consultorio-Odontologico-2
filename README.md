# Sistema de Consultorio Odontológico — Actividad 2

## Base del proyecto

Este repositorio parte de una copia del proyecto del [primer repositorio](https://github.com/jhonjlinaresb/Sistema-Consultorio-Odontologico). Se toma ese código como base para reutilizar y adaptar las clases, modelos y fragmentos que sean útiles para resolver esta segunda actividad. La aplicación se modificará para incorporar las estructuras de datos solicitadas: una **pila** para las urgencias de extracción y una **cola** para la atención diaria según la agenda.

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