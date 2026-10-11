from collections import deque
from typing import Deque, Iterable, List, Optional
from src.excepciones.estructura_vacia_error import EstructuraVaciaError
from src.modelos.cita import Cita

class ColaAtencion:
    def __init__(self, agenda: Optional[Iterable[Cita]] = None) -> None:
        contenido = agenda if agenda is not None else ()
        self._elementos: Deque[Cita] = deque(contenido)

    def encolar(self, cita: Cita) -> None:
        self._elementos.append(cita)

    def atender_siguiente(self) -> Cita:
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede atender: la cola de atención está vacía.")
        return self._elementos.popleft()

    def ver_siguiente(self) -> Cita:
        if self.esta_vacia():
            raise EstructuraVaciaError("No se puede ver el siguiente: la cola de atención está vacía.")
        return self._elementos[0]

    def esta_vacia(self) -> bool:
        return len(self._elementos) == 0

    def generar_informe(self) -> str:
        if self.esta_vacia():
            return "No hay citas pendientes en la agenda."

        lineas = ["COLA DE ATENCIÓN (orden de la agenda)"]
        for posicion, cita in enumerate(self._elementos, start=1):
            cliente = cita.cliente
            lineas.append(
                f"{posicion}. Fecha {cita.fecha} |"
                f"Cédula: {cliente.cedula} |"
                f"Nombre: {cliente.nombre} |"
                f"Atención: {cita.tipo_atencion.name} |"
            )
        lineas.append(f"Total de citas pendientes: {len(self)}")
        return "\n".join(lineas)

    def como_lista(self) -> List[Cita]:
        return list(self._elementos)

    def __len__(self) -> int:
        return len(self._elementos)    