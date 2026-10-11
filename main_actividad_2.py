from datetime import date
from src.estructuras.cola_atencion import ColaAtencion
from src.estructuras.pila_urgencias import PilaUrgencias
from src.modelos.cita import Cita
from src.modelos.cliente import Cliente
from src.modelos.consultorio import Consultorio
from src.modelos.prioridad_atencion import PrioridadAtencion
from src.modelos.tipo_atencion import TipoAtencion
from src.modelos.tipo_cliente import TipoCliente

def ejecutar_demostracion() -> None:
    consultorio = Consultorio()

    cliente_ana = Cliente(1001, "Ana Torres", 3001112233, TipoCliente.EPS)
    cliente_luis = Cliente(1002, "Luis Rojas", 3002223344, TipoCliente.PARTICULAR)
    cliente_laura = Cliente(1003, "Laura Díaz", 3003334455, TipoCliente.PREPAGADA)
    cliente_pedro = Cliente(1004, "Pedro Gil", 3004445566, TipoCliente.EPS)
    cliente_sofia = Cliente(1005, "Sofía Mora", 3005556677, TipoCliente.PARTICULAR)

    fecha_agenda = date(2026, 10, 15)
    citas = [
        Cita(cliente_ana, TipoAtencion.LIMPIEZA, 1, PrioridadAtencion.NORMAL, fecha_agenda),
        Cita(cliente_luis, TipoAtencion.EXTRACCION, 1, PrioridadAtencion.URGENTE, fecha_agenda),
        Cita(cliente_laura, TipoAtencion.CALZAS, 2, PrioridadAtencion.URGENTE, fecha_agenda),
        Cita(cliente_pedro, TipoAtencion.EXTRACCION, 1, PrioridadAtencion.URGENTE, date(2026, 10, 17)),
        Cita(cliente_sofia, TipoAtencion.EXTRACCION, 1, PrioridadAtencion.NORMAL, fecha_agenda),
    ]
    for cita in citas:
        consultorio.agregar_cita(cita)

    print("=" * 68)
    print("ACTIVIDAD 2 — PILA DE URGENCIAS (EXTRACCIONES URGENTES)")
    print("=" * 68)

    pila: PilaUrgencias = consultorio.crear_pila_urgencias()
    print("\n1) INFORME DE LA PILA DE URGENCIAS")
    print(pila.generar_informe())

    print("\n2) LLAMADO DE CLIENTES (desapilar: cima primero)")
    while not pila.esta_vacia():
        cita = pila.desapilar()
        print(f"Llamar a {cita.cliente.nombre}, cita del {cita.fecha}.")

    cola: ColaAtencion = consultorio.crear_cola_atencion(fecha_agenda)
    print(f"\n3) AGENDA DEL {fecha_agenda} Y COLA DE ATENCIÓN")
    print(cola.generar_informe())

    print("\n4) ATENCIÓN FIFO (primero en la agenda, primero atendido)")
    while not cola.esta_vacia():
        cita = cola.atender_siguiente()
        print(
            f"Atender a {cita.cliente.nombre}: "
            f"{cita.tipo_atencion.name} del {cita.fecha}."
        )

if __name__ == "__main__":
    ejecutar_demostracion()