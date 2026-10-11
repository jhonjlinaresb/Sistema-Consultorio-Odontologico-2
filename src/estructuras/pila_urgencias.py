from typing import Iterable, List, Optional
from src.excepciones.estructura_vacia_error import EstructuraVaciaError
from src.modelos.cita import Cita
from src.modelos.prioridad_atencion import PrioridadAtencion
from src.modelos.tipo_atencion import TipoAtencion
from src.estructuras.ordenamiento_burbuja import ordenar_por_fecha_burbuja

class PilaUrgencias:
    def __init__(self, citas: Optional[Iterable[Cita]] = None) -> None:
        self._elementos: List[Cita] = []
        if citas is not None:
            self.cargar(citas)

    @staticmethod
    def _es_elegible(cita: Cita) -> bool:
        return (
            cita.tipo_atencion == TipoAtencion.EXTRACCION
            and cita.prioridad == PrioridadAtencion.URGENTE
        )

    def cargar(self, citas: Iterable[Cita]) -> int:
        elegibles = [cita for cita in citas if self._es_elegible(cita)]
        ordenadas_cercana_primero = ordenar_por_fecha_burbuja(elegibles)
        self._elementos = list(reversed(ordenadas_cercana_primero))
        return len(elegibles)

    def apilar(self, cita: Cita) -> bool:
        if not self._es_elegible(cita):
            return False

        self._elementos.append(cita)
        self._elementos = ordenar_por_fecha_burbuja(self._elementos, descendente=True)
        return True

    def desapilar(self) -> Cita:
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede desapilar: la pila de urgencias está vacía.")
        return self._elementos.pop()

    def ver_cima(self) -> Cita:
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede ver la cima: la pila de urgencias está vacía.")
        return self._elementos[-1]

    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0

    def __len__(self) -> int:
        return len(self._elementos)

    def generar_informe(self) -> str:
        if self.esta_vacia():
            return "No hay citas urgentes de extracción en la pila."

        lineas = ["PILA DE URGENCIAS (próxima cita primero)"]
        for posicion, cita in enumerate(reversed(self._elementos), start=1):
            cliente = cita.cliente
            lineas.append(
                f"{posicion}. Fecha {cita.fecha} |"
                f"Cédula: {cliente.cedula} | Nombre: {cliente.nombre} |"
                f"Teléfono: {cliente.telefono}"
            )
        lineas.append(f"Total de clientes urgentes de extracción: {len(self)}")
        return "\n".join(lineas)

    def como_lista_prioritaria(self) -> List[Cita]:
        return list(reversed(self._elementos))