# Sistemas-Operativos-Cajeros-Autom-ticos

Objetivo

Organizar y documentar el proyecto mediante un repositorio en GitHub, utilizando un archivo README.md como documento principal.


Instrucciones

    Cree un repositorio en GitHub con un nombre representativo del proyecto.
    Agregue un archivo README.md, que incluya el nombre del proyecto, los integrantes y la descripción de la situación seleccionada.
    Verifique que el contenido del README.md se visualice correctamente y que tenga acceso al repositorio.
    Copie la URL del repositorio y regístrela en el espacio de entrega de la actividad.


Entregable

La URL del repositorio en GitHub, con el archivo README.md documentado de acuerdo con la plantilla proporcionada.

nombre proyecto
- Cajeros automaticos

integrantes
- Jose Ruiz
- RAFAEL BRITO

descripcion
- Aplicación que simula clientes realizando operaciones financieras como retiros, depósitos y consultas en diferentes cajeros de una misma institución bancaria.




# Análisis

El escenario escogido es una aplicación que simula transacciones bancarias en diferentes cajeros automáticos de una misma institución financiera. En este sistema, el recurso principal compartido es la base de datos centralizada del banco, específicamente los registros de los saldos de los clientes.

Esto requiere una importante cooperación y sincronización, ya que diversos cajeros podrían intentar acceder y modificar el saldo de una misma cuenta. Si estas operaciones no se coordinan adecuadamente, podrían generarse condiciones de carrera y, en consecuencia, inconsistencias graves, como retirar más fondos de los disponibles o perder el registro de un depósito.

**Tabla comparativa: implementación de modelos**

| **Característica** | **Modelo de Memoria Compartida** | **Modelo de Paso de Mensajes** |
|---|---|---|
| **Arquitectura en este escenario** | Todos los cajeros acceden directamente a un espacio de memoria común donde se almacenan los saldos de las cuentas. | Los cajeros funcionan como clientes independientes que envían solicitudes (mensajes) a un servidor central del banco. |
| **Sincronización** | Requiere el uso explícito de mecanismos de control de concurrencia para bloquear la cuenta mientras se realiza la transacción. | La coordinación se realiza mediante mensajes. El servidor central recibe las peticiones en una cola y las procesa de forma estructurada. |
| **Ventajas** | Alta velocidad de acceso a los datos, ya que no existe sobrecarga por el envío de mensajes a través de una red. | Es escalable y adecuado para sistemas distribuidos. Aísla la lógica de negocio y permite que un cajero falle sin corromper directamente la memoria del servidor. |
| **Desventajas** | Presenta una alta complejidad para evitar bloqueos mutuos. Es difícil y riesgoso implementarlo en sistemas físicamente distribuidos, como una red real de cajeros. | Existe una ligera latencia debido al tiempo de comunicación por red entre el cajero y el servidor central. |

# Conclusiones

Como conclusión, se considera que el modelo de paso de mensajes tiende a ser más efectivo en situaciones realistas para gestionar la coordinación entre cajeros automáticos. Debido a la ubicación distribuida de estos dispositivos, utilizar un esquema de memoria compartida puede resultar ineficiente desde el punto de vista del hardware y presentar riesgos para la integridad y seguridad de los datos.

El paso de mensajes permite que cada cajero actúe como un nodo independiente que envía solicitudes a un servidor centralizado. Este servidor funciona como un intermediario que procesa las transacciones de forma controlada, garantizando la sincronización y contribuyendo a mantener la consistencia de los datos.

# Bibliografía

*Inter Process Communication tutorial*. (s. f.). [TutorialsPoint](https://www.tutorialspoint.com/inter_process_communication/index.htm).

GeeksforGeeks. (2023). *Difference between shared memory and message passing model in operating system*. [GeeksforGeeks](https://www.geeksforgeeks.org/difference-between-shared-memory-and-message-passing-model-in-operating-system/).
