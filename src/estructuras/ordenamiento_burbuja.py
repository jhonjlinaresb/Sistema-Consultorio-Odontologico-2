from typing import Iterable, List
from src.modelos.cita import Cita

def ordenar_por_fecha_burbuja(citas : Iterable[Cita], *, descendente: bool = False) -> List[Cita]:
    resultado = list(citas)
    n = len(resultado)

    for limite in range(n - 1, 0, -1):
        hubo_intercambio = False
        for indice in range(limite):
            fecha_actual = resultado[indice].fecha
            fecha_siguiente = resultado[indice + 1].fecha

            debe_intercambiar = (
                fecha_actual < fecha_siguiente
                if descendente
                else fecha_actual > fecha_siguiente
            )
            if debe_intercambiar:
                resultado[indice], resultado[indice + 1] = (
                    resultado[indice + 1],
                    resultado[indice],
                )
                hubo_intercambio = True

        if not hubo_intercambio:
            break

    return resultado